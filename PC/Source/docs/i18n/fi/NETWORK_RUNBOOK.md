# SUMUWW · Solmun käyttö

Solmu avaa tavallisesti 10 lähtevää yhteyttä. Useimmat välittävät lohkoja ja tapahtumia. Solmu voi käyttää varmennettua varayhteyttä lohkojen välitykseen ja avata hetkeksi yhdennentoista yhteyden muiden solmujen etsintään. Yhteyksiä voi olla yhteensä 125. Saapuvia yhteyksiä voi olla enintään 117 tai 10 lähtevän yhteyden kanssa enintään 115. Työpöytäsovellus näyttää nyt vain yhdistettyjen solmujen kokonaismäärän. Jokainen louhija muodostaa omat lohkonsa. PC-solmu välittää valmiit lohkot ja hylkää puhelimen louhintatyöpyynnöt ja ratkaisut.

Käynnistyessään uudelleen solmu jatkaa viimeisestä paikallisesti tarkistamastaan lohkosta ja tarkistaa uudet lohkot. Jos tallennettu tarkistustieto puuttuu tai on ristiriitainen, solmu tarkistaa tallennetun historian uudelleen.


SUMUWW PC 0.57.61 · Solmu tarkistaa, tallentaa, välittää ja tarjoaa ketjun tiedot.

## Verkko ja osoitteet

Julkinen verkko on `sumuww`, sisäinen alias `dora`. Tarkista alla oleva genesis-tiiviste. Osoitteet käyttävät witness v0 P2WPKH:ta ja pakatun secp256k1-julkisen avaimen HASH160:tä. Memoa tai tagia ei vaadita. Hylkää väärän verkon osoitteet ja virheelliset tarkistussummat. Tallenna HD-vastaanotto-/vaihtorahahaara ja indeksi; älä oleta Bitcoinin johtamispolkua.

## Todennus ja rajat

Ota RPC erikseen käyttöön numeerisessa loopback-osoitteessa `127.0.0.1:18443` yksityisellä Bearer-tunnisteella. Lompakon avaamista tai etäallekirjoitusta ei tarjota. Käytä paikallista palvelua tai todennettua tunnelia; selaimen Origin/Referer-pyynnöt hylätään. JSON-RPC käyttää POST `/rpc`, olio-/taulukko-`params` ja `id`; ilmoitukset palauttavat HTTP 204. Rajat: runko 8004096 tavua, otsakkeet 8192, erä 16, samanaikaiset pyynnöt 16, määräaika 10 sekuntia; limit 1–1000, offset 0–1000000. Menetelmiä on 28 ja REST-reittejä 11.

## Tapahtumien ja lohkojen haku

`getrawtransaction` hakee aktiivisesta ketjusta ja mempoolista, ei vain hylätyistä haaroista. Syötteet viittaavat aiempiin tulosteisiin, eivät yksiselitteiseen lähettäjäosoitteeseen. `getblock` ottaa totuusarvon `verbose`; tallennetun epäaktiivisen lohkon arvot ovat `active=false`, `confirmations=-1`. Raakatapahtumat saa edelleen lohkotiivisteellä. `findspendingtransaction` hakee vain aktiivisen ketjun vahvistetut käytöt; null ei todista käytettävyyttä. Tarkista `gettxout` asetuksella `include_mempool=true`. Vahvistukset ja aktiivisuus voivat muuttua uudelleenjärjestelyssä.

## Varmennus

Asenna riippuvuudet ja suorita lähdekoodista python examples/node_contract.py. Julkiset testiavaimet ja tilapäinen regtest testaavat lähetyksen, hylkäyksen, vahvistukset, uudelleenjärjestelyn ja tietojen säilymisen. Oikeita varoja, käyttäjäprofiileja tai laitteistoallekirjoittajia ei käytetä.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Dokumentaatio](README.html) · [Solmun rajapinta](EXCHANGE_INTEGRATION.html) · [RPC- ja HTTP-API](RPC_API.html) · [Julkaisutiedot](RELEASE_NOTES.html) · [Varmennus](EXCHANGE_EXAMPLES.html)

[Laaja englanninkielinen viite](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Maksut, tarkistettu tapahtuma ja yhteensopivuus

Siirtomaksu on syötteiden summa vähennettynä tulosteiden summalla. Arvioon lasketaan vaihtorahatuloste vain, jos lompakko todella luo kynnysarvon täyttävän vaihtorahan. Kynnystä pienempi jäännös lisätään maksuun; lopullinen maksu ja kokonaisveloitus näytetään tarkistettaviksi. Maksutaso ilmoitetaan yksikössä yugeon/vB. Virtuaalikoko saadaan jakamalla tapahtuman paino neljällä ja pyöristämällä ylöspäin.

Lompakko valitsee syötteet ja tulosteet vain kerran ja allekirjoittaa saman tapahtumasuunnitelman. Vahvistettaessa lähetetään tallennettu allekirjoitettu tapahtuma rakentamatta sitä tai laskematta maksua uudelleen. Vanhentunut arvio tai jo käytetyt syötteet edellyttävät uutta tarkistusta. Paikalliseen jonoon hyväksyminen ei tarkoita vahvistusta lohkossa.

Tavallisissa P2WPKH-maksuissa lompakko luo low-R- ja low-S-allekirjoitukset, joiden enimmäispituus on 71 tavua SIGHASH_ALL-tavu mukaan lukien. Tämä on allekirjoitus- ja kokoarviokäytäntö, ei uusi konsensusraja muille kelvollisille allekirjoituksille. Lyhyempi allekirjoitus voi pienentää todellista virtuaalikokoa. Suositellut maksutasot perustuvat edelleen paikalliseen jonoon; Bitcoinin kaltainen kokolaskenta ei tarkoita Bitcoin-verkon maksutasojen käyttöä.

## Windowsin I2P-osa ja tietoturvatarkistus

Windows-paketeissa on virallinen i2pd 3.0.0 sekä päivitetyt tarkistussummat ja alkuyhteyden varmenteet. Tallennetussa tarkistuksessa Defender tunnistaa edelleen virallisen I2P-ohjelmatiedoston ja alkuperäisen ZIP-paketin uhkiksi. Virallisen tiivisteen täsmääminen ei osoita turvallisuutta eikä vahvista väärää hälytystä. Paikallinen tiedostopoikkeus koskee vain tietokonetta, jossa se on määritetty; julkinen paketti ei lisää sitä. Muut tietokoneet voivat estää samat tiedostot.

<!-- /payment-policy-20261116 -->

Saatuaan kelvollisen versiotiedon solmu antaa toiselle osapuolelle aikaa lähettää kuittauksen. Jos kaksi lähtevää yhteyttä johtaa samaan solmuun, käytettävissä oleva reitti pidetään auki, kunnes synkronointi on valmis jommankumman yhteyden kautta. Sisäinen testi hyväksyy kelvollisen työtodisteen sisältävän lohkon ennen yhteystodisteen saapumista. Sen jälkeen testi tarkistaa kolmen todistajan allekirjoitukset, yhteystodisteen välityksen ja sen säilymisen uudelleenkäynnistyksen jälkeen.
