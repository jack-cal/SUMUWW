# SUMUWW · Mga tala ng bersyon

Karaniwang nagbubukas ang node ng 10 papalabas na koneksyon. Karamihan ay nagpapasa ng mga bloke at transaksyon. Maaari itong gumamit ng nasubukang reserbang koneksyon para sa mga bloke at pansamantalang magbukas ng ika-11 koneksyon para maghanap ng ibang node. Hanggang 125 ang kabuuan. Tumatanggap ito ng hanggang 117 papasok na koneksyon, o 115 kapag may 10 papalabas. Kabuuang bilang na lang ng mga nakakonektang node ang makikita sa desktop app. Bawat minero ang bumubuo ng sarili nitong mga block. Ipinapasa ng PC node ang mga natapos na block at tinatanggihan ang mga hiling na trabaho sa pagmimina at mga solusyong galing sa telepono.

Kapag muling binuksan, magpapatuloy ang node mula sa huling block na sinuri nito sa device at susuriin ang mga bagong block. Kung wala o hindi tugma ang nakaimbak na tala ng pagsusuri, susuriin nitong muli ang nakaimbak na kasaysayan.


SUMUWW PC 0.57.54 · Sinusuri, iniimbak, ipinapasa at ipinapakita ng node ang datos ng chain.

## Pormat ng lagda

Binubuo ng opsyonal na source SDK ang transaksiyon at sinusuri ang ibinigay na lagda nang walang susi o network. Hindi ito programang lumalagda o utos ng node. Sa format ng halimbawa lang ang limitasyong P2WPKH, hindi sa node. Magagamit pa rin ang personal na wallet.

## RPC at HTTP API

Sinusuri ng validateaddress ang checksum at napiling network. Ang decoded_only mula sa decoderawtransaction ay pagbasa lang ng datos, hindi patunay ng wastong lagda o kumpirmasyon. Nag-iimbak ang OP_RETURN ng datos para sa panlabas na programa. May dagdag na pagtatanong ng bayad, pagsusuri bago magpadala, katayuan ng pagpapalit sa RBF at datos ayon sa pagkakasunod ng mga block. Sinusuri muna ang kapalit bago alisin ang mga nakabinbing transaksiyon. Naipatupad ang maramihang lagda at naka-lock na output para sa hiwalay na pagsubok; hindi pa aktibo sa pampublikong network.

## Beripikasyon

I-install ang dependencies at patakbuhin ang python examples/node_contract.py mula sa source. Pampublikong test key at pansamantalang regtest ang sumusubok sa pagpapasa, pagtanggi, kumpirmasyon, reorganisasyon at pag-iimbak. Walang totoong pondo, profile ng user o hardware signer na ginagamit.

[Dokumentasyon](README.html) · [Interface ng node](EXCHANGE_INTEGRATION.html) · [RPC at HTTP API](RPC_API.html) · [Pagpapatakbo ng node](NETWORK_RUNBOOK.html) · [Beripikasyon](EXCHANGE_EXAMPLES.html)

[Detalyadong sanggunian sa Ingles](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
