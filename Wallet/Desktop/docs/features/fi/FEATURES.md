# SUMUWW Wallet PC 1.0.15

Solmu avaa tavallisesti 10 lähtevää yhteyttä. Useimmat välittävät lohkoja ja tapahtumia. Solmu voi käyttää varmennettua varayhteyttä lohkojen välitykseen ja avata hetkeksi yhdennentoista yhteyden muiden solmujen etsintään. Yhteyksiä voi olla yhteensä 125. Saapuvia yhteyksiä voi olla enintään 117 tai 10 lähtevän yhteyden kanssa enintään 115.

1 SMW = 100 000 000 yugeon. Automaattinen maksu tarjoaa kolme tasoa paikallisten havaintojen perusteella, mutta ei takaa vahvistusaikaa. Voit syöttää maksutason yksikössä yugeon/vB. Tarkista lopullinen maksu ja kokonaissumma SMW-yksikössä ennen lähettämistä. Hylätty tapahtuma ei vähennä saldoa.

Kun käytät yhtä 1 SMW:n arvoista syötettä, maksu riippuu siitä, palautuuko lompakkoon vaihtorahaa. Jos syöte ja kaikki tulosteet ovat tyyppiä P2WPKH ja maksutaso on 1 yugeon/vB, 0.99999890 SMW:n lähettäminen maksaa 110 yugeon eikä vaihtorahaa jää. Jos lähetät samasta syötteestä 0.8 SMW, vaihtorahaa varten tarvitaan yksi tuloste lisää ja maksu on 141 yugeon. Lompakko palauttaa vaihtorahan, jos maksun vähentämisen jälkeen jäljelle jäävä summa saavuttaa vähimmäisrajan. Rajassa huomioidaan vaihtorahan myöhemmän käytön kustannus. Pienempi jäännös sisältyy ennen vahvistusta näytettävään maksuun. Natiivia SegWitiä (P2WPKH) käyttävän lompakon syötteen kokoarviossa allekirjoitukselle varataan enintään 71 tavua tiivistetyyppi mukaan lukien.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Automaattinen maksu perustuu jonossa olevaan datamäärään, lohkokapasiteettiin ja siirtojen etusijaan. Aiempien lohkojen maksuja ei käytetä. Lyhyessä jonossa käytetään vähimmäishintaa. Esikatselu päivittyy; lopullinen vahvistus lukitsee maksun. Havainnot koskevat yhdistettyä paikallista solmua, eivät kaikkia solmuja.

Tämän solmun kirjaama korvaushistoria säilyy lompakon uudelleenkäynnistyksen jälkeen. Poistetut tapahtumat eivät vaikuta saldoon.

Louhintahistoria erittelee kunkin lohkon uuden liikkeeseenlaskun, siirtomaksut ja kokonaispalkkion. Lompakkosi vastaanottama summa näkyy erikseen. Osittain lunastetun palkkion jakautumista ei oleteta. Solmu tarjoaa 28 RPC-menetelmää, mukaan lukien maksuarvion, sekä tarkistaa ja välittää allekirjoitetut tapahtumat.

<!-- payment-policy-20261116 -->

## Maksut, tarkistettu tapahtuma ja yhteensopivuus

Siirtomaksu on syötteiden summa vähennettynä tulosteiden summalla. Arvioon lasketaan vaihtorahatuloste vain, jos lompakko todella luo kynnysarvon täyttävän vaihtorahan. Kynnystä pienempi jäännös lisätään maksuun; lopullinen maksu ja kokonaisveloitus näytetään tarkistettaviksi. Maksutaso ilmoitetaan yksikössä yugeon/vB. Virtuaalikoko saadaan jakamalla tapahtuman paino neljällä ja pyöristämällä ylöspäin.

Lompakko valitsee syötteet ja tulosteet vain kerran ja allekirjoittaa saman tapahtumasuunnitelman. Vahvistettaessa lähetetään tallennettu allekirjoitettu tapahtuma rakentamatta sitä tai laskematta maksua uudelleen. Vanhentunut arvio tai jo käytetyt syötteet edellyttävät uutta tarkistusta. Paikalliseen jonoon hyväksyminen ei tarkoita vahvistusta lohkossa.

Tavallisissa P2WPKH-maksuissa lompakko luo low-R- ja low-S-allekirjoitukset, joiden enimmäispituus on 71 tavua SIGHASH_ALL-tavu mukaan lukien. Tämä on allekirjoitus- ja kokoarviokäytäntö, ei uusi konsensusraja muille kelvollisille allekirjoituksille. Lyhyempi allekirjoitus voi pienentää todellista virtuaalikokoa. 

<!-- /payment-policy-20261116 -->

Saatuaan kelvollisen versiotiedon solmu antaa toiselle osapuolelle aikaa lähettää kuittauksen. Jos kaksi lähtevää yhteyttä johtaa samaan solmuun, käytettävissä oleva reitti pidetään auki, kunnes synkronointi on valmis jommankumman yhteyden kautta. 
