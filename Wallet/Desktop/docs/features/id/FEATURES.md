# SUMUWW Wallet PC 1.0.15

Node biasanya membuka 10 koneksi keluar. Sebagian besar meneruskan blok dan transaksi. Node dapat menggunakan koneksi cadangan yang telah diverifikasi untuk meneruskan blok dan membuka koneksi ke-11 sebentar untuk mencari node lain. Batas totalnya 125 koneksi. Maksimal ada 117 koneksi masuk, atau 115 jika ada 10 koneksi keluar.


1 SMW = 100.000.000 yugeon. Biaya otomatis menawarkan tiga tingkat berdasarkan pengamatan lokal, tanpa menjamin waktu konfirmasi. Anda dapat memasukkan tarif yugeon/vB secara manual. Periksa biaya akhir dan total dalam SMW sebelum mengirim. Transaksi yang ditolak tidak mengurangi saldo.

Dengan satu input senilai 1 SMW, biaya bergantung pada ada tidaknya kembalian. Jika input dan semua output berjenis P2WPKH dengan tarif 1 yugeon/vB, pengiriman 0.99999890 SMW dikenai biaya 110 yugeon tanpa kembalian. Pengiriman 0.8 SMW dari input yang sama menambahkan satu output untuk kembalian sehingga biayanya menjadi 141 yugeon. Dompet mengembalikan sisa dana jika jumlah yang tersisa setelah biaya mencapai batas minimum. Batas ini memperhitungkan biaya untuk membelanjakan dana tersebut nanti. Jika jumlahnya lebih kecil, sisanya masuk dalam biaya yang ditampilkan sebelum konfirmasi. Untuk input dompet SegWit asli (P2WPKH), perkiraan ukuran memperhitungkan hingga 71 byte untuk tanda tangan, termasuk jenis hash.


`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Biaya otomatis mempertimbangkan volume data tertunda, kapasitas blok, dan prioritas transaksi. Biaya blok lama tidak digunakan. Saat antrean pendek, tarif minimum dipertahankan. Pratinjau diperbarui; konfirmasi akhir menetapkan biaya. Pengamatan mencakup node lokal yang terhubung, bukan semua node.

Riwayat penggantian yang dicatat node ini tetap tersimpan setelah dompet dimulai ulang. Transaksi yang dihapus tidak memengaruhi saldo.


Riwayat penambangan memisahkan penerbitan baru, biaya transaksi, dan total imbalan setiap blok. Jumlah yang diterima dompet Anda ditampilkan terpisah. Klaim sebagian tidak menentukan pembagian kedua komponen. Node menyediakan 28 metode RPC, termasuk perkiraan biaya, serta memvalidasi dan meneruskan transaksi bertanda tangan.

<!-- payment-policy-20261116 -->

## Biaya, transaksi yang ditinjau, dan kompatibilitas

Biaya adalah jumlah nilai input dikurangi jumlah nilai output. Perkiraan hanya menghitung output kembalian jika dompet benar-benar membuat kembalian yang memenuhi ambangnya. Sisa di bawah ambang tersebut ditambahkan ke biaya; biaya akhir dan total saldo yang dipotong ditampilkan untuk diperiksa. Tarif dinyatakan dalam yugeon/vB. Ukuran virtual adalah bobot transaksi dibagi empat, lalu dibulatkan ke atas.

Dompet memilih input dan output sekali saja, lalu menandatangani rencana transaksi yang sama. Saat dikonfirmasi, transaksi bertanda tangan yang tersimpan dikirim tanpa disusun ulang atau dihitung ulang biayanya. Perkiraan yang kedaluwarsa atau input yang sudah dibelanjakan memerlukan peninjauan baru. Diterima dalam antrean lokal bukan berarti sudah dikonfirmasi di dalam blok.

Untuk pembayaran P2WPKH biasa, dompet menghasilkan tanda tangan low-R dan low-S berukuran paling besar 71 bita, termasuk bita SIGHASH_ALL. Ini adalah kebijakan penandatanganan dan perkiraan ukuran, bukan batas konsensus baru bagi tanda tangan sah lainnya. Tanda tangan yang lebih pendek dapat memperkecil ukuran virtual sebenarnya. Saran tarif tetap memakai antrean lokal; mengikuti perhitungan ukuran Bitcoin tidak berarti memakai tarif jaringan Bitcoin.

## Komponen I2P Windows dan pemeriksaan keamanan

Paket Windows menyertakan i2pd 3.0.0 resmi dengan hash dan sertifikat koneksi awal yang diperbarui. Dalam pemeriksaan yang dicatat, Defender masih mendeteksi berkas I2P dan ZIP resmi tersebut. Kecocokan hash dengan sumber resmi tidak membuktikan keamanan atau memastikan deteksi keliru. Pengecualian berkas lokal hanya berlaku di komputer tempat pengecualian itu didaftarkan; paket publik tidak memasangnya. Komputer lain masih dapat memblokir berkas yang sama.

<!-- /payment-policy-20261116 -->

Setelah menerima respons versi yang sah, simpul memberi simpul lain waktu untuk mengirim konfirmasi. Jika dua koneksi keluar menuju simpul yang sama, jalur yang tersedia tetap terbuka sampai salah satunya selesai disinkronkan. Diagnostik bawaan menerima blok dengan bukti kerja yang sah sebelum bukti koneksi tersedia. Kemudian, diagnostik memeriksa tanda tangan tiga saksi, penerusan bukti koneksi, dan apakah bukti itu tetap tersimpan setelah mulai ulang.
