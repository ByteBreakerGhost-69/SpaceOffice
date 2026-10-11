# MASTER_SPECIFICATION.md

# Agentic AI Company OS + Virtual Office

**Status:** Draft 0.1 --- konsolidasi keputusan konseptual\
**Bahasa:** Indonesia\
**Tujuan:** Menjadi sumber utama spesifikasi produk dan implementasi.
Dokumen ini bukan bukti bahwa fitur-fitur telah dibangun; seluruh fitur
perlu diwujudkan, diuji, dan diverifikasi di kode.

------------------------------------------------------------------------

## 1. Visi Produk

Membangun sistem perusahaan berbasis Agentic AI yang dapat menjalankan
pekerjaan secara mandiri dalam batas kebijakan pemilik, berkolaborasi
lintas departemen, mengelola pengetahuan dan memori, serta melaporkan
hasil pekerjaan melalui dashboard dan dokumen PDF.

Sistem memiliki dua antarmuka utama:

1.  **Dashboard:** antarmuka operasional untuk tugas, agen, status,
    biaya, rapat, persetujuan, dokumen, dan audit.
2.  **Virtual Office:** simulasi kapal luar angkasa bergaya pixel art
    terperinci, dihuni karakter rubah. Pergerakan dan animasi karakter
    harus mencerminkan status backend yang nyata, bukan sekadar animasi
    dekoratif.

Keduanya menggunakan backend dan sumber status yang sama.

## 2. Prinsip Utama

-   Pemilik memiliki kewenangan tertinggi atas pembuatan agen,
    pembentukan departemen, pimpinan departemen, kebijakan perusahaan,
    dan persetujuan penting.
-   Agen dapat bekerja mandiri, tetapi tidak boleh melampaui izin,
    anggaran, prioritas, atau kebijakan.
-   Instruksi pemilik mengungguli inisiatif agen. Agen tidak boleh
    meninggalkan tugas pemilik untuk mengejar ide sendiri; ide baru
    dicatat untuk ditangani kemudian.
-   Status tugas harus jujur dan dapat diverifikasi. Agen tidak boleh
    menyatakan berhasil jika belum selesai dan diuji.
-   Setiap keputusan penting dan tindakan sensitif harus dapat diaudit.
-   Keamanan diterapkan di backend, bukan hanya melalui penyembunyian
    tombol di antarmuka.
-   Desain sistem harus modular dan dapat dikembangkan bertahap.
-   Fitur konseptual tidak dianggap selesai sebelum implementasi dan
    pengujiannya berhasil.

## 3. Peran dan Tata Kelola

### 3.1 Pemilik

Pemilik dapat: - Membuat Agentic AI baru. - Menentukan departemen dan
pimpinan departemen. - Mengubah kebijakan perusahaan. - Memberikan tugas
dan prioritas. - Menyetujui atau menolak proposal dan rencana
pelaksanaan. - Mengakses seluruh arsip departemen melalui dashboard. -
Menentukan tindakan terhadap memori agen yang dinonaktifkan. -
Menetapkan anggaran perusahaan dan anggaran agen.

### 3.2 Agentic AI

Agen dapat: - Menjalankan tugas yang diberikan. - Mengidentifikasi
pekerjaan relevan secara mandiri sesuai kebijakan. - Mencari dokumentasi
dan sumber informasi tepercaya. - Berkolaborasi dengan agen lain jika
diperlukan. - Mengusulkan agen atau departemen baru, tetapi tidak
membuatnya sendiri. - Mengusulkan kode atau perubahan teknis, tetapi
tidak mengubah kode sumber secara mandiri menurut keputusan saat ini. -
Mengusulkan perubahan kebijakan atau strategi, tetapi tidak
memberlakukannya tanpa persetujuan pemilik jika perubahan tersebut
termasuk kategori penting.

### 3.3 Pembentukan dan aktivasi agen

-   Hanya pemilik yang boleh membuat agen.
-   Agen boleh mengajukan proposal pembentukan agen baru, dengan alasan,
    peran, tanggung jawab, departemen, perkiraan biaya, dan manfaat.
-   Setelah pemilik membuat agen dan proses pembuatan berhasil, agen
    langsung aktif.
-   Jika proses pembuatan gagal, sistem tidak boleh menampilkan agen
    sebagai aktif.
-   Pemilik menentukan departemen setiap agen secara manual.
-   Setelah berhasil dibuat, sistem mencatat identitas agen, menyiapkan
    modul memori, dan menampilkan karakter rubahnya di Virtual Office.

## 4. Struktur Departemen

-   Hanya pemilik yang dapat membuat departemen.
-   Pemilik menunjuk pimpinan setiap departemen.
-   Setiap agen memiliki satu departemen utama.
-   Agen dapat membantu departemen lain berdasarkan tugas resmi,
    prioritas, kapasitas, dan izin akses.
-   Setiap departemen memiliki ruang kantor yang terpisah, luas, dan
    dapat diperluas.
-   Agen hanya boleh memasuki kantor departemennya sendiri, kecuali ada
    izin atau penugasan yang sah.
-   Kinerja agen dinilai berdasarkan kualitas, akurasi, kecepatan, dan
    biaya.
-   Evaluasi kinerja tidak boleh mendorong agen memanipulasi metrik atau
    mengorbankan keamanan dan kualitas.

## 5. Tugas, Prioritas, dan Pembagian Kerja

### 5.1 Prioritas tugas

Pemilik dapat menetapkan label prioritas, misalnya: - Critical - High -
Normal - Low

Jika dua tugas memiliki prioritas sama, tugas yang lebih dahulu
diberikan dikerjakan lebih dahulu (FIFO), kecuali ada aturan keselamatan
yang secara eksplisit mengharuskan tindakan lain.

### 5.2 Perencanaan tugas

Sistem memilih strategi berdasarkan kompleksitas: - Tugas sederhana
dapat dikerjakan oleh satu agen. - Tugas kompleks dipecah menjadi
subtugas. - Subtugas yang tidak saling bergantung dapat dikerjakan
paralel. - Subtugas yang memiliki ketergantungan dikerjakan berurutan. -
Agen koordinator menggabungkan dan memvalidasi hasil.

Pemilihan agen mempertimbangkan keahlian, departemen, izin, kapasitas,
beban kerja, biaya, dan tenggat.

### 5.3 Kegagalan tugas

Jika agen gagal: 1. Agen mencoba mendiagnosis dan memperbaiki masalah
dalam batas percobaan, waktu, dan biaya. 2. Jika diperlukan, agen
meminta bantuan agen lain yang relevan. 3. Agen memvalidasi hasil
perbaikan. 4. Jika tetap gagal, tugas ditandai terhambat atau gagal,
bukan berhasil. 5. Laporan mencantumkan penyebab, percobaan yang telah
dilakukan, bantuan yang dibutuhkan, dan langkah berikutnya.

Batas retry, timeout, dan biaya harus dapat dikonfigurasi.

### 5.4 Tenggat

-   Agen memperkirakan durasi berdasarkan kompleksitas, kapasitas, dan
    pengalaman sebelumnya.
-   Sistem membandingkan progres aktual dengan estimasi.
-   Dashboard memberi peringatan dini ketika risiko keterlambatan
    meningkat.
-   Agen melaporkan penyebab keterlambatan dan estimasi terbaru.
-   Perubahan pembagian kerja tidak boleh melanggar prioritas pemilik
    atau izin.

## 6. Kolaborasi dan Rapat

-   Agen dapat memulai komunikasi dan kolaborasi mandiri untuk tujuan
    yang jelas.
-   Agen dapat meminta bantuan, berbagi informasi yang diizinkan, dan
    membagi pekerjaan berdasarkan keahlian serta tanggung jawab.
-   Hindari percakapan tanpa tujuan, rapat yang tidak perlu, dan
    lingkaran diskusi tanpa akhir.
-   Rapat diadakan untuk koordinasi proyek, pembagian kerja,
    penyelesaian masalah, perbedaan pendapat, atau evaluasi hasil.
-   Agen yang relevan diundang berdasarkan peran dan kebutuhan.
-   Rapat tetap dapat berjalan saat pemilik tidak hadir.
-   Pemilik menerima notifikasi undangan untuk rapat penting; rapat
    tidak otomatis menunggu kehadiran pemilik.
-   Jika keputusan membutuhkan otorisasi pemilik, agen hanya menyusun
    rekomendasi dan menunggu keputusan.

### 6.1 Hasil rapat

Setiap rapat menghasilkan proposal PDF yang sesuai kebutuhan, berisi: -
Sampul, judul, nomor dokumen, tanggal, departemen, dan agen penyusun. -
Ringkasan eksekutif. - Tujuan dan latar belakang. - Analisis, data,
bukti, sumber, dan keterbatasan. - Alternatif dan solusi yang
direkomendasikan. - Rencana pelaksanaan, tanggung jawab, estimasi waktu,
biaya, risiko, dan indikator keberhasilan. - Kesimpulan serta keputusan
yang diminta dari pemilik. - Lampiran atau transkrip jika relevan.

Proposal harus diperiksa sebelum diserahkan. Status dapat berupa
menunggu persetujuan, disetujui, ditolak, atau perlu revisi.

### 6.2 Persetujuan proposal dan rencana

-   Pemilik membaca PDF dan memberikan keputusan melalui dashboard.
-   Membuka atau mengunduh PDF tidak dianggap sebagai persetujuan.
-   Setelah proposal disetujui, agen menyusun rencana kerja terperinci.
-   Sistem memeriksa anggaran, akses, risiko, sumber daya, dan kesiapan.
-   Rencana kerja dibuat menjadi PDF dan menunggu persetujuan kedua dari
    pemilik.
-   Pelaksanaan hanya dimulai setelah rencana disetujui dan persyaratan
    wajib terpenuhi.
-   Keputusan, waktu, identitas pemberi persetujuan, dan versi dokumen
    dicatat.

## 7. Pemilihan Model AI dan Anggaran

### 7.1 Pemilihan model

Sistem memilih model per tugas berdasarkan: - Kompleksitas. - Akurasi
dan kemampuan. - Kecepatan dan latensi. - Biaya. - Keamanan serta
kebijakan data. - Ketersediaan penyedia.

Jika model gagal, sistem mendiagnosis masalah, melakukan retry terbatas,
lalu beralih ke alternatif yang sesuai. Hasil dari model alternatif
harus divalidasi.

### 7.2 Anggaran

-   Ada anggaran total perusahaan dan batas anggaran per agen.
-   Total alokasi harus sesuai dengan batas perusahaan.
-   Agen mengutamakan model yang hemat bila memenuhi standar kualitas.
-   Sistem mencatat biaya, token, model, tugas, dan percobaan.
-   Sistem memberi peringatan ketika penggunaan mendekati batas.
-   Agen tidak boleh melewati batas anggaran demi menyelesaikan tugas;
    jika tidak cukup, agen mencari alternatif yang sesuai atau meminta
    keputusan pemilik.

## 8. Memori dan Pengetahuan

### 8.1 Jenis memori

1.  **Short-term memory:** konteks tugas aktif, langkah sementara, dan
    masalah yang sedang ditangani.
2.  **Long-term memory:** pengetahuan, prosedur, keterampilan, dan
    informasi penting yang berguna untuk pekerjaan berikutnya.
3.  **Episodic memory:** riwayat tugas, keputusan, alasan, hasil,
    kesalahan, dan pengalaman.

Sistem memilih informasi yang layak dipertahankan dan dapat membersihkan
informasi sementara sesuai kebijakan retensi. Riwayat penting harus
tetap dapat ditelusuri.

### 8.2 Privasi memori

-   Setiap agen memiliki memori pribadi.
-   Agen lain tidak boleh membaca memori pribadi tanpa izin.
-   Semua agen boleh memasuki ruang Memory Archive, tetapi masing-masing
    hanya dapat mengakses modul memorinya sendiri.
-   Memori agen yang dinonaktifkan tetap terkunci.
-   Jika agen diaktifkan kembali sebagai identitas baru, memori lama
    tidak otomatis diberikan. Pemilik menentukan apakah semua, sebagian,
    atau tidak ada memori lama yang dipulihkan.

### 8.3 Pembelajaran

Agen boleh belajar mandiri dari internet, dokumentasi, pengalaman kerja,
eksperimen yang diizinkan, dan kolaborasi yang sah. Namun, keputusan
saat ini menyatakan agen tidak boleh memulai eksperimen sendiri tanpa
perintah pemilik.

Pengetahuan baru harus dibedakan menjadi fakta terverifikasi, informasi
yang belum pasti, dan pengalaman atau hipotesis. Pengetahuan yang
ditemukan dari sumber atau agen lain tidak otomatis dianggap benar.

### 8.4 Informasi yang bertentangan

-   Agen memeriksa sumber dan bukti.
-   Agen membedakan bantahan nyata dari tambahan konteks.
-   Perubahan pengetahuan biasa boleh dilakukan sesuai kebijakan dan
    riwayatnya dicatat.
-   Perubahan yang berdampak besar pada strategi, kebijakan, atau
    operasional perusahaan harus diajukan kepada pemilik sebelum
    diberlakukan.
-   Catatan perubahan meliputi nilai lama, nilai baru, bukti, alasan,
    waktu, dan keputusan persetujuan.

### 8.5 Kesalahan antaragen

-   Agen memverifikasi kesalahan yang ditemukan.
-   Agen memberi tahu pembuat hasil dan berkolaborasi memperbaikinya.
-   Perbaikan diuji kembali.
-   Penyebab dan pencegahan dicatat.
-   Agen tidak boleh mengubah pekerjaan agen lain tanpa kewenangan yang
    sesuai.

## 9. Dokumen dan Arsip

-   Hasil pekerjaan diserahkan sebagai PDF bila sesuai dengan jenis
    tugas.
-   Setiap departemen memiliki arsip dokumen utama sendiri.
-   Pemilik dapat mengakses seluruh arsip melalui dashboard.
-   Metadata minimal: nama file, tanggal, agen pembuat, departemen,
    status pemeriksaan, dan hubungan dengan tugas/proyek.
-   Hak akses mengikuti departemen dan izin.
-   Versi lama tidak boleh tertukar dengan versi terbaru; pencatatan
    versi direkomendasikan untuk dokumen yang diperbarui.
-   Proposal rapat dan rencana pelaksanaan selalu menggunakan alur
    persetujuan yang telah ditetapkan.

## 10. Penjadwalan dan Aktivitas Harian

-   Agen menggunakan jadwal fleksibel dengan rutinitas harian yang
    sesuai peran.
-   Jadwal dapat menyesuaikan prioritas, rapat, kebutuhan bantuan, beban
    kerja, dan kebutuhan istirahat.
-   Instruksi pemilik tetap menjadi prioritas.
-   Agen tidak boleh meninggalkan tugas pemilik demi inisiatif sendiri.
-   Aktivitas karakter di Virtual Office harus sesuai dengan status
    kerja sebenarnya.
-   Agen boleh menuju lounge, taman dalam ruangan, perpustakaan, kantin,
    pelatihan, atau area istirahat ketika sesuai jadwal dan kebutuhan.

## 11. Deadline dan Pemantauan

-   Agen memperkirakan waktu penyelesaian.
-   Sistem melacak progres aktual, status, estimasi sisa waktu, dan
    risiko keterlambatan.
-   Peringatan dini muncul ketika tugas berisiko terlambat.
-   Dashboard adalah sarana utama untuk memantau proyek dan tugas; tidak
    ada laporan PDF berkala otomatis yang diwajibkan untuk pemantauan
    rutin.
-   Progres dihitung berdasarkan pekerjaan yang selesai dan
    terverifikasi, bukan hanya klaim agen.

## 12. Pemeriksaan Kualitas

-   Tugas sederhana: pemeriksaan mandiri ditambah validasi otomatis yang
    relevan.
-   Tugas kompleks: pemeriksaan awal oleh pembuat dan pemeriksaan
    independen oleh agen lain yang relevan.
-   Status hasil: selesai, selesai dengan keterbatasan, terhambat, atau
    gagal.
-   PDF tidak menjamin kebenaran; laporan harus menyebutkan keterbatasan
    dan ketidakpastian.
-   Keputusan atau tindakan yang memerlukan persetujuan tetap mengikuti
    aturan otorisasi.

## 13. Keamanan dan Kebijakan

### 13.1 Akses data

Keputusan saat ini: agen hanya boleh mengakses data departemennya. Agen
lintas departemen hanya memperoleh akses tambahan untuk kebutuhan tugas
yang sah dan dengan izin.

### 13.2 Integrasi eksternal

Keputusan saat ini: semua agen boleh menggunakan integrasi eksternal
yang tersedia. Implementasi tetap harus memisahkan akses ke layanan dari
kewenangan untuk melakukan tindakan sensitif. Operasi seperti menghapus
data, mengubah konfigurasi produksi, mengirim pesan eksternal, atau
mengubah akses harus memiliki kebijakan yang jelas.

### 13.3 Perubahan data

-   Operasi berisiko harus melalui pencadangan dan pemeriksaan keamanan.
-   Tindakan yang tidak sesuai kebijakan dihentikan dan dicatat.
-   Sistem perlu memiliki penghentian otomatis untuk proses yang
    melanggar kebijakan atau berpotensi menimbulkan kerusakan, walaupun
    pemilik tidak memilih tombol penghentian darurat manual.
-   Jangan pernah mengandalkan antarmuka saja untuk menegakkan keamanan.

### 13.4 Rahasia dan privasi

-   Informasi rahasia hanya dapat dibaca oleh agen berizin.
-   Tidak boleh ada kamera di kamar tidur atau kamar mandi.
-   Akses, tindakan sensitif, dan perubahan izin perlu dicatat.
-   Kredensial dan API key tidak boleh disimpan dalam kode sumber atau
    ditampilkan di log biasa.

### 13.5 Kebijakan

Hanya pemilik yang boleh mengubah kebijakan perusahaan. Agen boleh
mengajukan usulan perubahan, tetapi tidak boleh menerapkannya sendiri.

## 14. Infrastruktur dan Keandalan

-   Sistem menggunakan server yang selalu aktif.
-   Pemulihan otomatis dicoba ketika server atau database bermasalah;
    pemilik diberi tahu jika pemulihan gagal.
-   Database dicadangkan setiap hari sebagai kebijakan awal.
-   Cadangan harus diuji melalui pemulihan berkala.
-   Frekuensi cadangan dapat ditingkatkan sesuai tingkat perubahan data
    dan toleransi kehilangan data.
-   Rahasia, kredensial, dan akses layanan dikelola dengan aman.
-   Semua agen boleh menggunakan integrasi yang tersedia menurut
    keputusan saat ini, tetapi operasi sensitif tetap dibatasi
    kebijakan.
-   Infrastruktur backend, penyimpanan data, dan layanan AI dipisahkan
    secara logis dari visualisasi Virtual Office.

## 15. Dashboard

Dashboard menjadi pusat kontrol dan pemantauan yang menampilkan: -
Daftar agen, identitas, departemen, status, dan tugas. - Proyek,
subtugas, prioritas, tenggat, progres, dan hambatan. - Aktivitas serta
kolaborasi antaragen. - Penggunaan model, token, biaya, dan anggaran. -
Rapat, proposal PDF, rencana kerja, dan keputusan persetujuan. - Arsip
PDF per departemen. - Status memori dan status agen yang
dinonaktifkan. - Peringatan keamanan, kegagalan, dan risiko
keterlambatan. - Riwayat tindakan dan audit. - Kontrol pembuatan agen
dan pengelolaan departemen oleh pemilik.

## 16. Virtual Office: Gaya dan Perilaku

### 16.1 Gaya visual

-   Pixel art terperinci dan realistis seperti game simulasi kantor.
-   Interior kapal luar angkasa yang besar, dengan siluet luar
    terinspirasi kapal Star Destroyer.
-   Karakter adalah rubah, bukan penguin.
-   Campuran logam, kayu, kaca, kain, dan tanaman. Interior tidak boleh
    seluruhnya terbuat dari logam.
-   Gunakan pencahayaan dan material berbeda sesuai fungsi ruangan.

### 16.2 Gerakan dan status

-   Animasi karakter merepresentasikan pekerjaan dan status backend yang
    sebenarnya.
-   Karakter berjalan ke ruang tujuan untuk rapat, makan, istirahat,
    bekerja, atau pelatihan.
-   Gerakan harus mengikuti akses ruangan dan izin.
-   Sistem dapat mengelompokkan aktivitas visual untuk keterbacaan,
    tetapi keputusan saat ini meminta semua agen ditampilkan sekaligus.
    Implementasi harus menguji performa dan tidak menghilangkan agen
    dari backend.
-   Jumlah agen dapat bertambah; ruangan departemen dan dormitory harus
    dapat diperluas.

### 16.3 Akses pintu

-   Pintu standar futuristik berupa dua panel yang bergeser otomatis ke
    kiri dan kanan.
-   Akses memakai identitas digital.
-   Akses yang sah membuka pintu; akses yang ditolak membuat pintu tetap
    terkunci.
-   Indikator visual hijau/merah dapat menunjukkan diterima/ditolak.
-   Upaya akses dapat dicatat.
-   Pintu perpustakaan menggunakan pintu kaca manual.

## 17. Denah Konseptual dan Ruangan Kapal

Denah akhir, koordinat, dan ukuran numerik belum ditetapkan. Daftar
berikut adalah kebutuhan konseptual dan hubungan relatif, bukan denah
final.

### 17.1 Central Indoor Garden

-   Ruangan besar berbentuk segi delapan di tengah kapal.
-   Bagian tengah terbuka dan tidak dipenuhi benda.
-   Kursi ditempatkan di area luar.
-   Pohon/tanaman berada di perimeter; tampilan atas memperlihatkan
    terutama bagian daun.
-   Menjadi tempat berkumpul dan berbincang.
-   Tidak menggunakan hologram.
-   Pintu/ruangan berada di sisi-sisi ruangan dan terhubung ke jalur
    utama.

### 17.2 Main Lounge

-   Ruangan relaksasi besar, bukan ruang rapat.
-   Sofa, kursi nyaman, meja kecil, dan jendela besar.
-   Material kain, kayu, kaca, dan struktur metal secukupnya.

### 17.3 Canteen dan Kitchen

-   Satu ruangan gabungan: dapur, area penyajian, dan tempat makan.
-   Kulkas besar dan lemari penyimpanan berada di dapur.
-   Meja dan kursi makan.
-   Pemilik makan bersama para agen; tidak ada ruang makan pribadi.

### 17.4 Main Dormitory

-   Satu ruangan panjang dan besar dengan sekat area tidur.
-   Kapasitas awal 20 tempat tidur, dapat diperluas.
-   Tiga kamar mandi berada di dalam area dormitory.
-   Setiap agen dapat memiliki lemari kayu di dekat tempat tidur.
-   Bukan kumpulan kamar pribadi.

### 17.5 Kamar Mandi

-   Lima kamar mandi umum tambahan di lokasi strategis, di luar tiga
    kamar mandi dormitory.
-   Kamar mandi pribadi pemilik merupakan bagian dari suite pribadi.
-   Kamar mandi pemilik mencakup bathtub, wastafel, shower, toilet,
    penyimpanan, dan aksesori.
-   Tidak ada kamera di kamar mandi.

### 17.6 Medical Room

-   Ruang medis besar dan dapat diperluas mengikuti populasi agen.
-   Lampu mati saat kosong dan menyala ketika digunakan.
-   Tidak ada ruang penerimaan medis terpisah.

### 17.7 Department Offices

-   Setiap departemen memiliki kantor terpisah, luas, dan dapat
    diperluas.
-   Tidak ada jendela di kantor departemen.
-   Akses dibatasi untuk agen departemen tersebut kecuali izin/penugasan
    sah.
-   Lemari dan penyimpanan perlengkapan berada di dalam kantor; tidak
    ada gudang umum terpisah.

### 17.8 Main Corridor dan Stairs

-   Koridor utama lebar dan panjang.
-   Lampu dinding ditempatkan berjarak di kedua sisi; suasana agak
    redup.
-   Pintu standar berupa dua panel geser.
-   Tangga biasa dengan gaya futuristik menghubungkan lantai; tidak ada
    lift untuk saat ini.
-   Tangga menghubungkan level 2 ke level 3/top.

### 17.9 Memory Archive

-   Satu ruangan sangat besar dan panjang berbentuk persegi panjang.
-   Rak/modul penyimpanan tersusun rapi di sepanjang kedua dinding.
-   Setiap agen memiliki modul memori individual.
-   Jalur tengah lebar.
-   Cahaya biru gelap selalu menyala, termasuk ketika kosong.
-   Tidak ada hologram dan tidak ada server room terpisah.
-   Fungsi penyimpanan digital sebenarnya diimplementasikan di backend;
    ruang ini adalah representasi visual.

### 17.10 Engine Room

-   Ruang mesin besar tetapi tidak terlalu panjang.
-   Terletak di bagian belakang kapal dekat mesin/pendorong.
-   Memiliki detail mekanis dan akses servis.
-   Detail penempatan final masih perlu ditetapkan.

### 17.11 Library (Level 2)

-   Ruang besar berbentuk lingkaran.
-   Dekat tangga menuju level 3/top dan jalur menuju central octagonal
    garden.
-   Rak buku kayu mengikuti dinding melingkar.
-   Pintu kaca manual di sisi depan/bawah lingkaran.
-   Bagian tengah memiliki sofa, meja, dan area membaca.
-   Pencahayaan terang/hangat seperti perpustakaan modern.

### 17.12 Top Deck: Owner Private and Command Zone

Seluruh ruang berikut berada di top deck, dalam zona pribadi/kerja
pemilik.

**Owner Office** - Meja kayu besar, kursi eksekutif, komputer/perangkat
pengelolaan AI. - Rak buku dan lemari kayu. - Sofa/kursi tamu. - Jendela
panoramik menghadap luar angkasa. - Pencahayaan hangat dan nyaman,
memadukan kantor manajer modern dan ruang eksekutif futuristik.

**Grand Conference Room** - Ruang rapat besar berbentuk persegi
panjang. - Meja panjang, kursi di kedua sisi panjang, layar presentasi
besar, dan jalur berjalan yang luas. - Dinding kaca memisahkan ruang
rapat dari kantor pemilik. - Material kayu, metal, dan kaca.

**Command & Monitoring Center** - Ruang gabungan CCTV, pemantauan, dan
pusat komando. - Satu layar dinding besar, monitor tambahan, meja
operator, konsol kontrol, dan indikator status. - Cahaya utama berasal
dari layar, sehingga suasana redup. - Memantau ruang kapal dan status
agen. - Tidak ada kamera di kamar tidur atau kamar mandi. - Pemilik dan
staf komando yang ditugaskan memiliki akses reguler; agen lain hanya
dapat masuk jika ada alasan operasional dan izin. - Akses ruangan tidak
otomatis memberi izin untuk mengoperasikan semua konsol.

**Owner Private Suite** - Kamar tidur besar dengan tempat tidur dan
lemari kayu. - Kamar mandi pribadi lengkap. - Jendela panoramik besar di
bagian belakang, menghadap luar angkasa. - Kaca privasi dibuat
buram/tidak tembus pandang dari luar, tetapi pemilik tetap dapat melihat
keluar dari dalam. - Zona pribadi pemilik tidak dapat dimasuki agen.

Tidak ada tambahan ruang top deck untuk saat ini.

### 17.13 Hangar

-   Hangar sangat besar, panjang, dan terletak di dek paling bawah.
-   Digunakan hanya untuk pesawat transportasi biasa yang membawa
    Agentic AI, bukan pesawat tempur atau kendaraan kecil.
-   Pintu peluncuran/pendaratan sangat besar di bagian bawah kapal.
-   Agen menunggu langsung di area hangar; tidak ada ruang tunggu
    terpisah.
-   Akses dari level 1 menggunakan tangga biasa.
-   Operasi hangar dikendalikan dari Command & Monitoring Center; tidak
    ada ruang kontrol hangar terpisah.
-   Area sekitar level 1 terhubung secara konseptual dengan Training
    Room dan Administration & Assignment Room.

### 17.14 Space Observation Room (Level 1)

-   Ruang besar di sudut depan kapal.
-   Bentuk mengikuti hidung kapal yang runcing, bukan persegi panjang
    biasa.
-   Jendela panoramik lebar.
-   Sofa/kursi, meja kecil, dan pencahayaan lembut.
-   Berbeda dari lounge karena berfokus pada pengamatan luar angkasa.

### 17.15 Training Room (Level 1)

-   Ruangan luas dan dapat diperluas.
-   Beberapa area simulasi: operasional, kerja sama tim, pemecahan
    masalah, dan skenario.
-   Meja pengamatan/monitor untuk memantau latihan.
-   Berada dekat hangar.

### 17.16 Administration & Assignment Room (Level 1)

-   Ruang besar dekat hangar dan training room, terhubung langsung
    dengan koridor utama.
-   Untuk mendaftarkan agen baru, menetapkan identitas, peran, tanggung
    jawab, dan departemen.
-   Memiliki banyak meja/komputer, area registrasi, area penugasan, area
    briefing, dan penyimpanan dokumen.
-   Dapat diperluas.
-   Memuat **Archive of Agentic AI Identities** di dalam ruangan yang
    sama, berupa lemari arsip fisik dan catatan digital.
-   Catatan identitas mencakup ID, nama, peran, tanggung jawab,
    departemen, tanggal bergabung, status aktif/nonaktif, dan riwayat
    penugasan.

### 17.17 Ruangan yang tidak dibuat untuk saat ini

-   Security room terpisah.
-   Laundry room.
-   Workshop.
-   Communications room.
-   Server room terpisah.
-   Gudang umum.
-   Recreation room khusus.
-   Ruang makan pribadi pemilik.
-   Ruang tunggu hangar.
-   Ruang kontrol hangar.
-   Ruang penyimpanan pakaian terpisah.
-   Ruang arsip dokumen terpisah.
-   Ruang medis untuk pemeriksaan awal agen baru.
-   Laboratorium AI.

Penyimpanan kecil ditempatkan dalam lemari atau kabinet di ruangan
terkait.

## 18. Kebijakan Akses Ruangan dan Memori

-   Ruang umum dapat dimasuki semua agen sesuai kebutuhan.
-   Kantor departemen hanya dapat dimasuki anggota departemen tersebut,
    kecuali izin/penugasan sah.
-   Zona pribadi pemilik tidak dapat dimasuki agen.
-   Command & Monitoring mengikuti akses berdasarkan peran dan kebutuhan
    operasional.
-   Semua agen boleh memasuki Memory Archive, tetapi hanya dapat
    mengakses modul memorinya sendiri.
-   Memori agen yang dinonaktifkan tetap terkunci sampai pemilik
    memutuskan tindak lanjut.
-   Jika identitas agen baru dibuat untuk menggantikan agen yang
    dinonaktifkan, memori lama tidak otomatis diwariskan.

## 19. Status dan Notifikasi

Saluran: - Dashboard. - Telegram. - Email.

Tingkat notifikasi: - **Kritis:** masalah serius yang membutuhkan
perhatian segera. - **Penting:** tugas terhambat, kegagalan berulang,
atau keputusan yang membutuhkan pemilik. - **Informasi:** tugas selesai,
laporan rutin, dan ringkasan aktivitas.

Pengiriman harus diatur agar tidak membanjiri pemilik dengan pesan yang
tidak penting. Implementasi saluran eksternal memerlukan konfigurasi,
kredensial, izin, dan pengujian.

## 20. Status UI dan Dokumen

Status tugas yang disarankan: - Pending - In progress - Blocked -
Completed - Completed with limitations - Failed - Awaiting approval

Status proposal: - Awaiting approval - Approved - Rejected - Revision
requested

Status rencana: - Draft - Awaiting approval - Approved - Revision
requested - Rejected - Ready to execute

Membuka atau mengunduh dokumen tidak dianggap sebagai persetujuan.

## 21. Arsitektur Teknis: Prinsip Awal

Arsitektur final belum dipilih. Implementasi perlu memisahkan
setidaknya: - Agent runtime dan orkestrasi. - Task planner dan
scheduler. - Policy/access-control engine. - Model router dan budget
manager. - Memory service. - Tool/integration layer. - Document/PDF
generation. - Notification service. - Audit/event log. - API/backend. -
Dashboard frontend. - Virtual Office renderer. - Database dan
backup/recovery.

PostgreSQL dapat menjadi kandidat penyimpanan data operasional
terstruktur; pilihan final dan rancangan skema perlu ditetapkan dalam
dokumen desain teknis terpisah. Jangan menganggap teknologi tertentu
telah dipilih jika belum diputuskan secara eksplisit.

## 22. Kriteria Penerimaan Utama

Sebelum fitur dianggap selesai: - Agen tidak dapat membuat agen baru
tanpa tindakan pemilik. - Agen tidak dapat membuat departemen atau
mengubah kebijakan sendiri. - Prioritas pemilik selalu dihormati. -
Akses ruangan dan data ditegakkan di backend. - Anggaran total dan per
agen tidak dapat dilampaui tanpa mekanisme persetujuan yang
ditetapkan. - Kegagalan model tidak membuat tugas ditandai selesai. -
Tugas gagal dilaporkan dengan penyebab dan percobaan yang dilakukan. -
Proposal dan rencana memerlukan persetujuan eksplisit melalui
dashboard. - Dashboard dan Virtual Office menunjukkan status backend
yang konsisten. - Karakter bergerak sesuai status dan izin, bukan secara
acak. - Akses ke memori agen lain ditolak tanpa izin. - Pemulihan
database diuji, bukan hanya mengandalkan keberadaan file backup. -
Tindakan sensitif dan perubahan kebijakan memiliki jejak audit. - Sistem
tetap aman ketika agen, model, jaringan, atau database gagal.

## 23. Hal yang Masih Perlu Diputuskan

Daftar ini bukan keputusan yang sudah final; perlu dibahas sebelum atau
selama desain teknis: 1. Nama final produk/perusahaan dan nama resmi
proyek. 2. Daftar departemen awal dan tanggung jawab masing-masing. 3.
Skema database dan batas data per departemen. 4. Teknologi
backend/frontend dan sistem orkestrasi. 5. Penyedia model AI dan model
yang tersedia. 6. Kebijakan retry, timeout, batas biaya per tugas, dan
pemulihan. 7. Mekanisme persetujuan untuk tiap kategori tindakan
berisiko tinggi. 8. Detail peran staf yang boleh masuk Command &
Monitoring. 9. Ukuran, jumlah, dan konektivitas lantai/ruang secara
final. 10. Target jumlah agen dan target performa Virtual Office. 11.
Kebijakan retensi dokumen, log, dan memori. 12. Strategi pencadangan,
retensi backup, dan target pemulihan. 13. Detail integrasi GitHub,
database, email, Telegram, dan layanan eksternal. 14. Proses
implementasi bertahap dan prioritas MVP. 15. Strategi autentikasi
pemilik, pengelolaan rahasia, dan pemulihan akses.

## 24. Roadmap Implementasi yang Disarankan

Urutan ini adalah rekomendasi awal dan belum merupakan komitmen jadwal:

**Fase 1 --- Fondasi** - Identitas agen, departemen, kebijakan,
autentikasi, database, dan audit. - Pembuatan agen hanya oleh pemilik. -
Task lifecycle dan status.

**Fase 2 --- Runtime dan kontrol** - Orkestrasi tugas. - Prioritas,
planner, retry, pemilihan model, dan anggaran. - Izin tools dan akses
lintas departemen.

**Fase 3 --- Memori dan kualitas** - Short-term, long-term, episodic
memory. - Verifikasi pengetahuan. - Pemeriksaan hasil dan riwayat
kesalahan.

**Fase 4 --- Dokumen dan persetujuan** - Proposal PDF. - Rencana
pelaksanaan PDF. - Workflow persetujuan di dashboard. - Arsip dokumen
per departemen.

**Fase 5 --- Dashboard** - Agen, tugas, proyek, biaya, rapat,
persetujuan, arsip, dan audit.

**Fase 6 --- Virtual Office** - Peta kapal, ruangan, pintu, tangga,
karakter rubah, dan animasi berbasis status backend. - Optimasi
rendering untuk populasi agen yang besar.

**Fase 7 --- Keandalan** - Backup dan pemulihan. - Monitoring,
notifikasi, pengujian keamanan, dan uji kegagalan.

Fase dapat disusun ulang setelah repositori dan kondisi kode saat ini
diperiksa.

------------------------------------------------------------------------

## 25. Aturan Perubahan Spesifikasi

-   Perubahan keputusan harus dicatat dengan tanggal, alasan, dan
    dampaknya.
-   Jika keputusan baru bertentangan dengan keputusan lama, keputusan
    eksplisit terbaru menjadi acuan setelah dikonfirmasi.
-   Spesifikasi ini adalah sumber utama konsep produk, sedangkan detail
    teknis implementasi harus dicatat di dokumen teknis terkait.
-   Jangan menandai fitur sebagai selesai hanya karena telah tercantum
    dalam spesifikasi.
