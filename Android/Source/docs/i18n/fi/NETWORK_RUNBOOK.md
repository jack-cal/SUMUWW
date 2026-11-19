# SUMUWW Android 0.6.103 · Solmun käyttö

Käynnistyessään uudelleen solmu jatkaa viimeisestä paikallisesti tarkistamastaan lohkosta ja tarkistaa uudet lohkot. Jos tallennettu tarkistustieto puuttuu tai on ristiriitainen, solmu tarkistaa tallennetun historian uudelleen.

SUMUWW Android 0.6.103 · Solmu tarkistaa, tallentaa, välittää ja tarjoaa ketjun tiedot.

[Dokumentaatio](../../integration/docs/i18n/fi/NETWORK_RUNBOOK.html)

<!-- payment-policy-20261116 -->

## Maksut, tarkistettu tapahtuma ja yhteensopivuus

Siirtomaksu on syötteiden summa vähennettynä tulosteiden summalla. Arvioon lasketaan vaihtorahatuloste vain, jos lompakko todella luo kynnysarvon täyttävän vaihtorahan. Kynnystä pienempi jäännös lisätään maksuun; lopullinen maksu ja kokonaisveloitus näytetään tarkistettaviksi. Maksutaso ilmoitetaan yksikössä yugeon/vB. Virtuaalikoko saadaan jakamalla tapahtuman paino neljällä ja pyöristämällä ylöspäin.

Lompakko valitsee syötteet ja tulosteet vain kerran ja allekirjoittaa saman tapahtumasuunnitelman. Vahvistettaessa lähetetään tallennettu allekirjoitettu tapahtuma rakentamatta sitä tai laskematta maksua uudelleen. Vanhentunut arvio tai jo käytetyt syötteet edellyttävät uutta tarkistusta. Paikalliseen jonoon hyväksyminen ei tarkoita vahvistusta lohkossa.

Tavallisissa P2WPKH-maksuissa lompakko luo low-R- ja low-S-allekirjoitukset, joiden enimmäispituus on 71 tavua SIGHASH_ALL-tavu mukaan lukien. Tämä on allekirjoitus- ja kokoarviokäytäntö, ei uusi konsensusraja muille kelvollisille allekirjoituksille. Lyhyempi allekirjoitus voi pienentää todellista virtuaalikokoa. 

## Android-allekirjoituksen yhteensopivuus

Lompakon tiedostomuodot, osoitteet ja nykyiset kolikot eivät ole muuttuneet. Aiemman salatun varmuuskopion voi palauttaa uuteen sovellukseen ja jatkaa saman lompakon käyttöä. Android-solmu 0.6.103 ja lompakko 1.1.14 käyttävät uutta julkaisun allekirjoitusavainta. Ne eivät voi korvata eri avaimella allekirjoitettua asennusta. Säilytä vanha sovellus ja sen tiedot, kunnes lompakosta on salattu varmuuskopio ja toimiva palautustapa. Älä poista vanhaa sovellusta vain pakottaaksesi päivityksen asentumaan.

<!-- /payment-policy-20261116 -->

Saatuaan kelvollisen versiotiedon solmu antaa toiselle osapuolelle aikaa lähettää kuittauksen. Jos kaksi lähtevää yhteyttä johtaa samaan solmuun, käytettävissä oleva reitti pidetään auki, kunnes synkronointi on valmis jommankumman yhteyden kautta. 
