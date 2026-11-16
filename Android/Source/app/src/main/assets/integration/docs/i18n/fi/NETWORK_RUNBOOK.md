# SUMUWW Android 0.6.103 · Solmun käyttö

Käynnistyessään uudelleen solmu jatkaa viimeisestä paikallisesti tarkistamastaan lohkosta ja tarkistaa uudet lohkot. Jos tallennettu tarkistustieto puuttuu tai on ristiriitainen, solmu tarkistaa tallennetun historian uudelleen.

SUMUWW Android 0.6.103 · Solmu tarkistaa, tallentaa, välittää ja tarjoaa ketjun tiedot.

## Verkko ja osoitteet

Julkinen verkko on `sumuww`, sisäinen alias `dora`. Tarkista alla oleva genesis-tiiviste. Osoitteet käyttävät witness v0 P2WPKH:ta ja pakatun secp256k1-julkisen avaimen HASH160:tä. Memoa tai tagia ei vaadita. Hylkää väärän verkon osoitteet ja virheelliset tarkistussummat. Tallenna HD-vastaanotto-/vaihtorahahaara ja indeksi; älä oleta Bitcoinin johtamispolkua.

## Tapahtumien ja lohkojen haku

`getrawtransaction` hakee aktiivisesta ketjusta ja mempoolista, ei vain hylätyistä haaroista. Syötteet viittaavat aiempiin tulosteisiin, eivät yksiselitteiseen lähettäjäosoitteeseen. `getblock` ottaa totuusarvon `verbose`; tallennetun epäaktiivisen lohkon arvot ovat `active=false`, `confirmations=-1`. Raakatapahtumat saa edelleen lohkotiivisteellä. `findspendingtransaction` hakee vain aktiivisen ketjun vahvistetut käytöt; null ei todista käytettävyyttä. Tarkista `gettxout` asetuksella `include_mempool=true`. Vahvistukset ja aktiivisuus voivat muuttua uudelleenjärjestelyssä.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Maksut, tarkistettu tapahtuma ja yhteensopivuus

Siirtomaksu on syötteiden summa vähennettynä tulosteiden summalla. Arvioon lasketaan vaihtorahatuloste vain, jos lompakko todella luo kynnysarvon täyttävän vaihtorahan. Kynnystä pienempi jäännös lisätään maksuun; lopullinen maksu ja kokonaisveloitus näytetään tarkistettaviksi. Maksutaso ilmoitetaan yksikössä yugeon/vB. Virtuaalikoko saadaan jakamalla tapahtuman paino neljällä ja pyöristämällä ylöspäin.

Lompakko valitsee syötteet ja tulosteet vain kerran ja allekirjoittaa saman tapahtumasuunnitelman. Vahvistettaessa lähetetään tallennettu allekirjoitettu tapahtuma rakentamatta sitä tai laskematta maksua uudelleen. Vanhentunut arvio tai jo käytetyt syötteet edellyttävät uutta tarkistusta. Paikalliseen jonoon hyväksyminen ei tarkoita vahvistusta lohkossa.

Tavallisissa P2WPKH-maksuissa lompakko luo low-R- ja low-S-allekirjoitukset, joiden enimmäispituus on 71 tavua SIGHASH_ALL-tavu mukaan lukien. Tämä on allekirjoitus- ja kokoarviokäytäntö, ei uusi konsensusraja muille kelvollisille allekirjoituksille. Lyhyempi allekirjoitus voi pienentää todellista virtuaalikokoa. Suositellut maksutasot perustuvat edelleen paikalliseen jonoon; Bitcoinin kaltainen kokolaskenta ei tarkoita Bitcoin-verkon maksutasojen käyttöä.

## Android-allekirjoituksen yhteensopivuus

Lompakon tiedostomuodot, osoitteet ja nykyiset kolikot eivät ole muuttuneet. Aiemman salatun varmuuskopion voi palauttaa uuteen sovellukseen ja jatkaa saman lompakon käyttöä. Android-solmu 0.6.103 ja lompakko 1.1.14 käyttävät uutta julkaisun allekirjoitusavainta. Ne eivät voi korvata eri avaimella allekirjoitettua asennusta. Säilytä vanha sovellus ja sen tiedot, kunnes lompakosta on salattu varmuuskopio ja toimiva palautustapa. Älä poista vanhaa sovellusta vain pakottaaksesi päivityksen asentumaan.

<!-- /payment-policy-20261116 -->

Saatuaan kelvollisen versiotiedon solmu antaa toiselle osapuolelle aikaa lähettää kuittauksen. Jos kaksi lähtevää yhteyttä johtaa samaan solmuun, käytettävissä oleva reitti pidetään auki, kunnes synkronointi on valmis jommankumman yhteyden kautta. Sisäinen testi hyväksyy kelvollisen työtodisteen sisältävän lohkon ennen yhteystodisteen saapumista. Sen jälkeen testi tarkistaa kolmen todistajan allekirjoitukset, yhteystodisteen välityksen ja sen säilymisen uudelleenkäynnistyksen jälkeen.
