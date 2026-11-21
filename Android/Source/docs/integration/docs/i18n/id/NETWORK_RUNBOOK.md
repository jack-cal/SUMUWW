# SUMUWW Android 0.7.8 · Operasi node

Saat dimulai ulang, node melanjutkan dari blok terakhir yang sudah diverifikasi secara lokal dan memeriksa blok baru. Jika catatan verifikasi yang tersimpan hilang atau tidak cocok, node memeriksa kembali riwayat yang tersimpan.

SUMUWW Android 0.7.8 · Node memvalidasi, menyimpan, meneruskan, dan menyediakan data rantai.

## Jaringan dan alamat

Jaringan publik adalah `sumuww`, dengan alias internal `dora`. Periksa hash genesis di bawah. Alamat asli memakai witness v0 P2WPKH dan HASH160 kunci publik secp256k1 terkompresi. Memo atau tag tidak wajib. Tolak jaringan yang salah dan checksum tidak valid. Catat cabang HD penerimaan/kembalian serta indeks; jangan menganggap jalur derivasi Bitcoin berlaku.

## Pencarian transaksi dan blok

`getrawtransaction` mencari rantai aktif dan mempool, bukan transaksi yang hanya ada di cabang yatim. Input menunjuk output terdahulu, bukan satu alamat pengirim unik. `getblock` menerima `verbose` Boolean; blok tidak aktif yang tersimpan memiliki `active=false`, `confirmations=-1`. Transaksi mentahnya tetap dapat diakses melalui hash blok. `findspendingtransaction` hanya mencari pembelanjaan terkonfirmasi pada rantai aktif; null bukan bukti ketersediaan. Periksa `gettxout` dengan `include_mempool=true`. Konfirmasi dan status aktif bisa berubah setelah reorganisasi.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Biaya, transaksi yang ditinjau, dan kompatibilitas

Biaya adalah jumlah nilai input dikurangi jumlah nilai output. Perkiraan hanya menghitung output kembalian jika dompet benar-benar membuat kembalian yang memenuhi ambangnya. Sisa di bawah ambang tersebut ditambahkan ke biaya; biaya akhir dan total saldo yang dipotong ditampilkan untuk diperiksa. Tarif dinyatakan dalam yugeon/vB. Ukuran virtual adalah bobot transaksi dibagi empat, lalu dibulatkan ke atas.

Dompet memilih input dan output sekali saja, lalu menandatangani rencana transaksi yang sama. Saat dikonfirmasi, transaksi bertanda tangan yang tersimpan dikirim tanpa disusun ulang atau dihitung ulang biayanya. Perkiraan yang kedaluwarsa atau input yang sudah dibelanjakan memerlukan peninjauan baru. Diterima dalam antrean lokal bukan berarti sudah dikonfirmasi di dalam blok.

Untuk pembayaran P2WPKH biasa, dompet menghasilkan tanda tangan low-R dan low-S berukuran paling besar 71 bita, termasuk bita SIGHASH_ALL. Ini adalah kebijakan penandatanganan dan perkiraan ukuran, bukan batas konsensus baru bagi tanda tangan sah lainnya. Tanda tangan yang lebih pendek dapat memperkecil ukuran virtual sebenarnya. 

## Kompatibilitas tanda tangan Android

Format berkas dompet, alamat, dan koin yang sudah ada tidak berubah. Cadangan dompet terenkripsi yang lama dapat dipulihkan di aplikasi baru untuk terus memakai dompet yang sama. Node Android 0.6.103 dan dompet 1.1.14 memakai kunci penandatanganan rilis yang baru. Keduanya tidak dapat menggantikan aplikasi yang ditandatangani dengan kunci berbeda. Simpan aplikasi lama dan datanya sampai tersedia cadangan dompet terenkripsi serta cara pemulihan yang berfungsi. Jangan menghapus aplikasi lama hanya untuk memaksa pemasangan pembaruan.

<!-- /payment-policy-20261116 -->

Setelah menerima respons versi yang sah, simpul memberi simpul lain waktu untuk mengirim konfirmasi. Jika dua koneksi keluar menuju simpul yang sama, jalur yang tersedia tetap terbuka sampai salah satunya selesai disinkronkan.

<!-- poll-recovery-20261119 -->

Pembaruan sinkronisasi dicoba kembali setelah terjadi kesalahan internal. Kesalahan pada satu peer tidak lagi menghentikan pembaruan peer lain. Penambangan tetap memerlukan peer yang baru saja diverifikasi; koneksi yang terbuka saja tidak cukup. Saat penambangan dimulai di ponsel, aplikasi kini menunggu sinkronisasi selesai, bukan langsung berhenti. Terhentinya pemrosesan jaringan saat memverifikasi bukti koneksi dan meminta riwayat telah diperbaiki. Penambangan latar belakang tetap aktif.
