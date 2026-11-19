# SUMUWW · Mga tala ng bersyon

Kapag gumamit ka ng isang input na nagkakahalaga ng 1 SMW, nakadepende ang bayad sa kung may isusukli. Kung P2WPKH ang input at lahat ng output at 1 yugeon/vB ang singil, 110 yugeon ang bayad sa pagpapadala ng 0.99999890 SMW at walang sukli. Kung 0.8 SMW ang ipapadala mula sa parehong input, madaragdagan ng isang output para sa sukli at magiging 141 yugeon ang bayad. Ibinabalik ng wallet ang sukli kung ang natitira matapos ibawas ang bayad ay umabot sa minimum na halaga. Isinasaalang-alang sa minimum na ito ang gastos sa paggamit ng sukli sa hinaharap. Kung mas maliit ang natira, isinasama ito sa bayad na makikita mo bago kumpirmahin ang padala. Para sa input ng wallet na gumagamit ng native SegWit (P2WPKH), hanggang 71 byte ang inilalaan sa lagda sa pagtatantiya ng laki, kasama ang uri ng hash.

0.57.61 · Kapag nagpalit ka ng wika habang bukas ang app, magbabago rin ang icon nito sa taskbar ng Windows.

Karaniwang nagbubukas ang node ng 10 papalabas na koneksyon. Karamihan ay nagpapasa ng mga bloke at transaksyon. Maaari itong gumamit ng nasubukang reserbang koneksyon para sa mga bloke at pansamantalang magbukas ng ika-11 koneksyon para maghanap ng ibang node. Hanggang 125 ang kabuuan. Tumatanggap ito ng hanggang 117 papasok na koneksyon, o 115 kapag may 10 papalabas. Kabuuang bilang na lang ng mga nakakonektang node ang makikita sa desktop app. Bawat minero ang bumubuo ng sarili nitong mga block. Ipinapasa ng PC node ang mga natapos na block at tinatanggihan ang mga hiling na trabaho sa pagmimina at mga solusyong galing sa telepono.

Kapag muling binuksan, magpapatuloy ang node mula sa huling block na sinuri nito sa device at susuriin ang mga bagong block. Kung wala o hindi tugma ang nakaimbak na tala ng pagsusuri, susuriin nitong muli ang nakaimbak na kasaysayan.

SUMUWW PC 0.57.61 · Sinusuri, iniimbak, ipinapasa at ipinapakita ng node ang datos ng chain.

## Pormat ng lagda

Binubuo ng opsyonal na source SDK ang transaksiyon at sinusuri ang ibinigay na lagda nang walang susi o network. Hindi ito programang lumalagda o utos ng node. Sa format ng halimbawa lang ang limitasyong P2WPKH, hindi sa node. Magagamit pa rin ang personal na wallet.

## RPC at HTTP API

Sinusuri ng validateaddress ang checksum at napiling network. Ang decoded_only mula sa decoderawtransaction ay pagbasa lang ng datos, hindi patunay ng wastong lagda o kumpirmasyon. Nag-iimbak ang OP_RETURN ng datos para sa panlabas na programa. May dagdag na pagtatanong ng bayad, pagsusuri bago magpadala, katayuan ng pagpapalit sa RBF at datos ayon sa pagkakasunod ng mga block. Sinusuri muna ang kapalit bago alisin ang mga nakabinbing transaksiyon. Naipatupad ang maramihang lagda at naka-lock na output para sa hiwalay na pagsubok; hindi pa aktibo sa pampublikong network.

## Beripikasyon

I-install ang dependencies at patakbuhin ang python examples/node_contract.py mula sa source. Pampublikong test key at pansamantalang regtest ang sumusubok sa pagpapasa, pagtanggi, kumpirmasyon, reorganisasyon at pag-iimbak. Walang totoong pondo, profile ng user o hardware signer na ginagamit.

[Dokumentasyon](README.html) · [Interface ng node](EXCHANGE_INTEGRATION.html) · [RPC at HTTP API](RPC_API.html) · [Pagpapatakbo ng node](NETWORK_RUNBOOK.html) · [Beripikasyon](EXCHANGE_EXAMPLES.html)

[Detalyadong sanggunian sa Ingles](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Bayarin, nasuring transaksiyon, at pagiging tugma

Ang bayarin ay kabuuan ng mga input na binawasan ng kabuuan ng mga output. Isinasama lang sa tantiya ang output ng sukli kapag talagang gagawa ang wallet ng sukleng pasok sa itinakdang hangganan. Ang sobrang halagang mas mababa rito ay idinaragdag sa bayarin; ipinapakita ang huling bayarin at kabuuang ibabawas upang masuri. Yugeon/vB ang yunit ng rate. Ang virtual na laki ay bigat ng transaksiyon na hinati sa apat at ini-round up.

Minsan lang pinipili ng wallet ang mga input at output, at ang mismong planong iyon ang nilalagdaan. Sa pagkumpirma, ipinapadala ang nakaimbak na pirmadong transaksiyon nang hindi muling binubuo o kinakalkula ang bayarin. Kapag paso na ang tantiya o nagastos na ang isang input, kailangan ng panibagong pagsusuri. Ang pagtanggap sa lokal na pila ay hindi pa kumpirmasyon sa isang block.

Sa karaniwang P2WPKH na bayad, gumagawa ang wallet ng low-R at low-S na pirmang hindi hihigit sa 71 byte, kasama ang SIGHASH_ALL byte. Patakaran ito sa pagpirma at pagtantiya ng laki, hindi bagong limitasyon ng consensus para sa ibang wastong pirma. Maaaring mas maliit ang aktuwal na virtual na laki kapag mas maikli ang pirma. 

<!-- /payment-policy-20261116 -->
