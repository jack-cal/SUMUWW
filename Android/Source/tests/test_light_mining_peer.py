"""Real loopback full node and mobile service, using disposable wallets and databases."""
import asyncio
from concurrent.futures import Future
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

MOBILE = Path(__file__).resolve().parents[1] / 'app/src/main/python'
PC = Path(__file__).resolve().parents[3] / 'PC/Source'
# Use the host coincurve package rather than Android JNI in this host test.
import coincurve
sys.path.insert(0, str(MOBILE))
from light_service import LightService
from sumuww.primitives import COIN

SERVER = """
import asyncio,sys
from pathlib import Path
from sumuww.peer import PeerNode
from sumuww.address import decode_address
async def main():
    node=PeerNode(Path(sys.argv[1])/'node.sqlite')
    await node.start()
    print(node.address[1],flush=True)
    while True:
        line=(await asyncio.to_thread(sys.stdin.readline)).strip()
        if line=='quit' or not line: break
        action,address=line.split()
        script=decode_address(address,network=node.network)
        if action=='fund':
            node.chain.mine(script,101)
        if action=='reorg':
            parent=node.chain.get_block(node.chain.tip_hash).header.previous_hash
            one=node.chain.make_block(script,parent_hash=parent,extra_nonce=42)
            node.chain.accept_block(one)
            node.chain.accept_block(node.chain.make_block(script,parent_hash=one.block_hash()))
        print('ok',flush=True)
    await node.stop()
asyncio.run(main())
"""

class LightMiningTest(unittest.TestCase):
    def test_device_work_only_and_wallet_payment(self):
        with tempfile.TemporaryDirectory() as root:
            full = Path(root)/'full'
            full.mkdir()
            phone = Path(root)/'phone'
            server = subprocess.Popen([sys.executable,'-u','-c',SERVER,str(full)],cwd=PC,
                                      env=dict(os.environ,PYTHONPATH=str(PC)),text=True,
                                      stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            def command(line):
                server.stdin.write(line+'\n')
                server.stdin.flush()
            port=int(server.stdout.readline())
            def new_mobile():
                svc=LightService(phone,network='regtest',peers=[f'127.0.0.1:{port}'])
                svc.start().result(20)
                return svc
            def wait_for(test):
                until = time.monotonic()+30
                while time.monotonic()<until:
                    if test():return
                    time.sleep(.15)
                self.fail('Mobile state did not converge')
            svc=new_mobile()
            try:
                wallet=svc.create_wallet('wallet.json','local-light-test-password').result(10)
                address=wallet['address']
                command('fund '+address)
                self.assertEqual('ok',server.stdout.readline().strip())
                wait_for(lambda:svc.status().result(5)['wallet'].get('available_smw') not in (None,'0.00000000'))
                wait_for(lambda:svc.status().result(5)['wallet'].get('pending_smw')=='0.00000000')
                self.assertEqual(0,svc.transaction_history().result(5)['total'])
                result=svc.mine_one().result(30)
                wait_for(lambda:svc.transaction_history().result(10)['transactions'][0]['confirmations']==1)
                row=svc.transaction_history().result(5)['transactions'][0]
                self.assertEqual(result['block_hash'],row['block_hash'])
                quote=svc.prepare_payment(address,'0.01','auto:normal').result(8)
                sent=svc.submit_payment(quote['quote_id']).result(8)['txid']
                alerts=svc._submit('transfer_alerts',0).result(8)['transactions']
                self.assertTrue(any(x['txid']==sent and not x['coinbase'] for x in alerts))
                wait_for(lambda: svc.status().result(5)['wallet'].get('pending_smw') == '-' + quote['fee_smw'])
                svc.stop().result(15)
                svc=new_mobile()
                svc.open_wallet('wallet.json','local-light-test-password').result(15)
                self.assertEqual(1,svc.transaction_history().result(10)['total'])
                command('reorg '+address)
                self.assertEqual('ok',server.stdout.readline().strip())
                wait_for(lambda:svc.transaction_history().result(8)['transactions'][0]['status']=='orphaned')
                self.assertFalse((phone/'node.sqlite').exists())
            finally:
                svc.stop().result(15)
                command('quit')
                server.wait(timeout=10)
                server.stdin.close()
                server.stdout.close()

if __name__=='__main__':
    unittest.main()
