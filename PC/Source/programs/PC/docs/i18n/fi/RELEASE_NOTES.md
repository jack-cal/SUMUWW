# SUMUWW · Julkaisutiedot

Kun käytät yhtä 1 SMW:n arvoista syötettä, maksu riippuu siitä, palautuuko lompakkoon vaihtorahaa. Jos syöte ja kaikki tulosteet ovat tyyppiä P2WPKH ja maksutaso on 1 yugeon/vB, 0.99999890 SMW:n lähettäminen maksaa 110 yugeon eikä vaihtorahaa jää. Jos lähetät samasta syötteestä 0.8 SMW, vaihtorahaa varten tarvitaan yksi tuloste lisää ja maksu on 141 yugeon. Lompakko palauttaa vaihtorahan, jos maksun vähentämisen jälkeen jäljelle jäävä summa saavuttaa vähimmäisrajan. Rajassa huomioidaan vaihtorahan myöhemmän käytön kustannus. Pienempi jäännös sisältyy ennen vahvistusta näytettävään maksuun. Natiivia SegWitiä (P2WPKH) käyttävän lompakon syötteen kokoarviossa allekirjoitukselle varataan enintään 71 tavua tiivistetyyppi mukaan lukien.

0.57.61 · Kun vaihdat kieltä sovelluksen ollessa käynnissä, myös Windowsin tehtäväpalkin kuvake vaihtuu.

Solmu avaa tavallisesti 10 lähtevää yhteyttä. Useimmat välittävät lohkoja ja tapahtumia. Solmu voi käyttää varmennettua varayhteyttä lohkojen välitykseen ja avata hetkeksi yhdennentoista yhteyden muiden solmujen etsintään. Yhteyksiä voi olla yhteensä 125. Saapuvia yhteyksiä voi olla enintään 117 tai 10 lähtevän yhteyden kanssa enintään 115. Työpöytäsovellus näyttää nyt vain yhdistettyjen solmujen kokonaismäärän. Jokainen louhija muodostaa omat lohkonsa. PC-solmu välittää valmiit lohkot ja hylkää puhelimen louhintatyöpyynnöt ja ratkaisut.

Käynnistyessään uudelleen solmu jatkaa viimeisestä paikallisesti tarkistamastaan lohkosta ja tarkistaa uudet lohkot. Jos tallennettu tarkistustieto puuttuu tai on ristiriitainen, solmu tarkistaa tallennetun historian uudelleen.

SUMUWW PC 0.57.61 · Solmu tarkistaa, tallentaa, välittää ja tarjoaa ketjun tiedot.

## Allekirjoitusmuoto

Valinnainen lähdekoodin SDK kokoaa transaktiot ja tarkistaa toimitetut allekirjoitukset ilman avaimia tai verkkoa. Se ei ole allekirjoitusohjelma eikä solmun komento. P2WPKH-rajoitus koskee esimerkin muotoa, ei solmua. Henkilökohtainen lompakko säilyy käytössä.

## RPC- ja HTTP-API

validateaddress tarkistaa tarkistussumman ja valitun verkon. decoderawtransaction palauttaa decoded_only, ei todistusta allekirjoituksen kelpoisuudesta tai vahvistuksesta. OP_RETURN säilyttää tietoa ulkoisille ohjelmille. Solmuun lisätään maksukyselyt, tarkistus ennen lähetystä, RBF-korvauksen tila ja tietojen luku lohkojärjestyksessä. Korvaava tapahtuma tarkistetaan ennen odottavien tapahtumien poistamista. Moniallekirjoitus ja lukitut ulostulot on toteutettu erillisiä aktivointitestejä varten; ne eivät vielä ole käytössä julkisessa verkossa.

## Varmennus

Asenna riippuvuudet ja suorita lähdekoodista python examples/node_contract.py. Julkiset testiavaimet ja tilapäinen regtest testaavat lähetyksen, hylkäyksen, vahvistukset, uudelleenjärjestelyn ja tietojen säilymisen. Oikeita varoja, käyttäjäprofiileja tai laitteistoallekirjoittajia ei käytetä.

[Dokumentaatio](README.html) · [Solmun rajapinta](EXCHANGE_INTEGRATION.html) · [RPC- ja HTTP-API](RPC_API.html) · [Solmun käyttö](NETWORK_RUNBOOK.html) · [Varmennus](EXCHANGE_EXAMPLES.html)

[Laaja englanninkielinen viite](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Maksut, tarkistettu tapahtuma ja yhteensopivuus

Siirtomaksu on syötteiden summa vähennettynä tulosteiden summalla. Arvioon lasketaan vaihtorahatuloste vain, jos lompakko todella luo kynnysarvon täyttävän vaihtorahan. Kynnystä pienempi jäännös lisätään maksuun; lopullinen maksu ja kokonaisveloitus näytetään tarkistettaviksi. Maksutaso ilmoitetaan yksikössä yugeon/vB. Virtuaalikoko saadaan jakamalla tapahtuman paino neljällä ja pyöristämällä ylöspäin.

Lompakko valitsee syötteet ja tulosteet vain kerran ja allekirjoittaa saman tapahtumasuunnitelman. Vahvistettaessa lähetetään tallennettu allekirjoitettu tapahtuma rakentamatta sitä tai laskematta maksua uudelleen. Vanhentunut arvio tai jo käytetyt syötteet edellyttävät uutta tarkistusta. Paikalliseen jonoon hyväksyminen ei tarkoita vahvistusta lohkossa.

Tavallisissa P2WPKH-maksuissa lompakko luo low-R- ja low-S-allekirjoitukset, joiden enimmäispituus on 71 tavua SIGHASH_ALL-tavu mukaan lukien. Tämä on allekirjoitus- ja kokoarviokäytäntö, ei uusi konsensusraja muille kelvollisille allekirjoituksille. Lyhyempi allekirjoitus voi pienentää todellista virtuaalikokoa. 

<!-- /payment-policy-20261116 -->
