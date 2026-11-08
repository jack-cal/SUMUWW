# SUMUWW Android 0.6.98 · Solmun käyttö

Puhelin muodostaa yhteyden SUMUWW-täyssolmuun, jonka versio on 0.57.49 tai uudempi. Se tarkistaa palkkion ja laskee työtodisteen lataamatta ketjun koko tapahtumahistoriaa.

## Verkko ja osoitteet

Julkinen verkko on `sumuww`, sisäinen alias `dora`. Tarkista alla oleva genesis-tiiviste. Osoitteet käyttävät witness v0 P2WPKH:ta ja pakatun secp256k1-julkisen avaimen HASH160:tä. Memoa tai tagia ei vaadita. Hylkää väärän verkon osoitteet ja virheelliset tarkistussummat. Tallenna HD-vastaanotto-/vaihtorahahaara ja indeksi; älä oleta Bitcoinin johtamispolkua.

## Tapahtumien ja lohkojen haku

`getrawtransaction` hakee aktiivisesta ketjusta ja mempoolista, ei vain hylätyistä haaroista. Syötteet viittaavat aiempiin tulosteisiin, eivät yksiselitteiseen lähettäjäosoitteeseen. `getblock` ottaa totuusarvon `verbose`; tallennetun epäaktiivisen lohkon arvot ovat `active=false`, `confirmations=-1`. Raakatapahtumat saa edelleen lohkotiivisteellä. `findspendingtransaction` hakee vain aktiivisen ketjun vahvistetut käytöt; null ei todista käytettävyyttä. Tarkista `gettxout` asetuksella `include_mempool=true`. Vahvistukset ja aktiivisuus voivat muuttua uudelleenjärjestelyssä.

[API_CONTRACT.json](../../../API_CONTRACT.json)
