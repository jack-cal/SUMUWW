# SUMUWW Android 0.6.98 · Mga tala ng bersyon

Kumokonekta ang telepono sa isang SUMUWW full node na may bersyong 0.57.49 o mas bago. Sinusuri nito ang gantimpala at kinakalkula ang proof of work nang hindi dina-download ang buong kasaysayan ng mga transaksyon.

Inilalarawan ng API specification ang nakapaloob na node core. Walang screen ng RPC configuration ang Android app.

## RPC at HTTP API

Sinusuri ng validateaddress ang checksum at napiling network. Ang decoded_only mula sa decoderawtransaction ay pagbasa lang ng datos, hindi patunay ng wastong lagda o kumpirmasyon. Nag-iimbak ang OP_RETURN ng datos para sa panlabas na programa. May dagdag na pagtatanong ng bayad, pagsusuri bago magpadala, katayuan ng pagpapalit sa RBF at datos ayon sa pagkakasunod ng mga block. Sinusuri muna ang kapalit bago alisin ang mga nakabinbing transaksiyon. Naipatupad ang maramihang lagda at naka-lock na output para sa hiwalay na pagsubok; hindi pa aktibo sa pampublikong network.

[API_CONTRACT.json](../../../API_CONTRACT.json)
