# SUMUWW Android 0.6.103 · Belgeler

SUMUWW Android 0.6.103 · Düğüm zincir verilerini doğrular, saklar, iletir ve sorgulamaya açar.

[Belgeler](../../integration/docs/i18n/tr/README.html)

<!-- payment-policy-20261116 -->

## Ücretler, incelenen işlem ve uyumluluk

Ücret, girdilerin toplamından çıktıların toplamı çıkarılarak bulunur. Tahmine para üstü çıktısı yalnızca cüzdan gerçekten eşik değerini karşılayan bir para üstü oluşturduğunda eklenir. Eşiğin altında kalan tutar ücrete katılır; son ücret ve toplam borçlandırma inceleme için gösterilir. Ücret oranı yugeon/vB cinsindendir. Sanal boyut, işlem ağırlığının dörde bölünüp yukarı yuvarlanmasıyla hesaplanır.

Cüzdan girdileri ve çıktıları bir kez seçer, ardından aynı işlem planını imzalar. Onay verildiğinde saklanan imzalı işlem gönderilir; işlem yeniden kurulmaz ve ücret yeniden hesaplanmaz. Teklifin süresi dolmuşsa veya girdiler bu arada harcanmışsa yeniden inceleme gerekir. Yerel kuyruğa kabul edilmek, bir blokta onaylanmak anlamına gelmez.

Normal P2WPKH ödemelerinde cüzdan, SIGHASH_ALL baytı dahil en fazla 71 baytlık low-R ve low-S imzalar üretir. Bu bir imzalama ve boyut tahmini politikasıdır; diğer geçerli imzalara getirilen yeni bir mutabakat sınırı değildir. Daha kısa bir imza gerçek sanal boyutu azaltabilir. Önerilen oranlar hâlâ yerel kuyruğa dayanır; Bitcoin’e benzer boyut hesabı kullanılması Bitcoin ağının ücret oranlarının kullanıldığı anlamına gelmez.

## Android imza uyumluluğu

Cüzdan dosya biçimleri, adresler ve mevcut coinler değişmedi. Eski şifrelenmiş cüzdan yedeği yeni uygulamada geri yüklenerek aynı cüzdan kullanılabilir. Android düğümü 0.6.103 ve cüzdan 1.1.14 yeni bir sürüm imzalama anahtarı kullanır. Başka anahtarla imzalanmış bir kurulumun yerine yüklenemezler. Şifrelenmiş cüzdan yedeği ve çalışan bir kurtarma yöntemi edinene kadar eski uygulamayı ve verilerini saklayın. Güncellemeyi zorla yüklemek için eski uygulamayı kaldırmayın.

<!-- /payment-policy-20261116 -->
