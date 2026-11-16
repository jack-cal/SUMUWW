# SUMUWW Android 0.6.103 · Dokumentaatio

Kun käytät yhtä 1 SMW:n arvoista syötettä, maksu riippuu siitä, palautuuko lompakkoon vaihtorahaa. Jos syöte ja kaikki tulosteet ovat tyyppiä P2WPKH ja maksutaso on 1 yugeon/vB, 0.99999890 SMW:n lähettäminen maksaa 110 yugeon eikä vaihtorahaa jää. Jos lähetät samasta syötteestä 0.8 SMW, vaihtorahaa varten tarvitaan yksi tuloste lisää ja maksu on 141 yugeon. Lompakko palauttaa vaihtorahan, jos maksun vähentämisen jälkeen jäljelle jäävä summa saavuttaa vähimmäisrajan. Rajassa huomioidaan vaihtorahan myöhemmän käytön kustannus. Pienempi jäännös sisältyy ennen vahvistusta näytettävään maksuun. Natiivia SegWitiä (P2WPKH) käyttävän lompakon syötteen kokoarviossa allekirjoitukselle varataan enintään 71 tavua tiivistetyyppi mukaan lukien.


SUMUWW Android 0.6.103 · Solmu tarkistaa, tallentaa, välittää ja tarjoaa ketjun tiedot.

[Dokumentaatio](../../integration/docs/i18n/fi/ANDROID.html)

<!-- payment-policy-20261116 -->

## Maksut, tarkistettu tapahtuma ja yhteensopivuus

Siirtomaksu on syötteiden summa vähennettynä tulosteiden summalla. Arvioon lasketaan vaihtorahatuloste vain, jos lompakko todella luo kynnysarvon täyttävän vaihtorahan. Kynnystä pienempi jäännös lisätään maksuun; lopullinen maksu ja kokonaisveloitus näytetään tarkistettaviksi. Maksutaso ilmoitetaan yksikössä yugeon/vB. Virtuaalikoko saadaan jakamalla tapahtuman paino neljällä ja pyöristämällä ylöspäin.

Lompakko valitsee syötteet ja tulosteet vain kerran ja allekirjoittaa saman tapahtumasuunnitelman. Vahvistettaessa lähetetään tallennettu allekirjoitettu tapahtuma rakentamatta sitä tai laskematta maksua uudelleen. Vanhentunut arvio tai jo käytetyt syötteet edellyttävät uutta tarkistusta. Paikalliseen jonoon hyväksyminen ei tarkoita vahvistusta lohkossa.

Tavallisissa P2WPKH-maksuissa lompakko luo low-R- ja low-S-allekirjoitukset, joiden enimmäispituus on 71 tavua SIGHASH_ALL-tavu mukaan lukien. Tämä on allekirjoitus- ja kokoarviokäytäntö, ei uusi konsensusraja muille kelvollisille allekirjoituksille. Lyhyempi allekirjoitus voi pienentää todellista virtuaalikokoa. Suositellut maksutasot perustuvat edelleen paikalliseen jonoon; Bitcoinin kaltainen kokolaskenta ei tarkoita Bitcoin-verkon maksutasojen käyttöä.

## Android-allekirjoituksen yhteensopivuus

Lompakon tiedostomuodot, osoitteet ja nykyiset kolikot eivät ole muuttuneet. Aiemman salatun varmuuskopion voi palauttaa uuteen sovellukseen ja jatkaa saman lompakon käyttöä. Android-solmu 0.6.103 ja lompakko 1.1.14 käyttävät uutta julkaisun allekirjoitusavainta. Ne eivät voi korvata eri avaimella allekirjoitettua asennusta. Säilytä vanha sovellus ja sen tiedot, kunnes lompakosta on salattu varmuuskopio ja toimiva palautustapa. Älä poista vanhaa sovellusta vain pakottaaksesi päivityksen asentumaan.

<!-- /payment-policy-20261116 -->

Saatuaan kelvollisen versiotiedon solmu antaa toiselle osapuolelle aikaa lähettää kuittauksen. Jos kaksi lähtevää yhteyttä johtaa samaan solmuun, käytettävissä oleva reitti pidetään auki, kunnes synkronointi on valmis jommankumman yhteyden kautta. Sisäinen testi hyväksyy kelvollisen työtodisteen sisältävän lohkon ennen yhteystodisteen saapumista. Sen jälkeen testi tarkistaa kolmen todistajan allekirjoitukset, yhteystodisteen välityksen ja sen säilymisen uudelleenkäynnistyksen jälkeen.
