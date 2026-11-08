# SUMUWW Android 0.6.98 · Pagpapatakbo ng node

Kumokonekta ang telepono sa isang SUMUWW full node na may bersyong 0.57.49 o mas bago. Sinusuri nito ang gantimpala at kinakalkula ang proof of work nang hindi dina-download ang buong kasaysayan ng mga transaksyon.

## Network at mga address

Ang pampublikong network ay `sumuww`, na may panloob na alyas na `dora`. Suriin ang genesis hash sa ibaba. Gumagamit ang katutubong address ng witness v0 P2WPKH at HASH160 ng compressed secp256k1 public key. Walang kailangang memo o tag. Tanggihan ang maling network at di-wastong checksum. Itala ang HD branch para sa pagtanggap/sukli at index; huwag ipalagay ang derivation path ng Bitcoin.

## Paghahanap ng transaksyon at block

Hinahanap ng `getrawtransaction` ang active chain at mempool, hindi ang transaksyong nasa naulilang sangay lamang. Tumutukoy ang input sa dating output, hindi sa iisang sender address. Boolean ang `verbose` ng `getblock`; ang naka-save na inactive block ay may `active=false`, `confirmations=-1`. Maa-access pa rin ang raw transaction sa block hash. Confirmed active spend lamang ang hinahanap ng `findspendingtransaction`; hindi patunay ng availability ang null. Suriin ang `gettxout` na may `include_mempool=true`. Maaaring magbago ang kumpirmasyon at active status sa reorganisasyon.

[API_CONTRACT.json](../../../API_CONTRACT.json)
