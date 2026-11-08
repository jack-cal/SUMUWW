# SUMUWW · Julkaisutiedot

Solmu avaa tavallisesti 10 lähtevää yhteyttä. Useimmat välittävät lohkoja ja tapahtumia. Solmu voi käyttää varmennettua varayhteyttä lohkojen välitykseen ja avata hetkeksi yhdennentoista yhteyden muiden solmujen etsintään. Yhteyksiä voi olla yhteensä 125. Saapuvia yhteyksiä voi olla enintään 117 tai 10 lähtevän yhteyden kanssa enintään 115. Työpöytäsovellus näyttää nyt vain yhdistettyjen solmujen kokonaismäärän. Jokainen louhija muodostaa omat lohkonsa. PC-solmu välittää valmiit lohkot ja hylkää puhelimen louhintatyöpyynnöt ja ratkaisut.


SUMUWW PC 0.57.53 · Solmu tarkistaa, tallentaa, välittää ja tarjoaa ketjun tiedot.

## Allekirjoitusmuoto

Valinnainen lähdekoodin SDK kokoaa transaktiot ja tarkistaa toimitetut allekirjoitukset ilman avaimia tai verkkoa. Se ei ole allekirjoitusohjelma eikä solmun komento. P2WPKH-rajoitus koskee esimerkin muotoa, ei solmua. Henkilökohtainen lompakko säilyy käytössä.

## RPC- ja HTTP-API

validateaddress tarkistaa tarkistussumman ja valitun verkon. decoderawtransaction palauttaa decoded_only, ei todistusta allekirjoituksen kelpoisuudesta tai vahvistuksesta. OP_RETURN säilyttää tietoa ulkoisille ohjelmille. Solmuun lisätään maksukyselyt, tarkistus ennen lähetystä, RBF-korvauksen tila ja tietojen luku lohkojärjestyksessä. Korvaava tapahtuma tarkistetaan ennen odottavien tapahtumien poistamista. Moniallekirjoitus ja lukitut ulostulot on toteutettu erillisiä aktivointitestejä varten; ne eivät vielä ole käytössä julkisessa verkossa.

## Varmennus

Asenna riippuvuudet ja suorita lähdekoodista python examples/node_contract.py. Julkiset testiavaimet ja tilapäinen regtest testaavat lähetyksen, hylkäyksen, vahvistukset, uudelleenjärjestelyn ja tietojen säilymisen. Oikeita varoja, käyttäjäprofiileja tai laitteistoallekirjoittajia ei käytetä.

[Dokumentaatio](README.html) · [Solmun rajapinta](EXCHANGE_INTEGRATION.html) · [RPC- ja HTTP-API](RPC_API.html) · [Solmun käyttö](NETWORK_RUNBOOK.html) · [Varmennus](EXCHANGE_EXAMPLES.html)

[Laaja englanninkielinen viite](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
