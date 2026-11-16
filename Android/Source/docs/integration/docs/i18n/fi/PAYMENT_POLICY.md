# Maksut, tarkistettu tapahtuma ja yhteensopivuus

SUMUWW · 2026-11-16

<!-- payment-policy-20261116 -->

## Maksut, tarkistettu tapahtuma ja yhteensopivuus

Siirtomaksu on syötteiden summa vähennettynä tulosteiden summalla. Arvioon lasketaan vaihtorahatuloste vain, jos lompakko todella luo kynnysarvon täyttävän vaihtorahan. Kynnystä pienempi jäännös lisätään maksuun; lopullinen maksu ja kokonaisveloitus näytetään tarkistettaviksi. Maksutaso ilmoitetaan yksikössä yugeon/vB. Virtuaalikoko saadaan jakamalla tapahtuman paino neljällä ja pyöristämällä ylöspäin.

Lompakko valitsee syötteet ja tulosteet vain kerran ja allekirjoittaa saman tapahtumasuunnitelman. Vahvistettaessa lähetetään tallennettu allekirjoitettu tapahtuma rakentamatta sitä tai laskematta maksua uudelleen. Vanhentunut arvio tai jo käytetyt syötteet edellyttävät uutta tarkistusta. Paikalliseen jonoon hyväksyminen ei tarkoita vahvistusta lohkossa.

Tavallisissa P2WPKH-maksuissa lompakko luo low-R- ja low-S-allekirjoitukset, joiden enimmäispituus on 71 tavua SIGHASH_ALL-tavu mukaan lukien. Tämä on allekirjoitus- ja kokoarviokäytäntö, ei uusi konsensusraja muille kelvollisille allekirjoituksille. Lyhyempi allekirjoitus voi pienentää todellista virtuaalikokoa. Suositellut maksutasot perustuvat edelleen paikalliseen jonoon; Bitcoinin kaltainen kokolaskenta ei tarkoita Bitcoin-verkon maksutasojen käyttöä.

## Windowsin I2P-osa ja tietoturvatarkistus

Windows-paketeissa on virallinen i2pd 3.0.0 sekä päivitetyt tarkistussummat ja alkuyhteyden varmenteet. Tallennetussa tarkistuksessa Defender tunnistaa edelleen virallisen I2P-ohjelmatiedoston ja alkuperäisen ZIP-paketin uhkiksi. Virallisen tiivisteen täsmääminen ei osoita turvallisuutta eikä vahvista väärää hälytystä. Paikallinen tiedostopoikkeus koskee vain tietokonetta, jossa se on määritetty; julkinen paketti ei lisää sitä. Muut tietokoneet voivat estää samat tiedostot.

## Android-allekirjoituksen yhteensopivuus

Lompakon tiedostomuodot, osoitteet ja nykyiset kolikot eivät ole muuttuneet. Aiemman salatun varmuuskopion voi palauttaa uuteen sovellukseen ja jatkaa saman lompakon käyttöä. Android-solmu 0.6.103 ja lompakko 1.1.14 käyttävät uutta julkaisun allekirjoitusavainta. Ne eivät voi korvata eri avaimella allekirjoitettua asennusta. Säilytä vanha sovellus ja sen tiedot, kunnes lompakosta on salattu varmuuskopio ja toimiva palautustapa. Älä poista vanhaa sovellusta vain pakottaaksesi päivityksen asentumaan.

<!-- /payment-policy-20261116 -->

Saatuaan kelvollisen versiotiedon solmu antaa toiselle osapuolelle aikaa lähettää kuittauksen. Jos kaksi lähtevää yhteyttä johtaa samaan solmuun, käytettävissä oleva reitti pidetään auki, kunnes synkronointi on valmis jommankumman yhteyden kautta. Sisäinen testi hyväksyy kelvollisen työtodisteen sisältävän lohkon ennen yhteystodisteen saapumista. Sen jälkeen testi tarkistaa kolmen todistajan allekirjoitukset, yhteystodisteen välityksen ja sen säilymisen uudelleenkäynnistyksen jälkeen.
