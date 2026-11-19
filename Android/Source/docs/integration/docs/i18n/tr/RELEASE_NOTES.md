# SUMUWW Android 0.6.103 · Sürüm notları

1 SMW değerinde tek bir girdi kullanıldığında ücret, para üstü gerekip gerekmediğine bağlıdır. Girdi ve tüm çıktılar P2WPKH biçimindeyse ve ücret oranı 1 yugeon/vB ise 0.99999890 SMW gönderirken 110 yugeon ücret ödersiniz ve para üstü kalmaz. Aynı girdiden 0.8 SMW gönderirseniz para üstü için bir çıktı eklenir ve ücret 141 yugeon olur. Ücret düşüldükten sonra kalan tutar, para üstünü ileride harcamanın maliyetini de hesaba katan alt sınıra ulaşırsa cüzdan para üstünü iade eder. Daha küçük bir tutar kalırsa bu tutar, onaydan önce gösterilen ücrete eklenir. Yerel SegWit (P2WPKH) cüzdan girdisinin boyutu hesaplanırken imza için, özet türü dâhil, en fazla 71 bayt ayrılır.

Düğüm yeniden başlatıldığında yerel olarak doğruladığı son bloktan devam eder ve yeni blokları doğrular. Kayıtlı doğrulama bilgisi eksikse veya tutarsızsa saklanan geçmişi yeniden denetler.

SUMUWW Android 0.6.103 · Düğüm zincir verilerini doğrular, saklar, iletir ve sorgulamaya açar.

API belirtimi gömülü düğüm çekirdeğini açıklar. Android uygulamasında RPC yapılandırma ekranı yoktur.

## RPC ve HTTP API

validateaddress sağlama toplamını ve seçilen ağı denetler. decoderawtransaction için decoded_only yalnızca çözümlemedir. Düğüme ücret sorgusu, gönderim öncesi kontrol, RBF değiştirme durumu ve blok sırasıyla veri okuma eklendi. Bekleyen işlemler silinmeden önce yeni işlem doğrulanır. Çoklu imza ve kilitli çıktılar, yalıtılmış etkinleştirme testleri için uygulandı; genel ağda henüz etkin değildir.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Ücretler, incelenen işlem ve uyumluluk

Ücret, girdilerin toplamından çıktıların toplamı çıkarılarak bulunur. Tahmine para üstü çıktısı yalnızca cüzdan gerçekten eşik değerini karşılayan bir para üstü oluşturduğunda eklenir. Eşiğin altında kalan tutar ücrete katılır; son ücret ve toplam borçlandırma inceleme için gösterilir. Ücret oranı yugeon/vB cinsindendir. Sanal boyut, işlem ağırlığının dörde bölünüp yukarı yuvarlanmasıyla hesaplanır.

Cüzdan girdileri ve çıktıları bir kez seçer, ardından aynı işlem planını imzalar. Onay verildiğinde saklanan imzalı işlem gönderilir; işlem yeniden kurulmaz ve ücret yeniden hesaplanmaz. Teklifin süresi dolmuşsa veya girdiler bu arada harcanmışsa yeniden inceleme gerekir. Yerel kuyruğa kabul edilmek, bir blokta onaylanmak anlamına gelmez.

Normal P2WPKH ödemelerinde cüzdan, SIGHASH_ALL baytı dahil en fazla 71 baytlık low-R ve low-S imzalar üretir. Bu bir imzalama ve boyut tahmini politikasıdır; diğer geçerli imzalara getirilen yeni bir mutabakat sınırı değildir. Daha kısa bir imza gerçek sanal boyutu azaltabilir. 

## Android imza uyumluluğu

Cüzdan dosya biçimleri, adresler ve mevcut coinler değişmedi. Eski şifrelenmiş cüzdan yedeği yeni uygulamada geri yüklenerek aynı cüzdan kullanılabilir. Android düğümü 0.6.103 ve cüzdan 1.1.14 yeni bir sürüm imzalama anahtarı kullanır. Başka anahtarla imzalanmış bir kurulumun yerine yüklenemezler. Şifrelenmiş cüzdan yedeği ve çalışan bir kurtarma yöntemi edinene kadar eski uygulamayı ve verilerini saklayın. Güncellemeyi zorla yüklemek için eski uygulamayı kaldırmayın.

<!-- /payment-policy-20261116 -->
