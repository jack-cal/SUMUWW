# SUMUWW Wallet Android 1.1.9

Düğüm genellikle 10 giden bağlantı açar. Bunların çoğu hem blokları hem de işlemleri iletir. Doğrulanmış bir yedek bağlantı blokları iletebilir. Düğüm başka düğümler bulmak için kısa süreliğine 11. bağlantıyı açabilir. Toplam sınır 125 bağlantıdır. En fazla 117 gelen bağlantı kabul edilir. 10 giden bağlantı varken bu sayı 115’tir.


1 SMW = 100.000.000 yugeon. Otomatik ücret, yerel gözlemlere göre üç seçenek sunar; onay süresini garanti etmez. yugeon/vB oranını elle girebilirsiniz. Göndermeden önce son ücreti ve toplamı SMW cinsinden kontrol edin. Reddedilen işlem bakiyeyi azaltmaz.

`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Otomatik ücret, bekleyen veri hacmini, blok kapasitesini ve işlem önceliğini dikkate alır. Geçmiş blokların ücretleri kullanılmaz. Kuyruk kısaysa asgari oran korunur. Önizleme yenilenir; son onay ücreti sabitler. Gözlemler tüm düğümleri değil, bağlı yerel düğümü kapsar.

Bu düğümün kaydettiği işlem değiştirme geçmişi, cüzdan yeniden başlatıldığında korunur. Kaldırılan işlemler bakiyeyi etkilemez.


Madencilik geçmişi her bloğun yeni ihracını, işlem ücretlerini ve toplam ödülünü ayrı gösterir. Cüzdanınıza gelen tutar ayrıca gösterilir. Ödül kısmen talep edilmişse iki bileşenin dağılımı varsayılmaz. Düğüm, ücret tahmini dahil 28 RPC yöntemi sunar; imzalı işlemleri doğrular ve iletir.
