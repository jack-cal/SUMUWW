# SUMUWW · Operasi node

Node biasanya membuka 10 koneksi keluar. Sebagian besar meneruskan blok dan transaksi. Node dapat menggunakan koneksi cadangan yang telah diverifikasi untuk meneruskan blok dan membuka koneksi ke-11 sebentar untuk mencari node lain. Batas totalnya 125 koneksi. Maksimal ada 117 koneksi masuk, atau 115 jika ada 10 koneksi keluar. Aplikasi desktop kini hanya menampilkan jumlah total simpul yang terhubung. Setiap penambang menyusun bloknya sendiri. Node PC meneruskan blok yang sudah selesai dan menolak permintaan pekerjaan penambangan serta solusi dari ponsel.

Saat dimulai ulang, node melanjutkan dari blok terakhir yang sudah diverifikasi secara lokal dan memeriksa blok baru. Jika catatan verifikasi yang tersimpan hilang atau tidak cocok, node memeriksa kembali riwayat yang tersimpan.


SUMUWW PC 0.57.61 · Node memvalidasi, menyimpan, meneruskan, dan menyediakan data rantai.

## Jaringan dan alamat

Jaringan publik adalah `sumuww`, dengan alias internal `dora`. Periksa hash genesis di bawah. Alamat asli memakai witness v0 P2WPKH dan HASH160 kunci publik secp256k1 terkompresi. Memo atau tag tidak wajib. Tolak jaringan yang salah dan checksum tidak valid. Catat cabang HD penerimaan/kembalian serta indeks; jangan menganggap jalur derivasi Bitcoin berlaku.

## Autentikasi dan batas

Aktifkan RPC secara eksplisit pada loopback numerik `127.0.0.1:18443` dengan token Bearer privat. Tidak ada pembukaan kunci dompet atau penandatanganan jarak jauh. Gunakan layanan lokal atau terowongan terautentikasi; permintaan browser Origin/Referer ditolak. JSON-RPC memakai POST `/rpc`, objek/array `params`, dan `id`; notifikasi mengembalikan HTTP 204. Batas: badan 8004096 byte, header 8192, batch 16, permintaan bersamaan 16, tenggat 10 detik; limit 1–1000, offset 0–1000000. Ada 28 metode dan 11 rute REST.

## Pencarian transaksi dan blok

`getrawtransaction` mencari rantai aktif dan mempool, bukan transaksi yang hanya ada di cabang yatim. Input menunjuk output terdahulu, bukan satu alamat pengirim unik. `getblock` menerima `verbose` Boolean; blok tidak aktif yang tersimpan memiliki `active=false`, `confirmations=-1`. Transaksi mentahnya tetap dapat diakses melalui hash blok. `findspendingtransaction` hanya mencari pembelanjaan terkonfirmasi pada rantai aktif; null bukan bukti ketersediaan. Periksa `gettxout` dengan `include_mempool=true`. Konfirmasi dan status aktif bisa berubah setelah reorganisasi.

## Verifikasi

Pasang dependensi lalu jalankan python examples/node_contract.py dari sumber. Kunci uji publik dan regtest sementara menguji pengiriman, penolakan, konfirmasi, reorganisasi, dan persistensi. Tidak ada dana nyata, profil pengguna, atau penanda tangan perangkat keras yang digunakan.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Dokumentasi](README.html) · [Antarmuka node](EXCHANGE_INTEGRATION.html) · [API RPC dan HTTP](RPC_API.html) · [Catatan versi](RELEASE_NOTES.html) · [Verifikasi](EXCHANGE_EXAMPLES.html)

[Referensi lengkap bahasa Inggris](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Biaya, transaksi yang ditinjau, dan kompatibilitas

Biaya adalah jumlah nilai input dikurangi jumlah nilai output. Perkiraan hanya menghitung output kembalian jika dompet benar-benar membuat kembalian yang memenuhi ambangnya. Sisa di bawah ambang tersebut ditambahkan ke biaya; biaya akhir dan total saldo yang dipotong ditampilkan untuk diperiksa. Tarif dinyatakan dalam yugeon/vB. Ukuran virtual adalah bobot transaksi dibagi empat, lalu dibulatkan ke atas.

Dompet memilih input dan output sekali saja, lalu menandatangani rencana transaksi yang sama. Saat dikonfirmasi, transaksi bertanda tangan yang tersimpan dikirim tanpa disusun ulang atau dihitung ulang biayanya. Perkiraan yang kedaluwarsa atau input yang sudah dibelanjakan memerlukan peninjauan baru. Diterima dalam antrean lokal bukan berarti sudah dikonfirmasi di dalam blok.

Untuk pembayaran P2WPKH biasa, dompet menghasilkan tanda tangan low-R dan low-S berukuran paling besar 71 bita, termasuk bita SIGHASH_ALL. Ini adalah kebijakan penandatanganan dan perkiraan ukuran, bukan batas konsensus baru bagi tanda tangan sah lainnya. Tanda tangan yang lebih pendek dapat memperkecil ukuran virtual sebenarnya. Saran tarif tetap memakai antrean lokal; mengikuti perhitungan ukuran Bitcoin tidak berarti memakai tarif jaringan Bitcoin.

## Komponen I2P Windows dan pemeriksaan keamanan

Paket Windows menyertakan i2pd 3.0.0 resmi dengan hash dan sertifikat koneksi awal yang diperbarui. Dalam pemeriksaan yang dicatat, Defender masih mendeteksi berkas I2P dan ZIP resmi tersebut. Kecocokan hash dengan sumber resmi tidak membuktikan keamanan atau memastikan deteksi keliru. Pengecualian berkas lokal hanya berlaku di komputer tempat pengecualian itu didaftarkan; paket publik tidak memasangnya. Komputer lain masih dapat memblokir berkas yang sama.

<!-- /payment-policy-20261116 -->

Setelah menerima respons versi yang sah, simpul memberi simpul lain waktu untuk mengirim konfirmasi. Jika dua koneksi keluar menuju simpul yang sama, jalur yang tersedia tetap terbuka sampai salah satunya selesai disinkronkan. Diagnostik bawaan menerima blok dengan bukti kerja yang sah sebelum bukti koneksi tersedia. Kemudian, diagnostik memeriksa tanda tangan tiga saksi, penerusan bukti koneksi, dan apakah bukti itu tetap tersimpan setelah mulai ulang.
