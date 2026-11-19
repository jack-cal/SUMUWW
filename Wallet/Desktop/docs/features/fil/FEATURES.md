# SUMUWW Wallet PC 1.0.15

Karaniwang nagbubukas ang node ng 10 papalabas na koneksyon. Karamihan ay nagpapasa ng mga bloke at transaksyon. Maaari itong gumamit ng nasubukang reserbang koneksyon para sa mga bloke at pansamantalang magbukas ng ika-11 koneksyon para maghanap ng ibang node. Hanggang 125 ang kabuuan. Tumatanggap ito ng hanggang 117 papasok na koneksyon, o 115 kapag may 10 papalabas.

1 SMW = 100,000,000 yugeon. May tatlong antas ang awtomatikong bayad batay sa lokal na obserbasyon, ngunit walang garantisadong oras ng kumpirmasyon. Maaari kang magtakda ng rate sa yugeon/vB. Suriin ang huling bayad at kabuuang SMW bago magpadala. Hindi nababawasan ang balanse sa tinanggihang transaksiyon.

Kapag gumamit ka ng isang input na nagkakahalaga ng 1 SMW, nakadepende ang bayad sa kung may isusukli. Kung P2WPKH ang input at lahat ng output at 1 yugeon/vB ang singil, 110 yugeon ang bayad sa pagpapadala ng 0.99999890 SMW at walang sukli. Kung 0.8 SMW ang ipapadala mula sa parehong input, madaragdagan ng isang output para sa sukli at magiging 141 yugeon ang bayad. Ibinabalik ng wallet ang sukli kung ang natitira matapos ibawas ang bayad ay umabot sa minimum na halaga. Isinasaalang-alang sa minimum na ito ang gastos sa paggamit ng sukli sa hinaharap. Kung mas maliit ang natira, isinasama ito sa bayad na makikita mo bago kumpirmahin ang padala. Para sa input ng wallet na gumagamit ng native SegWit (P2WPKH), hanggang 71 byte ang inilalaan sa lagda sa pagtatantiya ng laki, kasama ang uri ng hash.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Batay ang awtomatikong bayad sa dami ng nakabinbing datos, kapasidad ng bloke at prayoridad ng transaksiyon. Hindi ginagamit ang bayad ng mga nakaraang bloke. Kapag maikli ang pila, nananatili ang pinakamababang singil. Naa-update ang preview; itinatakda ng huling kumpirmasyon ang bayad. Ang obserbasyon ay para sa nakakonektang lokal na node, hindi sa lahat ng node.

Nananatili ang tala ng mga pagpapalit na naitala ng node na ito kahit i-restart ang wallet. Hindi naaapektuhan ng mga inalis na transaksiyon ang balanse.

Hiwalay sa kasaysayan ng pagmimina ang bagong inilabas, bayarin sa transaksyon, at kabuuang gantimpala ng bawat block. Hiwalay ding ipinapakita ang natanggap ng iyong wallet. Kapag bahagi lamang ang kinuha, hindi ipinapalagay ang paghahati ng dalawang sangkap. May 28 RPC method ang node, kabilang ang pagtatantiya ng bayarin, at sinusuri at ipinapasa nito ang mga nilagdaang transaksyon.

<!-- payment-policy-20261116 -->

## Bayarin, nasuring transaksiyon, at pagiging tugma

Ang bayarin ay kabuuan ng mga input na binawasan ng kabuuan ng mga output. Isinasama lang sa tantiya ang output ng sukli kapag talagang gagawa ang wallet ng sukleng pasok sa itinakdang hangganan. Ang sobrang halagang mas mababa rito ay idinaragdag sa bayarin; ipinapakita ang huling bayarin at kabuuang ibabawas upang masuri. Yugeon/vB ang yunit ng rate. Ang virtual na laki ay bigat ng transaksiyon na hinati sa apat at ini-round up.

Minsan lang pinipili ng wallet ang mga input at output, at ang mismong planong iyon ang nilalagdaan. Sa pagkumpirma, ipinapadala ang nakaimbak na pirmadong transaksiyon nang hindi muling binubuo o kinakalkula ang bayarin. Kapag paso na ang tantiya o nagastos na ang isang input, kailangan ng panibagong pagsusuri. Ang pagtanggap sa lokal na pila ay hindi pa kumpirmasyon sa isang block.

Sa karaniwang P2WPKH na bayad, gumagawa ang wallet ng low-R at low-S na pirmang hindi hihigit sa 71 byte, kasama ang SIGHASH_ALL byte. Patakaran ito sa pagpirma at pagtantiya ng laki, hindi bagong limitasyon ng consensus para sa ibang wastong pirma. Maaaring mas maliit ang aktuwal na virtual na laki kapag mas maikli ang pirma. 

<!-- /payment-policy-20261116 -->

Kapag nakatanggap ng wastong tugon tungkol sa bersyon, binibigyan ng node ng oras ang kabilang node na magpadala ng kumpirmasyon. Kung dalawang papalabas na koneksyon ang patungo sa iisang node, mananatiling bukas ang isang magagamit na ruta hanggang sa matapos ang pag-sync sa isa sa mga ito. 
