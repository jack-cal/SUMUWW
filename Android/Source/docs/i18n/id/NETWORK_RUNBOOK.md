# SUMUWW Android 0.6.103 · Operasi node

Saat dimulai ulang, node melanjutkan dari blok terakhir yang sudah diverifikasi secara lokal dan memeriksa blok baru. Jika catatan verifikasi yang tersimpan hilang atau tidak cocok, node memeriksa kembali riwayat yang tersimpan.

SUMUWW Android 0.6.103 · Node memvalidasi, menyimpan, meneruskan, dan menyediakan data rantai.

[Dokumentasi](../../integration/docs/i18n/id/NETWORK_RUNBOOK.html)

<!-- payment-policy-20261116 -->

## Biaya, transaksi yang ditinjau, dan kompatibilitas

Biaya adalah jumlah nilai input dikurangi jumlah nilai output. Perkiraan hanya menghitung output kembalian jika dompet benar-benar membuat kembalian yang memenuhi ambangnya. Sisa di bawah ambang tersebut ditambahkan ke biaya; biaya akhir dan total saldo yang dipotong ditampilkan untuk diperiksa. Tarif dinyatakan dalam yugeon/vB. Ukuran virtual adalah bobot transaksi dibagi empat, lalu dibulatkan ke atas.

Dompet memilih input dan output sekali saja, lalu menandatangani rencana transaksi yang sama. Saat dikonfirmasi, transaksi bertanda tangan yang tersimpan dikirim tanpa disusun ulang atau dihitung ulang biayanya. Perkiraan yang kedaluwarsa atau input yang sudah dibelanjakan memerlukan peninjauan baru. Diterima dalam antrean lokal bukan berarti sudah dikonfirmasi di dalam blok.

Untuk pembayaran P2WPKH biasa, dompet menghasilkan tanda tangan low-R dan low-S berukuran paling besar 71 bita, termasuk bita SIGHASH_ALL. Ini adalah kebijakan penandatanganan dan perkiraan ukuran, bukan batas konsensus baru bagi tanda tangan sah lainnya. Tanda tangan yang lebih pendek dapat memperkecil ukuran virtual sebenarnya. 

## Kompatibilitas tanda tangan Android

Format berkas dompet, alamat, dan koin yang sudah ada tidak berubah. Cadangan dompet terenkripsi yang lama dapat dipulihkan di aplikasi baru untuk terus memakai dompet yang sama. Node Android 0.6.103 dan dompet 1.1.14 memakai kunci penandatanganan rilis yang baru. Keduanya tidak dapat menggantikan aplikasi yang ditandatangani dengan kunci berbeda. Simpan aplikasi lama dan datanya sampai tersedia cadangan dompet terenkripsi serta cara pemulihan yang berfungsi. Jangan menghapus aplikasi lama hanya untuk memaksa pemasangan pembaruan.

<!-- /payment-policy-20261116 -->

Setelah menerima respons versi yang sah, simpul memberi simpul lain waktu untuk mengirim konfirmasi. Jika dua koneksi keluar menuju simpul yang sama, jalur yang tersedia tetap terbuka sampai salah satunya selesai disinkronkan. 
