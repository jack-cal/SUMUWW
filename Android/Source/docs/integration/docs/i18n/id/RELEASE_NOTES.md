# SUMUWW Android 0.6.103 · Catatan versi

Dengan satu input senilai 1 SMW, biaya bergantung pada ada tidaknya kembalian. Jika input dan semua output berjenis P2WPKH dengan tarif 1 yugeon/vB, pengiriman 0.99999890 SMW dikenai biaya 110 yugeon tanpa kembalian. Pengiriman 0.8 SMW dari input yang sama menambahkan satu output untuk kembalian sehingga biayanya menjadi 141 yugeon. Dompet mengembalikan sisa dana jika jumlah yang tersisa setelah biaya mencapai batas minimum. Batas ini memperhitungkan biaya untuk membelanjakan dana tersebut nanti. Jika jumlahnya lebih kecil, sisanya masuk dalam biaya yang ditampilkan sebelum konfirmasi. Untuk input dompet SegWit asli (P2WPKH), perkiraan ukuran memperhitungkan hingga 71 byte untuk tanda tangan, termasuk jenis hash.


Saat dimulai ulang, node melanjutkan dari blok terakhir yang sudah diverifikasi secara lokal dan memeriksa blok baru. Jika catatan verifikasi yang tersimpan hilang atau tidak cocok, node memeriksa kembali riwayat yang tersimpan.

SUMUWW Android 0.6.103 · Node memvalidasi, menyimpan, meneruskan, dan menyediakan data rantai.

Spesifikasi API menjelaskan inti node tertanam. Aplikasi Android tidak memiliki layar pengaturan RPC.

## API RPC dan HTTP

validateaddress memeriksa checksum dan jaringan pilihan. decoded_only dari decoderawtransaction hanya berarti penguraian, bukan keabsahan tanda tangan atau konfirmasi. Output OP_RETURN menyimpan data bagi program eksternal. Node menyediakan kueri biaya, pemeriksaan sebelum pengiriman, status penggantian RBF, dan data sesuai urutan blok. Pengganti divalidasi sebelum transaksi tertunda dihapus. Multitanda tangan dan keluaran terkunci telah diterapkan untuk pengujian aktivasi terpisah; belum aktif di jaringan publik.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Biaya, transaksi yang ditinjau, dan kompatibilitas

Biaya adalah jumlah nilai input dikurangi jumlah nilai output. Perkiraan hanya menghitung output kembalian jika dompet benar-benar membuat kembalian yang memenuhi ambangnya. Sisa di bawah ambang tersebut ditambahkan ke biaya; biaya akhir dan total saldo yang dipotong ditampilkan untuk diperiksa. Tarif dinyatakan dalam yugeon/vB. Ukuran virtual adalah bobot transaksi dibagi empat, lalu dibulatkan ke atas.

Dompet memilih input dan output sekali saja, lalu menandatangani rencana transaksi yang sama. Saat dikonfirmasi, transaksi bertanda tangan yang tersimpan dikirim tanpa disusun ulang atau dihitung ulang biayanya. Perkiraan yang kedaluwarsa atau input yang sudah dibelanjakan memerlukan peninjauan baru. Diterima dalam antrean lokal bukan berarti sudah dikonfirmasi di dalam blok.

Untuk pembayaran P2WPKH biasa, dompet menghasilkan tanda tangan low-R dan low-S berukuran paling besar 71 bita, termasuk bita SIGHASH_ALL. Ini adalah kebijakan penandatanganan dan perkiraan ukuran, bukan batas konsensus baru bagi tanda tangan sah lainnya. Tanda tangan yang lebih pendek dapat memperkecil ukuran virtual sebenarnya. Saran tarif tetap memakai antrean lokal; mengikuti perhitungan ukuran Bitcoin tidak berarti memakai tarif jaringan Bitcoin.

## Kompatibilitas tanda tangan Android

Format berkas dompet, alamat, dan koin yang sudah ada tidak berubah. Cadangan dompet terenkripsi yang lama dapat dipulihkan di aplikasi baru untuk terus memakai dompet yang sama. Node Android 0.6.103 dan dompet 1.1.14 memakai kunci penandatanganan rilis yang baru. Keduanya tidak dapat menggantikan aplikasi yang ditandatangani dengan kunci berbeda. Simpan aplikasi lama dan datanya sampai tersedia cadangan dompet terenkripsi serta cara pemulihan yang berfungsi. Jangan menghapus aplikasi lama hanya untuk memaksa pemasangan pembaruan.

<!-- /payment-policy-20261116 -->
