# SUMUWW Android 0.6.103 · Pagpapatakbo ng node

Kapag muling binuksan, magpapatuloy ang node mula sa huling block na sinuri nito sa device at susuriin ang mga bagong block. Kung wala o hindi tugma ang nakaimbak na tala ng pagsusuri, susuriin nitong muli ang nakaimbak na kasaysayan.

SUMUWW Android 0.6.103 · Sinusuri, iniimbak, ipinapasa at ipinapakita ng node ang datos ng chain.

## Network at mga address

Ang pampublikong network ay `sumuww`, na may panloob na alyas na `dora`. Suriin ang genesis hash sa ibaba. Gumagamit ang katutubong address ng witness v0 P2WPKH at HASH160 ng compressed secp256k1 public key. Walang kailangang memo o tag. Tanggihan ang maling network at di-wastong checksum. Itala ang HD branch para sa pagtanggap/sukli at index; huwag ipalagay ang derivation path ng Bitcoin.

## Paghahanap ng transaksyon at block

Hinahanap ng `getrawtransaction` ang active chain at mempool, hindi ang transaksyong nasa naulilang sangay lamang. Tumutukoy ang input sa dating output, hindi sa iisang sender address. Boolean ang `verbose` ng `getblock`; ang naka-save na inactive block ay may `active=false`, `confirmations=-1`. Maa-access pa rin ang raw transaction sa block hash. Confirmed active spend lamang ang hinahanap ng `findspendingtransaction`; hindi patunay ng availability ang null. Suriin ang `gettxout` na may `include_mempool=true`. Maaaring magbago ang kumpirmasyon at active status sa reorganisasyon.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Bayarin, nasuring transaksiyon, at pagiging tugma

Ang bayarin ay kabuuan ng mga input na binawasan ng kabuuan ng mga output. Isinasama lang sa tantiya ang output ng sukli kapag talagang gagawa ang wallet ng sukleng pasok sa itinakdang hangganan. Ang sobrang halagang mas mababa rito ay idinaragdag sa bayarin; ipinapakita ang huling bayarin at kabuuang ibabawas upang masuri. Yugeon/vB ang yunit ng rate. Ang virtual na laki ay bigat ng transaksiyon na hinati sa apat at ini-round up.

Minsan lang pinipili ng wallet ang mga input at output, at ang mismong planong iyon ang nilalagdaan. Sa pagkumpirma, ipinapadala ang nakaimbak na pirmadong transaksiyon nang hindi muling binubuo o kinakalkula ang bayarin. Kapag paso na ang tantiya o nagastos na ang isang input, kailangan ng panibagong pagsusuri. Ang pagtanggap sa lokal na pila ay hindi pa kumpirmasyon sa isang block.

Sa karaniwang P2WPKH na bayad, gumagawa ang wallet ng low-R at low-S na pirmang hindi hihigit sa 71 byte, kasama ang SIGHASH_ALL byte. Patakaran ito sa pagpirma at pagtantiya ng laki, hindi bagong limitasyon ng consensus para sa ibang wastong pirma. Maaaring mas maliit ang aktuwal na virtual na laki kapag mas maikli ang pirma. Lokal na pila pa rin ang batayan ng mga mungkahing rate; ang pagkakatulad sa pagkalkula ng laki ng Bitcoin ay hindi nangangahulugang rate ng Bitcoin network ang ginagamit.

## Pagiging tugma ng pirma sa Android

Hindi nagbago ang format ng wallet file, mga address, at umiiral na mga coin. Maibabalik ang dating naka-encrypt na backup sa bagong app upang magamit pa rin ang parehong wallet. Bagong release signing key ang ginagamit ng Android node 0.6.103 at wallet 1.1.13. Hindi nila mapapalitan ang naka-install na app na nilagdaan gamit ang ibang key. Panatilihin ang lumang app at datos nito hangga’t walang naka-encrypt na backup ng wallet at gumaganang paraan ng pagbawi. Huwag alisin ang lumang app para lamang piliting mai-install ang update.

<!-- /payment-policy-20261116 -->

Kapag nakatanggap ng wastong tugon tungkol sa bersyon, binibigyan ng node ng oras ang kabilang node na magpadala ng kumpirmasyon. Kung dalawang papalabas na koneksyon ang patungo sa iisang node, mananatiling bukas ang isang magagamit na ruta hanggang sa matapos ang pag-sync sa isa sa mga ito. Tinatanggap ng pansariling pagsusuri ang bloke na may wastong proof of work bago dumating ang patunay ng koneksiyon. Pagkatapos, sinusuri nito ang lagda ng tatlong saksi, ang pagpapasa ng patunay sa ibang node, at kung naroon pa ito matapos mag-restart.
