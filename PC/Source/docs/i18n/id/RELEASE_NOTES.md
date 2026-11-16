# SUMUWW · Catatan versi

Dengan satu input senilai 1 SMW, biaya bergantung pada ada tidaknya kembalian. Jika input dan semua output berjenis P2WPKH dengan tarif 1 yugeon/vB, pengiriman 0.99999890 SMW dikenai biaya 110 yugeon tanpa kembalian. Pengiriman 0.8 SMW dari input yang sama menambahkan satu output untuk kembalian sehingga biayanya menjadi 141 yugeon. Dompet mengembalikan sisa dana jika jumlah yang tersisa setelah biaya mencapai batas minimum. Batas ini memperhitungkan biaya untuk membelanjakan dana tersebut nanti. Jika jumlahnya lebih kecil, sisanya masuk dalam biaya yang ditampilkan sebelum konfirmasi. Untuk input dompet SegWit asli (P2WPKH), perkiraan ukuran memperhitungkan hingga 71 byte untuk tanda tangan, termasuk jenis hash.


0.57.61 · Saat Anda mengganti bahasa ketika aplikasi berjalan, ikon di bilah tugas Windows juga berubah.

Node biasanya membuka 10 koneksi keluar. Sebagian besar meneruskan blok dan transaksi. Node dapat menggunakan koneksi cadangan yang telah diverifikasi untuk meneruskan blok dan membuka koneksi ke-11 sebentar untuk mencari node lain. Batas totalnya 125 koneksi. Maksimal ada 117 koneksi masuk, atau 115 jika ada 10 koneksi keluar. Aplikasi desktop kini hanya menampilkan jumlah total simpul yang terhubung. Setiap penambang menyusun bloknya sendiri. Node PC meneruskan blok yang sudah selesai dan menolak permintaan pekerjaan penambangan serta solusi dari ponsel.

Saat dimulai ulang, node melanjutkan dari blok terakhir yang sudah diverifikasi secara lokal dan memeriksa blok baru. Jika catatan verifikasi yang tersimpan hilang atau tidak cocok, node memeriksa kembali riwayat yang tersimpan.


SUMUWW PC 0.57.61 · Node memvalidasi, menyimpan, meneruskan, dan menyediakan data rantai.

## Format tanda tangan

SDK sumber opsional menyusun transaksi dan memverifikasi tanda tangan yang diberikan tanpa kunci atau jaringan. Ini bukan penanda tangan atau perintah node. Batas pembayaran P2WPKH berlaku pada format contoh, bukan node. Dompet pribadi yang ada tetap tersedia.

## API RPC dan HTTP

validateaddress memeriksa checksum dan jaringan pilihan. decoded_only dari decoderawtransaction hanya berarti penguraian, bukan keabsahan tanda tangan atau konfirmasi. Output OP_RETURN menyimpan data bagi program eksternal. Node menyediakan kueri biaya, pemeriksaan sebelum pengiriman, status penggantian RBF, dan data sesuai urutan blok. Pengganti divalidasi sebelum transaksi tertunda dihapus. Multitanda tangan dan keluaran terkunci telah diterapkan untuk pengujian aktivasi terpisah; belum aktif di jaringan publik.

## Verifikasi

Pasang dependensi lalu jalankan python examples/node_contract.py dari sumber. Kunci uji publik dan regtest sementara menguji pengiriman, penolakan, konfirmasi, reorganisasi, dan persistensi. Tidak ada dana nyata, profil pengguna, atau penanda tangan perangkat keras yang digunakan.

[Dokumentasi](README.html) · [Antarmuka node](EXCHANGE_INTEGRATION.html) · [API RPC dan HTTP](RPC_API.html) · [Operasi node](NETWORK_RUNBOOK.html) · [Verifikasi](EXCHANGE_EXAMPLES.html)

[Referensi lengkap bahasa Inggris](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Biaya, transaksi yang ditinjau, dan kompatibilitas

Biaya adalah jumlah nilai input dikurangi jumlah nilai output. Perkiraan hanya menghitung output kembalian jika dompet benar-benar membuat kembalian yang memenuhi ambangnya. Sisa di bawah ambang tersebut ditambahkan ke biaya; biaya akhir dan total saldo yang dipotong ditampilkan untuk diperiksa. Tarif dinyatakan dalam yugeon/vB. Ukuran virtual adalah bobot transaksi dibagi empat, lalu dibulatkan ke atas.

Dompet memilih input dan output sekali saja, lalu menandatangani rencana transaksi yang sama. Saat dikonfirmasi, transaksi bertanda tangan yang tersimpan dikirim tanpa disusun ulang atau dihitung ulang biayanya. Perkiraan yang kedaluwarsa atau input yang sudah dibelanjakan memerlukan peninjauan baru. Diterima dalam antrean lokal bukan berarti sudah dikonfirmasi di dalam blok.

Untuk pembayaran P2WPKH biasa, dompet menghasilkan tanda tangan low-R dan low-S berukuran paling besar 71 bita, termasuk bita SIGHASH_ALL. Ini adalah kebijakan penandatanganan dan perkiraan ukuran, bukan batas konsensus baru bagi tanda tangan sah lainnya. Tanda tangan yang lebih pendek dapat memperkecil ukuran virtual sebenarnya. Saran tarif tetap memakai antrean lokal; mengikuti perhitungan ukuran Bitcoin tidak berarti memakai tarif jaringan Bitcoin.

## Komponen I2P Windows dan pemeriksaan keamanan

Paket Windows menyertakan i2pd 3.0.0 resmi dengan hash dan sertifikat koneksi awal yang diperbarui. Dalam pemeriksaan yang dicatat, Defender masih mendeteksi berkas I2P dan ZIP resmi tersebut. Kecocokan hash dengan sumber resmi tidak membuktikan keamanan atau memastikan deteksi keliru. Pengecualian berkas lokal hanya berlaku di komputer tempat pengecualian itu didaftarkan; paket publik tidak memasangnya. Komputer lain masih dapat memblokir berkas yang sama.

<!-- /payment-policy-20261116 -->
