# Bayarin, nasuring transaksiyon, at pagiging tugma

SUMUWW · 2026-11-16

<!-- payment-policy-20261116 -->

## Bayarin, nasuring transaksiyon, at pagiging tugma

Ang bayarin ay kabuuan ng mga input na binawasan ng kabuuan ng mga output. Isinasama lang sa tantiya ang output ng sukli kapag talagang gagawa ang wallet ng sukleng pasok sa itinakdang hangganan. Ang sobrang halagang mas mababa rito ay idinaragdag sa bayarin; ipinapakita ang huling bayarin at kabuuang ibabawas upang masuri. Yugeon/vB ang yunit ng rate. Ang virtual na laki ay bigat ng transaksiyon na hinati sa apat at ini-round up.

Minsan lang pinipili ng wallet ang mga input at output, at ang mismong planong iyon ang nilalagdaan. Sa pagkumpirma, ipinapadala ang nakaimbak na pirmadong transaksiyon nang hindi muling binubuo o kinakalkula ang bayarin. Kapag paso na ang tantiya o nagastos na ang isang input, kailangan ng panibagong pagsusuri. Ang pagtanggap sa lokal na pila ay hindi pa kumpirmasyon sa isang block.

Sa karaniwang P2WPKH na bayad, gumagawa ang wallet ng low-R at low-S na pirmang hindi hihigit sa 71 byte, kasama ang SIGHASH_ALL byte. Patakaran ito sa pagpirma at pagtantiya ng laki, hindi bagong limitasyon ng consensus para sa ibang wastong pirma. Maaaring mas maliit ang aktuwal na virtual na laki kapag mas maikli ang pirma. Lokal na pila pa rin ang batayan ng mga mungkahing rate; ang pagkakatulad sa pagkalkula ng laki ng Bitcoin ay hindi nangangahulugang rate ng Bitcoin network ang ginagamit.

## I2P na bahagi sa Windows at pagsusuring panseguridad

Kasama sa Windows package ang opisyal na i2pd 3.0.0, mga bagong hash, at mga sertipiko para sa unang koneksiyon. Sa naitalang pagsusuri, natutukoy pa rin ng Defender ang opisyal na I2P executable at orihinal na ZIP. Hindi patunay ng kaligtasan o tiyak na maling pagtukoy ang pagtugma sa opisyal na hash. Ang lokal na pagbubukod sa isang file ay para lamang sa PC kung saan ito itinakda; hindi ito awtomatikong idinaragdag ng pampublikong package. Maaaring harangin ng ibang PC ang parehong mga file.

## Pagiging tugma ng pirma sa Android

Hindi nagbago ang format ng wallet file, mga address, at umiiral na mga coin. Maibabalik ang dating naka-encrypt na backup sa bagong app upang magamit pa rin ang parehong wallet. Bagong release signing key ang ginagamit ng Android node 0.6.103 at wallet 1.1.13. Hindi nila mapapalitan ang naka-install na app na nilagdaan gamit ang ibang key. Panatilihin ang lumang app at datos nito hangga’t walang naka-encrypt na backup ng wallet at gumaganang paraan ng pagbawi. Huwag alisin ang lumang app para lamang piliting mai-install ang update.

<!-- /payment-policy-20261116 -->

Kapag nakatanggap ng wastong tugon tungkol sa bersyon, binibigyan ng node ng oras ang kabilang node na magpadala ng kumpirmasyon. Kung dalawang papalabas na koneksyon ang patungo sa iisang node, mananatiling bukas ang isang magagamit na ruta hanggang sa matapos ang pag-sync sa isa sa mga ito. Tinatanggap ng pansariling pagsusuri ang bloke na may wastong proof of work bago dumating ang patunay ng koneksiyon. Pagkatapos, sinusuri nito ang lagda ng tatlong saksi, ang pagpapasa ng patunay sa ibang node, at kung naroon pa ito matapos mag-restart.
