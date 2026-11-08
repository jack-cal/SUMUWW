# SUMUWW Android 0.6.98 · Sürüm notları

Telefon, 0.57.49 veya sonraki bir sürümü çalıştıran bir SUMUWW tam düğümüne bağlanır. Ödülü kontrol eder ve tüm işlem geçmişini indirmeden iş ispatını hesaplar.

API belirtimi gömülü düğüm çekirdeğini açıklar. Android uygulamasında RPC yapılandırma ekranı yoktur.

## RPC ve HTTP API

validateaddress sağlama toplamını ve seçilen ağı denetler. decoderawtransaction için decoded_only yalnızca çözümlemedir. Düğüme ücret sorgusu, gönderim öncesi kontrol, RBF değiştirme durumu ve blok sırasıyla veri okuma eklendi. Bekleyen işlemler silinmeden önce yeni işlem doğrulanır. Çoklu imza ve kilitli çıktılar, yalıtılmış etkinleştirme testleri için uygulandı; genel ağda henüz etkin değildir.

[API_CONTRACT.json](../../../API_CONTRACT.json)
