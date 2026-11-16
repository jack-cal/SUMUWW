# SUMUWW Wallet PC 1.0.15

Noden öppnar normalt 10 utgående anslutningar. De flesta förmedlar block och transaktioner. En verifierad reservanslutning kan förmedla block, och noden kan tillfälligt öppna en elfte anslutning för att hitta andra noder. Totalt tillåts 125 anslutningar. Högst 117 kan vara inkommande, eller 115 vid 10 utgående.


1 SMW = 100 000 000 yugeon. Automatiska avgifter erbjuder tre nivåer utifrån lokala observationer, utan att garantera bekräftelsetiden. Du kan ange en sats i yugeon/vB. Kontrollera den slutliga avgiften och totalsumman i SMW innan du skickar. En avvisad transaktion minskar inte saldot.

Med en ingång på 1 SMW beror avgiften på om du ska få växel tillbaka. Om ingången och alla utgångar är av typen P2WPKH och avgiftssatsen är 1 yugeon/vB kostar det 110 yugeon att skicka 0.99999890 SMW. Då blir det ingen växel. Skickar du 0.8 SMW från samma ingång tillkommer en utgång för växeln och avgiften blir 141 yugeon. Plånboken ger växel tillbaka om beloppet som återstår efter avgiften når en gräns som tar hänsyn till kostnaden för att använda växeln senare. Ett mindre restbelopp ingår i avgiften som visas före bekräftelsen. För en indata från en plånbok med inbyggt SegWit-stöd (P2WPKH) räknar uppskattningen med högst 71 byte för signaturen, inklusive hashtypen.


`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Automatiska avgifter utgår från väntande datamängd, blockkapacitet och transaktionsprioritet. Avgifter i tidigare block används inte. Vid kort kö gäller minimiavgiften. Förhandsvisningen uppdateras; den slutliga bekräftelsen låser avgiften. Uppgifterna gäller den anslutna lokala noden, inte alla noder.

Ersättningar som denna nod har registrerat finns kvar i historiken efter omstart av plånboken. Borttagna transaktioner påverkar inte saldot.


Utvinningshistoriken visar ny utgivning, avgifter och total belöning för varje block var för sig. Beloppet din plånbok tar emot visas separat. Vid delvis uttag antas ingen fördelning mellan delarna. Noden erbjuder 28 RPC-metoder, inklusive avgiftsuppskattning, och kontrollerar och vidarebefordrar signerade transaktioner.

<!-- payment-policy-20261116 -->

## Avgifter, granskad transaktion och kompatibilitet

Avgiften är summan av ingångarna minus summan av utgångarna. Uppskattningen räknar bara med en växelutgång när plånboken faktiskt skapar tillräcklig växel. Ett restbelopp under plånbokens gräns läggs till avgiften; den slutliga avgiften och hela debiteringen visas för granskning. Avgiftssatsen anges i yugeon/vB. Virtuell storlek är transaktionens vikt delad med fyra, avrundad uppåt.

Plånboken väljer ingångar och utgångar en gång och signerar samma transaktionsplan. Vid bekräftelse skickas den sparade signerade transaktionen utan att byggas om eller få avgiften omräknad. Ett utgånget förslag eller redan förbrukade ingångar kräver en ny granskning. Att tas emot i den lokala kön betyder inte att transaktionen är bekräftad i ett block.

För vanliga P2WPKH-betalningar skapar plånboken low-R- och low-S-signaturer på högst 71 byte, inklusive SIGHASH_ALL-byten. Det är en policy för signering och storleksuppskattning, inte en ny konsensusgräns för andra giltiga signaturer. En kortare signatur kan minska den verkliga virtuella storleken. Föreslagna satser grundas fortfarande på den lokala kön; en storleksberäkning som liknar Bitcoins innebär inte att Bitcoin-nätverkets avgiftssatser används.

## Windows I2P-komponent och säkerhetskontroll

Windows-paketen innehåller officiella i2pd 3.0.0 med uppdaterade kontrollsummor och certifikat för första anslutningen. I den dokumenterade kontrollen upptäcker Defender fortfarande den officiella I2P-programfilen och den ursprungliga ZIP-filen som hot. En matchande officiell hash bevisar varken säkerhet eller en falsk varning. Ett lokalt filundantag gäller bara på datorn där det har lagts till; det offentliga paketet lägger inte till det. Andra datorer kan blockera samma filer.

<!-- /payment-policy-20261116 -->

När noden har fått ett giltigt versionssvar får motparten tid att skicka en bekräftelse. Om två utgående anslutningar leder till samma nod hålls en tillgänglig väg öppen tills synkroniseringen är klar via en av dem. Det inbyggda självtestet godtar ett block med giltigt arbetsbevis innan anslutningsbeviset kommer fram. Därefter kontrollerar det de tre vittnenas underskrifter, att beviset vidarebefordras och att det finns kvar efter omstart.
