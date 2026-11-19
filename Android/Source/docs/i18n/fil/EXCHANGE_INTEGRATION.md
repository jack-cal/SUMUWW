# SUMUWW Android 0.6.103 · Interface ng node

SUMUWW Android 0.6.103 · Sinusuri, iniimbak, ipinapasa at ipinapakita ng node ang datos ng chain.

[Dokumentasyon](../../integration/docs/i18n/fil/EXCHANGE_INTEGRATION.html)

<!-- payment-policy-20261116 -->

## Bayarin, nasuring transaksiyon, at pagiging tugma

Ang bayarin ay kabuuan ng mga input na binawasan ng kabuuan ng mga output. Isinasama lang sa tantiya ang output ng sukli kapag talagang gagawa ang wallet ng sukleng pasok sa itinakdang hangganan. Ang sobrang halagang mas mababa rito ay idinaragdag sa bayarin; ipinapakita ang huling bayarin at kabuuang ibabawas upang masuri. Yugeon/vB ang yunit ng rate. Ang virtual na laki ay bigat ng transaksiyon na hinati sa apat at ini-round up.

Minsan lang pinipili ng wallet ang mga input at output, at ang mismong planong iyon ang nilalagdaan. Sa pagkumpirma, ipinapadala ang nakaimbak na pirmadong transaksiyon nang hindi muling binubuo o kinakalkula ang bayarin. Kapag paso na ang tantiya o nagastos na ang isang input, kailangan ng panibagong pagsusuri. Ang pagtanggap sa lokal na pila ay hindi pa kumpirmasyon sa isang block.

Sa karaniwang P2WPKH na bayad, gumagawa ang wallet ng low-R at low-S na pirmang hindi hihigit sa 71 byte, kasama ang SIGHASH_ALL byte. Patakaran ito sa pagpirma at pagtantiya ng laki, hindi bagong limitasyon ng consensus para sa ibang wastong pirma. Maaaring mas maliit ang aktuwal na virtual na laki kapag mas maikli ang pirma. 

## Pagiging tugma ng pirma sa Android

Hindi nagbago ang format ng wallet file, mga address, at umiiral na mga coin. Maibabalik ang dating naka-encrypt na backup sa bagong app upang magamit pa rin ang parehong wallet. Bagong release signing key ang ginagamit ng Android node 0.6.103 at wallet 1.1.13. Hindi nila mapapalitan ang naka-install na app na nilagdaan gamit ang ibang key. Panatilihin ang lumang app at datos nito hangga’t walang naka-encrypt na backup ng wallet at gumaganang paraan ng pagbawi. Huwag alisin ang lumang app para lamang piliting mai-install ang update.

<!-- /payment-policy-20261116 -->
