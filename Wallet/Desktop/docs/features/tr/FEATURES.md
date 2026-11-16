# SUMUWW Wallet PC 1.0.15

Düğüm genellikle 10 giden bağlantı açar. Bunların çoğu hem blokları hem de işlemleri iletir. Doğrulanmış bir yedek bağlantı blokları iletebilir. Düğüm başka düğümler bulmak için kısa süreliğine 11. bağlantıyı açabilir. Toplam sınır 125 bağlantıdır. En fazla 117 gelen bağlantı kabul edilir. 10 giden bağlantı varken bu sayı 115’tir.


1 SMW = 100.000.000 yugeon. Otomatik ücret, yerel gözlemlere göre üç seçenek sunar; onay süresini garanti etmez. yugeon/vB oranını elle girebilirsiniz. Göndermeden önce son ücreti ve toplamı SMW cinsinden kontrol edin. Reddedilen işlem bakiyeyi azaltmaz.

1 SMW değerinde tek bir girdi kullanıldığında ücret, para üstü gerekip gerekmediğine bağlıdır. Girdi ve tüm çıktılar P2WPKH biçimindeyse ve ücret oranı 1 yugeon/vB ise 0.99999890 SMW gönderirken 110 yugeon ücret ödersiniz ve para üstü kalmaz. Aynı girdiden 0.8 SMW gönderirseniz para üstü için bir çıktı eklenir ve ücret 141 yugeon olur. Ücret düşüldükten sonra kalan tutar, para üstünü ileride harcamanın maliyetini de hesaba katan alt sınıra ulaşırsa cüzdan para üstünü iade eder. Daha küçük bir tutar kalırsa bu tutar, onaydan önce gösterilen ücrete eklenir. Yerel SegWit (P2WPKH) cüzdan girdisinin boyutu hesaplanırken imza için, özet türü dâhil, en fazla 71 bayt ayrılır.


`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Otomatik ücret, bekleyen veri hacmini, blok kapasitesini ve işlem önceliğini dikkate alır. Geçmiş blokların ücretleri kullanılmaz. Kuyruk kısaysa asgari oran korunur. Önizleme yenilenir; son onay ücreti sabitler. Gözlemler tüm düğümleri değil, bağlı yerel düğümü kapsar.

Bu düğümün kaydettiği işlem değiştirme geçmişi, cüzdan yeniden başlatıldığında korunur. Kaldırılan işlemler bakiyeyi etkilemez.


Madencilik geçmişi her bloğun yeni ihracını, işlem ücretlerini ve toplam ödülünü ayrı gösterir. Cüzdanınıza gelen tutar ayrıca gösterilir. Ödül kısmen talep edilmişse iki bileşenin dağılımı varsayılmaz. Düğüm, ücret tahmini dahil 28 RPC yöntemi sunar; imzalı işlemleri doğrular ve iletir.

<!-- payment-policy-20261116 -->

## Ücretler, incelenen işlem ve uyumluluk

Ücret, girdilerin toplamından çıktıların toplamı çıkarılarak bulunur. Tahmine para üstü çıktısı yalnızca cüzdan gerçekten eşik değerini karşılayan bir para üstü oluşturduğunda eklenir. Eşiğin altında kalan tutar ücrete katılır; son ücret ve toplam borçlandırma inceleme için gösterilir. Ücret oranı yugeon/vB cinsindendir. Sanal boyut, işlem ağırlığının dörde bölünüp yukarı yuvarlanmasıyla hesaplanır.

Cüzdan girdileri ve çıktıları bir kez seçer, ardından aynı işlem planını imzalar. Onay verildiğinde saklanan imzalı işlem gönderilir; işlem yeniden kurulmaz ve ücret yeniden hesaplanmaz. Teklifin süresi dolmuşsa veya girdiler bu arada harcanmışsa yeniden inceleme gerekir. Yerel kuyruğa kabul edilmek, bir blokta onaylanmak anlamına gelmez.

Normal P2WPKH ödemelerinde cüzdan, SIGHASH_ALL baytı dahil en fazla 71 baytlık low-R ve low-S imzalar üretir. Bu bir imzalama ve boyut tahmini politikasıdır; diğer geçerli imzalara getirilen yeni bir mutabakat sınırı değildir. Daha kısa bir imza gerçek sanal boyutu azaltabilir. Önerilen oranlar hâlâ yerel kuyruğa dayanır; Bitcoin’e benzer boyut hesabı kullanılması Bitcoin ağının ücret oranlarının kullanıldığı anlamına gelmez.

## Windows I2P bileşeni ve güvenlik denetimleri

Windows paketleri, güncel özet değerleri ve ilk bağlantı sertifikalarıyla birlikte resmî i2pd 3.0.0 sürümünü içerir. Kaydedilen denetimde Defender, resmî I2P yürütülebilir dosyasını ve kaynak ZIP’i hâlâ algılamaktadır. Resmî özetin eşleşmesi, güvenliği veya yanlış algılamayı kanıtlamaz. Yerel dosya istisnası yalnızca kaydedildiği bilgisayarda geçerlidir; genel dağıtım paketi bu istisnayı eklemez. Başka bilgisayarlar aynı dosyaları engelleyebilir.

<!-- /payment-policy-20261116 -->

Düğüm, geçerli bir sürüm yanıtı aldıktan sonra karşı düğüme onay göndermesi için süre tanır. İki giden bağlantı aynı düğüme ulaşıyorsa bunlardan biri eşitlemeyi tamamlayana kadar kullanılabilir bir yol açık kalır. Yerleşik tanılama, bağlantı kanıtı gelmeden önce geçerli iş kanıtı taşıyan bir bloğu kabul eder. Ardından üç tanığın imzasını, bağlantı kanıtının diğer düğümlere iletilmesini ve yeniden başlatmadan sonra korunmasını denetler.
