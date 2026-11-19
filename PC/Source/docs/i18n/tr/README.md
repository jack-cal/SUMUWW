# SUMUWW · Belgeler

1 SMW değerinde tek bir girdi kullanıldığında ücret, para üstü gerekip gerekmediğine bağlıdır. Girdi ve tüm çıktılar P2WPKH biçimindeyse ve ücret oranı 1 yugeon/vB ise 0.99999890 SMW gönderirken 110 yugeon ücret ödersiniz ve para üstü kalmaz. Aynı girdiden 0.8 SMW gönderirseniz para üstü için bir çıktı eklenir ve ücret 141 yugeon olur. Ücret düşüldükten sonra kalan tutar, para üstünü ileride harcamanın maliyetini de hesaba katan alt sınıra ulaşırsa cüzdan para üstünü iade eder. Daha küçük bir tutar kalırsa bu tutar, onaydan önce gösterilen ücrete eklenir. Yerel SegWit (P2WPKH) cüzdan girdisinin boyutu hesaplanırken imza için, özet türü dâhil, en fazla 71 bayt ayrılır.

SUMUWW PC 0.57.51 · Düğüm zincir verilerini doğrular, saklar, iletir ve sorgulamaya açar.

## İmza biçimi

İsteğe bağlı kaynak SDK, anahtar veya ağ olmadan işlem oluşturur ve verilen imzaları doğrular. Bir imzalama programı veya düğüm komutu değildir. P2WPKH ödeme sınırı düğüme değil örnek biçime aittir. Mevcut kişisel cüzdan kullanılabilir.

## RPC ve HTTP API

validateaddress sağlama toplamını ve seçilen ağı denetler. decoderawtransaction için decoded_only yalnızca çözümlemedir. Düğüme ücret sorgusu, gönderim öncesi kontrol, RBF değiştirme durumu ve blok sırasıyla veri okuma eklendi. Bekleyen işlemler silinmeden önce yeni işlem doğrulanır. Çoklu imza ve kilitli çıktılar, yalıtılmış etkinleştirme testleri için uygulandı; genel ağda henüz etkin değildir.

## Doğrulama

Bağımlılıkları yükleyip kaynakta python examples/node_contract.py çalıştırın. Açık test anahtarları ve geçici regtest gönderim, ret, onay, yeniden düzenleme ve veri kalıcılığını sınar. Gerçek para, kullanıcı profili veya donanım imzalayıcı kullanılmaz.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Düğüm arayüzü](EXCHANGE_INTEGRATION.html) · [RPC ve HTTP API](RPC_API.html) · [Düğüm işletimi](NETWORK_RUNBOOK.html) · [Sürüm notları](RELEASE_NOTES.html) · [Doğrulama](EXCHANGE_EXAMPLES.html)

[Ayrıntılı İngilizce kaynak](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Ücretler, incelenen işlem ve uyumluluk

Ücret, girdilerin toplamından çıktıların toplamı çıkarılarak bulunur. Tahmine para üstü çıktısı yalnızca cüzdan gerçekten eşik değerini karşılayan bir para üstü oluşturduğunda eklenir. Eşiğin altında kalan tutar ücrete katılır; son ücret ve toplam borçlandırma inceleme için gösterilir. Ücret oranı yugeon/vB cinsindendir. Sanal boyut, işlem ağırlığının dörde bölünüp yukarı yuvarlanmasıyla hesaplanır.

Cüzdan girdileri ve çıktıları bir kez seçer, ardından aynı işlem planını imzalar. Onay verildiğinde saklanan imzalı işlem gönderilir; işlem yeniden kurulmaz ve ücret yeniden hesaplanmaz. Teklifin süresi dolmuşsa veya girdiler bu arada harcanmışsa yeniden inceleme gerekir. Yerel kuyruğa kabul edilmek, bir blokta onaylanmak anlamına gelmez.

Normal P2WPKH ödemelerinde cüzdan, SIGHASH_ALL baytı dahil en fazla 71 baytlık low-R ve low-S imzalar üretir. Bu bir imzalama ve boyut tahmini politikasıdır; diğer geçerli imzalara getirilen yeni bir mutabakat sınırı değildir. Daha kısa bir imza gerçek sanal boyutu azaltabilir. 

<!-- /payment-policy-20261116 -->
