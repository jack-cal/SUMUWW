# SUMUWW Wallet Android 1.1.14

Noden öppnar normalt 10 utgående anslutningar. De flesta förmedlar block och transaktioner. En verifierad reservanslutning kan förmedla block, och noden kan tillfälligt öppna en elfte anslutning för att hitta andra noder. Totalt tillåts 125 anslutningar. Högst 117 kan vara inkommande, eller 115 vid 10 utgående. Ett fel vid start av Android-plånboken har rättats. Plånboken känner av när telefonens nätverksanslutning ändras.


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

## Kompatibilitet för Android-signaturer

Plånbokens filformat, adresser och befintliga mynt har inte ändrats. Den tidigare krypterade säkerhetskopian kan återställas i den nya appen för att fortsätta använda samma plånbok. Android-noden 0.6.103 och plånboken 1.1.14 använder en ny nyckel för utgivningssignering. De kan inte ersätta en installation som signerats med en annan nyckel. Behåll den gamla appen och dess data tills du har en krypterad säkerhetskopia av plånboken och en fungerande återställningsmetod. Avinstallera inte den gamla appen bara för att tvinga fram installationen av en uppdatering.

<!-- /payment-policy-20261116 -->

När noden har fått ett giltigt versionssvar får motparten tid att skicka en bekräftelse. Om två utgående anslutningar leder till samma nod hålls en tillgänglig väg öppen tills synkroniseringen är klar via en av dem. Det inbyggda självtestet godtar ett block med giltigt arbetsbevis innan anslutningsbeviset kommer fram. Därefter kontrollerar det de tre vittnenas underskrifter, att beviset vidarebefordras och att det finns kvar efter omstart.
