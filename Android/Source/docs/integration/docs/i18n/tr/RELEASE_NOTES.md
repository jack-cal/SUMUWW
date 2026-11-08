# SUMUWW Android 0.6.99 · Sürüm notları

Düğüm yeniden başlatıldığında yerel olarak doğruladığı son bloktan devam eder ve yeni blokları doğrular. Kayıtlı doğrulama bilgisi eksikse veya tutarsızsa saklanan geçmişi yeniden denetler.

SUMUWW Android 0.6.99 · Düğüm zincir verilerini doğrular, saklar, iletir ve sorgulamaya açar.

API belirtimi gömülü düğüm çekirdeğini açıklar. Android uygulamasında RPC yapılandırma ekranı yoktur.

## RPC ve HTTP API

validateaddress sağlama toplamını ve seçilen ağı denetler. decoderawtransaction için decoded_only yalnızca çözümlemedir. Düğüme ücret sorgusu, gönderim öncesi kontrol, RBF değiştirme durumu ve blok sırasıyla veri okuma eklendi. Bekleyen işlemler silinmeden önce yeni işlem doğrulanır. Çoklu imza ve kilitli çıktılar, yalıtılmış etkinleştirme testleri için uygulandı; genel ağda henüz etkin değildir.

[API_CONTRACT.json](../../../API_CONTRACT.json)
