# SUMUWW Android 0.6.98 · Dokumentasyon

Kumokonekta ang telepono sa isang SUMUWW full node na may bersyong 0.57.49 o mas bago. Sinusuri nito ang gantimpala at kinakalkula ang proof of work nang hindi dina-download ang buong kasaysayan ng mga transaksyon.

Lalabas ang inirerekomendang bayad kapag naibigay na ng nakakonektang node ang datos. Ipapakita ng wallet ang nakabinbing pagbabago sa balanse kapag nasuri na ang buong halaga.

## Kasaysayan ng pagmimina

Ang mga block na mismong minina ng teleponong ito lang ang makikita rito. I-tap ang tala para makita ang gantimpala at bilang ng kumpirmasyon.

## Network at mga address

Ang pampublikong network ay `sumuww`, na may panloob na alyas na `dora`. Suriin ang genesis hash sa ibaba. Gumagamit ang katutubong address ng witness v0 P2WPKH at HASH160 ng compressed secp256k1 public key. Walang kailangang memo o tag. Tanggihan ang maling network at di-wastong checksum. Itala ang HD branch para sa pagtanggap/sukli at index; huwag ipalagay ang derivation path ng Bitcoin.

## Halaga at magagamit na output

Ang `_units` ay integer sa pinakamaliit na yunit; `_smw` ay string na may 8 decimal; `_dora` ay compatibility alias. Walang amount field na `_sumuww`. 1 SMW = 100000000 yunit. Walang `spendable` ang `gettxout` at maaaring magbalik ng hindi pa hinog na coinbase output. Kailangan ng hindi bababa sa 100 kumpirmasyon para gastusin sa susunod na block. Salain ang `listunspent` sa `spendable`; hindi kasama sa available ng `getaddressbalance` ang hindi pa hinog at nakatali sa pending spend. Hindi kumpirmado ang bagong mempool output. Suriin ang dulo sa pagitan ng mga pahina at muling patunayan ang piniling input.

1 SMW = 100,000,000 yugeon. May tatlong antas ang awtomatikong bayad batay sa lokal na obserbasyon, ngunit walang garantisadong oras ng kumpirmasyon. Maaari kang magtakda ng rate sa yugeon/vB. Suriin ang huling bayad at kabuuang SMW bago magpadala. Hindi nababawasan ang balanse sa tinanggihang transaksiyon.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

Batay ang awtomatikong bayad sa dami ng nakabinbing datos, kapasidad ng bloke at prayoridad ng transaksiyon. Hindi ginagamit ang bayad ng mga nakaraang bloke. Kapag maikli ang pila, nananatili ang pinakamababang singil. Naa-update ang preview; itinatakda ng huling kumpirmasyon ang bayad. Ang obserbasyon ay para sa nakakonektang lokal na node, hindi sa lahat ng node.

Nananatili ang tala ng mga pagpapalit na naitala ng node na ito kahit i-restart ang wallet. Hindi naaapektuhan ng mga inalis na transaksiyon ang balanse.

Hiwalay sa kasaysayan ng pagmimina ang bagong inilabas, bayarin sa transaksyon, at kabuuang gantimpala ng bawat block. Hiwalay ding ipinapakita ang natanggap ng iyong wallet. Kapag bahagi lamang ang kinuha, hindi ipinapalagay ang paghahati ng dalawang sangkap. May 28 RPC method ang node, kabilang ang pagtatantiya ng bayarin, at sinusuri at ipinapasa nito ang mga nilagdaang transaksyon.

## Paghahanap ng transaksyon at block

Hinahanap ng `getrawtransaction` ang active chain at mempool, hindi ang transaksyong nasa naulilang sangay lamang. Tumutukoy ang input sa dating output, hindi sa iisang sender address. Boolean ang `verbose` ng `getblock`; ang naka-save na inactive block ay may `active=false`, `confirmations=-1`. Maa-access pa rin ang raw transaction sa block hash. Confirmed active spend lamang ang hinahanap ng `findspendingtransaction`; hindi patunay ng availability ang null. Suriin ang `gettxout` na may `include_mempool=true`. Maaaring magbago ang kumpirmasyon at active status sa reorganisasyon.

[API_CONTRACT.json](../../../API_CONTRACT.json)
