# SUMUWW Android 0.7.8 · Belgeler

SUMUWW Android 0.7.8 · Düğüm zincir verilerini doğrular, saklar, iletir ve sorgulamaya açar.

## Ağ ve adresler

Genel ağ `sumuww`, iç takma adı `dora`dır. Aşağıdaki başlangıç bloğu hashini kontrol edin. Yerel adresler witness v0 P2WPKH ve sıkıştırılmış secp256k1 açık anahtarının HASH160 değerini kullanır. Zorunlu memo veya tag yoktur. Yanlış ağ ve geçersiz sağlama toplamını reddedin. HD alma/para üstü dalını ve indeksini kaydedin; Bitcoin türetme yolunu varsaymayın.

## Tutarlar ve kullanılabilir çıktılar

`_units` en küçük birimin tam sayısı, `_smw` 8 ondalıklı metin, `_dora` uyumluluk takma adıdır. `_sumuww` tutar alanı yoktur. 1 SMW = 100000000 birim. `gettxout` içinde `spendable` yoktur; olgunlaşmamış coinbase çıktısı dönebilir. Sonraki blokta harcamak için en az 100 onay gerekir. `listunspent` listesini `spendable` ile süzün; `getaddressbalance` available tutarı olgunlaşmamış ve bekleyen harcamaya bağlı fonları dışlar. Yeni mempool çıktıları onaylı değildir. Sayfalar arasında zincir ucunu kontrol edin ve seçilen girdileri yeniden doğrulayın.

1 SMW = 100.000.000 yugeon. Otomatik ücret, yerel gözlemlere göre üç seçenek sunar; onay süresini garanti etmez. yugeon/vB oranını elle girebilirsiniz. Göndermeden önce son ücreti ve toplamı SMW cinsinden kontrol edin. Reddedilen işlem bakiyeyi azaltmaz.

1 SMW değerinde tek bir girdi kullanıldığında ücret, para üstü gerekip gerekmediğine bağlıdır. Girdi ve tüm çıktılar P2WPKH biçimindeyse ve ücret oranı 1 yugeon/vB ise 0.99999890 SMW gönderirken 110 yugeon ücret ödersiniz ve para üstü kalmaz. Aynı girdiden 0.8 SMW gönderirseniz para üstü için bir çıktı eklenir ve ücret 141 yugeon olur. Ücret düşüldükten sonra kalan tutar, para üstünü ileride harcamanın maliyetini de hesaba katan alt sınıra ulaşırsa cüzdan para üstünü iade eder. Daha küçük bir tutar kalırsa bu tutar, onaydan önce gösterilen ücrete eklenir. Yerel SegWit (P2WPKH) cüzdan girdisinin boyutu hesaplanırken imza için, özet türü dâhil, en fazla 71 bayt ayrılır.

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

Otomatik ücret, bekleyen veri hacmini, blok kapasitesini ve işlem önceliğini dikkate alır. Geçmiş blokların ücretleri kullanılmaz. Kuyruk kısaysa asgari oran korunur. Önizleme yenilenir; son onay ücreti sabitler. Gözlemler tüm düğümleri değil, bağlı yerel düğümü kapsar.

Bu düğümün kaydettiği işlem değiştirme geçmişi, cüzdan yeniden başlatıldığında korunur. Kaldırılan işlemler bakiyeyi etkilemez.

Madencilik geçmişi her bloğun yeni ihracını, işlem ücretlerini ve toplam ödülünü ayrı gösterir. Cüzdanınıza gelen tutar ayrıca gösterilir. Ödül kısmen talep edilmişse iki bileşenin dağılımı varsayılmaz. Düğüm, ücret tahmini dahil 28 RPC yöntemi sunar; imzalı işlemleri doğrular ve iletir.

## İşlem ve blok sorgulama

`getrawtransaction` aktif zincir ve mempool’u arar, yalnızca ayrılmış dallardaki işlemleri aramaz. Girdiler tek bir gönderen adresini değil önceki çıktıları belirtir. `getblock`, Boolean `verbose` alır; kayıtlı pasif bloklarda `active=false`, `confirmations=-1` olur. Ham işlemler blok hashiyle erişilebilir kalır. `findspendingtransaction` yalnızca aktif zincirde onaylanmış harcamaları arar; null kullanılabilirliği kanıtlamaz. `include_mempool=true` ile `gettxout` kontrol edin. Onaylar ve aktif durum yeniden yapılanmada değişebilir.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Ücretler, incelenen işlem ve uyumluluk

Ücret, girdilerin toplamından çıktıların toplamı çıkarılarak bulunur. Tahmine para üstü çıktısı yalnızca cüzdan gerçekten eşik değerini karşılayan bir para üstü oluşturduğunda eklenir. Eşiğin altında kalan tutar ücrete katılır; son ücret ve toplam borçlandırma inceleme için gösterilir. Ücret oranı yugeon/vB cinsindendir. Sanal boyut, işlem ağırlığının dörde bölünüp yukarı yuvarlanmasıyla hesaplanır.

Cüzdan girdileri ve çıktıları bir kez seçer, ardından aynı işlem planını imzalar. Onay verildiğinde saklanan imzalı işlem gönderilir; işlem yeniden kurulmaz ve ücret yeniden hesaplanmaz. Teklifin süresi dolmuşsa veya girdiler bu arada harcanmışsa yeniden inceleme gerekir. Yerel kuyruğa kabul edilmek, bir blokta onaylanmak anlamına gelmez.

Normal P2WPKH ödemelerinde cüzdan, SIGHASH_ALL baytı dahil en fazla 71 baytlık low-R ve low-S imzalar üretir. Bu bir imzalama ve boyut tahmini politikasıdır; diğer geçerli imzalara getirilen yeni bir mutabakat sınırı değildir. Daha kısa bir imza gerçek sanal boyutu azaltabilir. 

## Android imza uyumluluğu

Cüzdan dosya biçimleri, adresler ve mevcut coinler değişmedi. Eski şifrelenmiş cüzdan yedeği yeni uygulamada geri yüklenerek aynı cüzdan kullanılabilir. Android düğümü 0.6.103 ve cüzdan 1.1.14 yeni bir sürüm imzalama anahtarı kullanır. Başka anahtarla imzalanmış bir kurulumun yerine yüklenemezler. Şifrelenmiş cüzdan yedeği ve çalışan bir kurtarma yöntemi edinene kadar eski uygulamayı ve verilerini saklayın. Güncellemeyi zorla yüklemek için eski uygulamayı kaldırmayın.

<!-- /payment-policy-20261116 -->

Düğüm, geçerli bir sürüm yanıtı aldıktan sonra karşı düğüme onay göndermesi için süre tanır. İki giden bağlantı aynı düğüme ulaşıyorsa bunlardan biri eşitlemeyi tamamlayana kadar kullanılabilir bir yol açık kalır.

<!-- poll-recovery-20261119 -->

Dahili bir hatadan sonra eşitleme güncellemesi yeniden denenir. Bir eşte oluşan hata artık diğer eşlerin güncellemelerini durdurmaz. Madencilik için hâlâ yakın zamanda doğrulanmış bir eş gerekir; bağlantının açık kalması tek başına yeterli değildir. Telefonda madencilik başlatıldığında artık hemen durmak yerine eşitlemenin tamamlanması beklenir. Bağlantı kanıtlarının doğrulanması ve geçmişin sorgulanması sırasında ağ işlemlerinin durması düzeltildi. Arka planda madencilik devam eder.
