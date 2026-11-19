# SUMUWW · Dokumentaatio

SUMUWW PC 0.57.51 · Solmu tarkistaa, tallentaa, välittää ja tarjoaa ketjun tiedot.

## Allekirjoitusmuoto

Valinnainen lähdekoodin SDK kokoaa transaktiot ja tarkistaa toimitetut allekirjoitukset ilman avaimia tai verkkoa. Se ei ole allekirjoitusohjelma eikä solmun komento. P2WPKH-rajoitus koskee esimerkin muotoa, ei solmua. Henkilökohtainen lompakko säilyy käytössä.

## RPC- ja HTTP-API

validateaddress tarkistaa tarkistussumman ja valitun verkon. decoderawtransaction palauttaa decoded_only, ei todistusta allekirjoituksen kelpoisuudesta tai vahvistuksesta. OP_RETURN säilyttää tietoa ulkoisille ohjelmille. Solmuun lisätään maksukyselyt, tarkistus ennen lähetystä, RBF-korvauksen tila ja tietojen luku lohkojärjestyksessä. Korvaava tapahtuma tarkistetaan ennen odottavien tapahtumien poistamista. Moniallekirjoitus ja lukitut ulostulot on toteutettu erillisiä aktivointitestejä varten; ne eivät vielä ole käytössä julkisessa verkossa.

## Varmennus

Asenna riippuvuudet ja suorita lähdekoodista python examples/node_contract.py. Julkiset testiavaimet ja tilapäinen regtest testaavat lähetyksen, hylkäyksen, vahvistukset, uudelleenjärjestelyn ja tietojen säilymisen. Oikeita varoja, käyttäjäprofiileja tai laitteistoallekirjoittajia ei käytetä.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Solmun rajapinta](EXCHANGE_INTEGRATION.html) · [RPC- ja HTTP-API](RPC_API.html) · [Solmun käyttö](NETWORK_RUNBOOK.html) · [Julkaisutiedot](RELEASE_NOTES.html) · [Varmennus](EXCHANGE_EXAMPLES.html)

[Laaja englanninkielinen viite](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Maksut, tarkistettu tapahtuma ja yhteensopivuus

Siirtomaksu on syötteiden summa vähennettynä tulosteiden summalla. Arvioon lasketaan vaihtorahatuloste vain, jos lompakko todella luo kynnysarvon täyttävän vaihtorahan. Kynnystä pienempi jäännös lisätään maksuun; lopullinen maksu ja kokonaisveloitus näytetään tarkistettaviksi. Maksutaso ilmoitetaan yksikössä yugeon/vB. Virtuaalikoko saadaan jakamalla tapahtuman paino neljällä ja pyöristämällä ylöspäin.

Lompakko valitsee syötteet ja tulosteet vain kerran ja allekirjoittaa saman tapahtumasuunnitelman. Vahvistettaessa lähetetään tallennettu allekirjoitettu tapahtuma rakentamatta sitä tai laskematta maksua uudelleen. Vanhentunut arvio tai jo käytetyt syötteet edellyttävät uutta tarkistusta. Paikalliseen jonoon hyväksyminen ei tarkoita vahvistusta lohkossa.

Tavallisissa P2WPKH-maksuissa lompakko luo low-R- ja low-S-allekirjoitukset, joiden enimmäispituus on 71 tavua SIGHASH_ALL-tavu mukaan lukien. Tämä on allekirjoitus- ja kokoarviokäytäntö, ei uusi konsensusraja muille kelvollisille allekirjoituksille. Lyhyempi allekirjoitus voi pienentää todellista virtuaalikokoa. 

<!-- /payment-policy-20261116 -->
