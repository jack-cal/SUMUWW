# SUMUWW · Pagpapatakbo ng node

Karaniwang nagbubukas ang node ng 10 papalabas na koneksyon. Karamihan ay nagpapasa ng mga bloke at transaksyon. Maaari itong gumamit ng nasubukang reserbang koneksyon para sa mga bloke at pansamantalang magbukas ng ika-11 koneksyon para maghanap ng ibang node. Hanggang 125 ang kabuuan. Tumatanggap ito ng hanggang 117 papasok na koneksyon, o 115 kapag may 10 papalabas. Kabuuang bilang na lang ng mga nakakonektang node ang makikita sa desktop app. Bawat minero ang bumubuo ng sarili nitong mga block. Ipinapasa ng PC node ang mga natapos na block at tinatanggihan ang mga hiling na trabaho sa pagmimina at mga solusyong galing sa telepono.

Kapag muling binuksan, magpapatuloy ang node mula sa huling block na sinuri nito sa device at susuriin ang mga bagong block. Kung wala o hindi tugma ang nakaimbak na tala ng pagsusuri, susuriin nitong muli ang nakaimbak na kasaysayan.

SUMUWW PC 0.57.61 · Sinusuri, iniimbak, ipinapasa at ipinapakita ng node ang datos ng chain.

## Network at mga address

Ang pampublikong network ay `sumuww`, na may panloob na alyas na `dora`. Suriin ang genesis hash sa ibaba. Gumagamit ang katutubong address ng witness v0 P2WPKH at HASH160 ng compressed secp256k1 public key. Walang kailangang memo o tag. Tanggihan ang maling network at di-wastong checksum. Itala ang HD branch para sa pagtanggap/sukli at index; huwag ipalagay ang derivation path ng Bitcoin.

## Pagpapatunay at mga limitasyon

Tahasang paganahin ang RPC sa numerikong loopback `127.0.0.1:18443` gamit ang pribadong Bearer token. Walang remote signing o pag-unlock ng wallet. Gumamit ng lokal na serbisyo o authenticated tunnel; tinatanggihan ang browser Origin/Referer request. Gumagamit ang JSON-RPC ng POST `/rpc`, object/array `params` at `id`; HTTP 204 ang notification. Limitasyon: body 8004096 byte, header 8192, batch 16, sabay na request 16, takdang oras 10 segundo; limit 1–1000, offset 0–1000000. May 28 method at 11 REST route.

## Paghahanap ng transaksyon at block

Hinahanap ng `getrawtransaction` ang active chain at mempool, hindi ang transaksyong nasa naulilang sangay lamang. Tumutukoy ang input sa dating output, hindi sa iisang sender address. Boolean ang `verbose` ng `getblock`; ang naka-save na inactive block ay may `active=false`, `confirmations=-1`. Maa-access pa rin ang raw transaction sa block hash. Confirmed active spend lamang ang hinahanap ng `findspendingtransaction`; hindi patunay ng availability ang null. Suriin ang `gettxout` na may `include_mempool=true`. Maaaring magbago ang kumpirmasyon at active status sa reorganisasyon.

## Beripikasyon

I-install ang dependencies at patakbuhin ang python examples/node_contract.py mula sa source. Pampublikong test key at pansamantalang regtest ang sumusubok sa pagpapasa, pagtanggi, kumpirmasyon, reorganisasyon at pag-iimbak. Walang totoong pondo, profile ng user o hardware signer na ginagamit.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Dokumentasyon](README.html) · [Interface ng node](EXCHANGE_INTEGRATION.html) · [RPC at HTTP API](RPC_API.html) · [Mga tala ng bersyon](RELEASE_NOTES.html) · [Beripikasyon](EXCHANGE_EXAMPLES.html)

[Detalyadong sanggunian sa Ingles](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Bayarin, nasuring transaksiyon, at pagiging tugma

Ang bayarin ay kabuuan ng mga input na binawasan ng kabuuan ng mga output. Isinasama lang sa tantiya ang output ng sukli kapag talagang gagawa ang wallet ng sukleng pasok sa itinakdang hangganan. Ang sobrang halagang mas mababa rito ay idinaragdag sa bayarin; ipinapakita ang huling bayarin at kabuuang ibabawas upang masuri. Yugeon/vB ang yunit ng rate. Ang virtual na laki ay bigat ng transaksiyon na hinati sa apat at ini-round up.

Minsan lang pinipili ng wallet ang mga input at output, at ang mismong planong iyon ang nilalagdaan. Sa pagkumpirma, ipinapadala ang nakaimbak na pirmadong transaksiyon nang hindi muling binubuo o kinakalkula ang bayarin. Kapag paso na ang tantiya o nagastos na ang isang input, kailangan ng panibagong pagsusuri. Ang pagtanggap sa lokal na pila ay hindi pa kumpirmasyon sa isang block.

Sa karaniwang P2WPKH na bayad, gumagawa ang wallet ng low-R at low-S na pirmang hindi hihigit sa 71 byte, kasama ang SIGHASH_ALL byte. Patakaran ito sa pagpirma at pagtantiya ng laki, hindi bagong limitasyon ng consensus para sa ibang wastong pirma. Maaaring mas maliit ang aktuwal na virtual na laki kapag mas maikli ang pirma. 

<!-- /payment-policy-20261116 -->

Kapag nakatanggap ng wastong tugon tungkol sa bersyon, binibigyan ng node ng oras ang kabilang node na magpadala ng kumpirmasyon. Kung dalawang papalabas na koneksyon ang patungo sa iisang node, mananatiling bukas ang isang magagamit na ruta hanggang sa matapos ang pag-sync sa isa sa mga ito. 
