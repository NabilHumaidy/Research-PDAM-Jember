# RISET DATA OPERASIONAL & TEKNIS PERUMDAM TIRTA PANDALUNGAN KAB. JEMBER
*Materi persiapan lomba business case · Pemkab Jember-owned water utility (PDAM → Perumdam)*

**Catatan keterbacaan (penting):** Semua domain KemenPU (`pu.go.id/ppspamsip`, `aplikasi.bppspam.kim.pu.go.id`) **gagal resolusi DNS** dari lingkungan riset ini (curl & WebFetch, berulang) → data BPPSPAM rating & PPSPAM/SIP PDAM tidak bisa diakses dan diberi label **TIDAK DITEMUKAN (domain tidak dapat diakses)**. Demikian pula situs resmi PDAM `perumdamtirtapandalungan.com` **tidak resolve** (domain ybs merespons NXHOST; keberadaan domain email saja yang terverifikasi di LK). Data statistik BPS "Jember Dalam Angka" tidak dapat diekstrak (situs Next.js client-rendered). Karena itu, **tulang punggung data riset ini adalah Laporan Keuangan BUMD Jember yang sudah diaudit (TA2022 & TA2023)**, yang memuat tabel kinerja operasional PDAM terlengkap yang tersedia secara publik.

---

## 0. PROFIL & LEGALITAS

| Item | Data | Tahun | Sumber |
|---|---|---|---|
| Nama | Perumdam Tirta Pandalungan (eks PDAM Kab. Jember) | — | LK BUMD |
| Dasar hukum | **Perda No. 4/1975** (pendirian PDAM) → **Perda No. 3 Tahun 2022** (19 April 2022, konversi PDAM→Perumdam) | 2022 | http://www.jemberkab.go.id/wp-content/uploads/2024/09/26.-LK-BUMD-2023.pdf |
| Kantor pusat | Jl. Trunojoyo No. 73 Jember · (0331) 483509/485421 · perumdam@tirtapandalungan.com | 2023 | LK BUMD 2023 |
| Unit organisasi | Kantor Pusat + **3 Kantor Area: Mangli (MAPAN), Rambipuji (TRAJEM), Puger (GERBANG)** + IKK Rambipuji, Mumbulsari, Jelbuk, Panti, Balung; Kantor Area Tanggul & Puger | 2023 | LK BUMD 2023 |
| Karyawan | **175** (2023) / 179 (2022) | 2022–23 | LK BUMD 2023 |
| Bisnis | Air minum perpipaan + **AMDK "Hazora"** (PM Rp2 M era Bupati Faida; kemasan dibeli 2023 Rp11,85 jt) | 2019/2023 | beritajatim.com & LK |
| MoU AM&DK kampus | MoU Perumdam–Universitas Jember untuk AMDK "**Unej Cool**" | 2024 | https://beritajatim.com/perumdam-tirta-pandalungan-jember-suplai-air-untuk-unej-cool |

---

## 1. CAKUPAN PELAYANAN (SERVICE COVERAGE)

| Indikator | 2022 | 2023 | Tahun data | Sumber |
|---|---|---|---|---|
| Jumlah pelanggan (SR) | **43.654** | **44.029** | per 31 Des | LK BUMD TA2022/TA2023 |
| Penduduk Kab. Jember | 2.581.486 | **2.584.233** | per 31 Des | LK BUMD |
| Penduduk terlayani | 261.924 | **264.174** | per 31 Des | LK BUMD |
| Penduduk di *daerah pelayanan* | 1.070.706 | **1.032.013** | per 31 Des | LK BUMD |
| Pertumbuhan SR YoY | — | **+375 SR (+0,86%)** | 2023 | hitung dari LK |
| SR meter ditera | 3.673 | 9.143 | per 31 Des | LK BUMD |
| Pemakaian rata-rata | 172,25 m³/thn/SR | **171,72 m³/thn/SR** | per 31 Des | LK BUMD |
| Kecepatan penyambungan baru | — | **6 hari** | 2023 | LK BUMD 2023 |
| Cakupan kecamatan | **baru 13 dari 31 kecamatan** | — | Okt 2021 | https://beritajatim.com/perumdam-tirta-pandalungan-baru-layani-13-kecamatan-di-jember |
| Target SR Bupati | "43.000 pelanggan… saya ingin **100.000 pelanggan pada 2027**" (Bupati Hendy) | Ags 2022 | jemberkab.go.id post id 100051 |

**Cakupan populasi:** 264.174 / 2.584.233 = **±10,2% penduduk terlayani**; atau 264.174 / 1.032.013 = **±25,6% dari penduduk di wilayah pelayanan** (2023). **Konflik definisi:** LK melaporkan dua angka populasi berbeda ("penduduk terlayani" 264 rb vs "penduduk di daerah pelayanan" 1,03 jt) — gunakan kedua interpretasi dalam analisis.

**Target vs realisasi SR:** Bupati Hendy (Agustus 2022) mengatakan "43.000 pelanggan" dan menargetkan **100.000 SR pada 2027** → realisasi 31 Des 2023 hanya **44.029 SR** → gap strategis (hanya +1.029 SR dari target baseline, perlu ~+14.000 SR/tahun untuk capai 2027). Ini adalah isu utama yang diangkat DPRD.

---

## 2. KAPASITAS & INFRASTRUKTUR PRODUKSI

| Indikator | 2022 | 2023 | Sumber |
|---|---|---|---|
| Kapasitas terpasang | 495,00 ltr/dtk | **510,00 ltr/dtk** | LK BUMD |
| Kapasitas produksi | 488,40 ltr/dtk | **495,90 ltr/dtk** | LK BUMD |
| Produksi air | 9.870.157 m³ | **9.791.778 m³** | LK BUMD |
| Distribusi | 9.620.782 m³ | **9.543.593 m³** | LK BUMD |
| Air terjual | 7.519.490 m³ | **7.560.828 m³** | LK BUMD |

**Catatan satuan:** LK BUMD menggunakan **liter/detik** untuk kapasitas (510 ltr/dtk ≈ 0,51 m³/detik ≈ 44.064 m³/hari kapasitas terpasang, 2023). Rasio air terjual/produksi 2023 = **77,2%**.

**Unit produksi (dari rincian aset LK 2023 & berita):**
- **IPA Wirolegi**, **IPA Tegal Gede**, **IPA Tegal Besar** (dana PM TA2004 Rp5 M + TA2005 Rp1 M), **IPA PPI Puger (Balung)**, **IPA Ajung** (PAPBD 2019)
- **Sumber Darungan (Tanggul)** — sumber air permukaan; pipanya putus tergerus banjir Des 2018 (700 pelanggan terdampak)
- Reservoir: **Sumber Telas (Panti)**, **Semeru**, **Kaca Piring**
- Sumur bor: **P22 Argopuro**, **P11 Condro**, **P.07** (perizinan pipa), sumur bor baru **Jl. Sentot** 2023 (T1 Rp90,3 jt + T2 Rp108,3 jt + T3 Rp144,5 jt)
- **15 sumur bor** dimatikan di musim hujan / diaktifkan saat kemarau
- **Sumber mata air Karangpring** (Sukorambi) — lahan strategis, gedung Perumdam di sampingnya mangkrak 2 tahun (2022)
- Aset hibah APBN: pipa distribusi Perumahan Graha Citra Mas/Bumi Tegal Besar (2010, Rp592,8 jt); instalasi transmisi & distribusi + jembatan pipa **IKK Patrang** (2014, Rp1,13 M)

**Jumlah IPA:** LK menyebut nama 5 IPA (Wirolegi, Tegal Gede, Tegal Besar, PPI Puger/Balung, Ajung) — **jumlah pasti IPA & lokasi lengkap sumur bor/mata air: TIDAK DITEMUKAN** (tidak ada daftar terpusat di dokumen yang dapat diakses).

---

## 3. JARINGAN PIPA & DISTRIBUSI

- **Panjang jaringan pipa (km): TIDAK DITEMUKAN** — tidak tercantum di LK BUMD (yang ada hanya **nilai aset** Instalasi Transmisi & Distribusi **Rp93,18 M** per 31 Des 2023, naik dari Rp90,7 M; Penyusutan Rp2,77 M/thn) maupun di berita/portal yang dapat diakses.
- **Nilai aset 31 Des 2023:** Instalasi Sumber Rp6,49 M · Instalasi Pompa Rp16,72 M · Instalasi Pengolahan Rp31,69 M · Instalasi Transmisi & Distribusi **Rp93,18 M** · Tanah Rp1,83 M.
- Cakupan: **13 dari 31 kecamatan** (Okt 2021); ekspansi desa via program pedesaan (lihat #9).
- **Penyambungan liar:** (Des 2018) pipa Paralon ilegal terbongkar dari dua makam di Jember → indikasi praktik sambungan liar.
- Gangguan jaringan: pipa Sumber Darungan putus (Des 2018, 700 pelanggan); Jl. Sultan Agung ambrol Mar 2020 (akses PDAM ke **150 rumah** macet; dari 3.000 rumah terdampak; 4 truk tangki 30 rit).

---

## 4. NON REVENUE WATER (NRW)

| Indikator | 2022 | 2023 | Sumber |
|---|---|---|---|
| Air hilang dari produksi | 249.375 m³ (2,53%) | 249.185 m³ (**2,53%**) | LK BUMD |
| Air hilang dari distribusi | 1.778.799 m³ | 1.982.765 m³ | LK BUMD |
| **% air hilang distribusi (proxy NRW)** | **18,49%** | **20,78%** | LK BUMD |
| Air hilang yg dapat dipertanggungjawabkan | 322.493 m³ | 381.655 m³ | LK BUMD |

**Tren: NRW memburuk** dari 18,49% (2022) → **20,78% (2023)**, dan absolutnya bertambah ~204 ribu m³. Ini kinerja **kelas sedang** (BPPSPAM: A <20%, B 20–25% — namun sumber KemenPU tidak dapat diverifikasi).
**Tren program:** Fraksi **PKS DPRD Jember** secara eksplisit meminta direksi baru fokus **penurunan NRW**, perluasan cakupan layanan & kualitas (raperda pembaruan Perumdam, Juni 2026 → per 20 Juli 2026 direksi baru dilantik).
**Aksi terkait:** penggantian meter 2023 **4.539 SR**, ditera **9.143 SR**.

---

## 5. KINERJA PELAYANAN (IKM/SKM, SPM, PENGADUAN)

| Indikator | 2022 | 2023 | Sumber |
|---|---|---|---|
| Pengaduan | 2.877 | **3.405** | LK BUMD |
| Penyelesaian pengaduan | 2.874 | **3.294** | LK BUMD |
| % penyelesaian | 99,9% | **96,7%** | hitung dari LK |

- **SKM/CSI Bidang Air Bersih (Kab. Jember):** **CSI 74,61 — kategori "Kurang Baik"** · 159 responden · performance 2,98 vs importance 3,33 (GAP −0,35) · atribut terbaik: biaya/retribusi **89,45 (sangat baik)**; terlemah: kecepatan penanganan kendala **66,33**; prosedur **70,85**. Tahun data 2021. Sumber: dokumen SKM Bidang PU & Perhubungan 2020/2021 Pemkab Jember (Google Drive via jemberkab.go.id/skm2021/).
- **Tekanan air:** **35.359 SR (80,3% dari 44.029) mendapat tekanan >0,7 bar** (2023); 34.923 SR (2022).
- **Jam pelayanan:** **TIDAK DITEMUKAN** angka eksplisit (mis. 24 jam). Yang terdokumentasi: saat kemarau pasokan **bergiliran** di pusat kota Jember (beritajatim, "Kemarau, PDAM Jember Pasok Air Bergiliran").
- **Pengaduan & kendala:** hanya **5 hidran** berfungsi dari 9 di kota (damkar) — konteks mitigasi, bukan layanan PDAM.

---

## 6. KUALITAS AIR

| Indikator | 2022 | 2023 | Sumber |
|---|---|---|---|
| Sampel uji kualitas air | 612 | **648** | LK BUMD |
| Sampel memenuhi syarat | 577 (94,3%) | **624 (96,3%)** | LK BUMD |

- **Sertifikasi air minum layak konsumsi (Kemenkes / pilot program nasional): TIDAK DITEMUKAN** untuk Perumdam Tirta Pandalungan di sumber yang dapat diakses. Yang tersedia: uji sampel internal di atas (96,3% memenuhi syarat, 2023).
- Pengeluaran "Sertifikasi ISO dan Sistem Informasi Manajemen" tercatat di LK (komitmen kualitas) — namun peringkat sertifikat/akreditasi lab **TIDAK DITEMUKAN**.

---

## 7. BPPSPAM (KEMENPU) — TIDAK DITEMUKAN

**Rating BPPSPAM 2018–2024: TIDAK DITEMUKAN.** Penyebab: domain `aplikasi.bppspam.kim.pu.go.id` & `pu.go.id/ppspamsip` **gagal resolusi DNS** dari lingkungan riset (diverifikasi berulang dengan curl dan WebFetch; `getaddrinfo failed`). Karena itu **tidak ada data peringkat (A/B/C/D/E) yang dapat dilaporkan** — dan untuk lomba, harus diakui sebagai keterbatasan, bukan diasumsikan.

**Indikator audit yang tersedia dari sumber lain:**
- **KAP auditor: opini "Wajar Tanpa Pengecualian"** untuk tahun buku 2020 (disampaikan audiensi 2/10/2021; KAP memeriksa, BPKP menghitung kinerja) — https://beritajatim.com/dprd-jember-desak-perumdam-tirta-pandalungan-diaudit-menyeluruh
- **BPKP 2021: terjadi penurunan pencapaian nilai kinerja**, baik dihitung dengan aturan BPPSPAM maupun Permendagri 47/1999 → **sinyal rating BPPSPAM yang menurun** (namun peringkat hurufnya tidak dipublikasikan dalam artikel).
- Inspektorat menemukan temuan; Fraksi "Pandekar" DPRD mendesak **audit menyeluruh**; **PM Rp25 M (APBD 2021) dibatalkan** akibatnya.
- **LK BUMD TA2022 & TA2023 sudah diaudit** (diterbitkan di portal jemberkab Oktober 2023 & September 2024). LK TA2025 terupload September 2026 tetapi **file hasil scan (1 halaman cover saja yang dapat dibaca)** → data operasional 2024/2025 tidak dapat diekstrak: http://www.jemberkab.go.id/wp-content/uploads/2026/09/11.-LK-KOMPLIT-AUDITED-PDAM-JEMBER-dan-PDP-Kahyangan-Jember-2025.pdf

---

## 8. PPSPAM/SIP PDAM, BPS, RIPAM — SEBAGIAN BESAR TIDAK DITEMUKAN

- **PPSPAM/SIP PDAM (KemenPU): TIDAK DITEMUKAN** (domain pu.go.id tidak reachable, sama dengan #7).
- **BPS Jember (Jember Dalam Angka) statistik air minum: TIDAK DITEMUKAN** (situs Next.js, data tabel tidak dapat diekstrak).
- **RIPAM Kabupaten Jember: TIDAK DITEMUKAN** (tidak ditemukan dokumen publik di jemberkab/JDIH/Google Drive Pemkab).
- **Data pendamping (konteks regional, BPS Jatim via beritajatim):** Produksi air bersih **Jawa Timur 810,68 juta m³/tahun — tertinggi se-Indonesia** (Indonesia 5,25 miliar m³; DKI 643,07; Jateng 619,17; Jabar 514,2 juta m³). Tahun data 2021, dirilis Feb 2023. Sumber: https://beritajatim.com/produksi-air-bersih-jatim-tertinggi-se-indonesia-ini-harapan-khofifah
- **Penembusan pasar PDAM & inflasi:** kenaikan tarif air PDAM masuk kelompok penyumbang inflasi tahunan Jember **7,39%** (Des 2022, BPS Jember) — https://beritajatim.com/tarif-air-pdam-dan-rokok-ikut-bikin-inflasi-tahunan-jember-739-persen

---

## 9. PROYEK BESAR & PEMBIAYAAN (APBD/APBN/DAK/HIBAH)

**A. Penyertaan Modal (PM) APBD Kab. Jember ke Perumdam (riwayat, dari LK & berita):**

| Tahun | PM | Sumber |
|---|---|---|
| 2018 | Rp7 M | https://beritajatim.com/pdam-jember-minta-rp-10-m-untuk-apa-saja |
| 2019 | **Rp10 M** (PAPBD 2019) — untuk IPA Ajung, 1.000 SR gratis, jaringan | beritajatim, idem |
| 2020 | Rp15 M | LK BUMD 2023 (catatan penyertaan modal) |
| 2021 | **Rp25 M — DI BATALKAN** setelah desakan audit | https://beritajatim.com/dprd-jember-desak-perumdam-tirta-pandalungan-diaudit-menyeluruh |
| 2022–2027 | program sambungan gratis 2018–2022 (PM Rp7/10/15/25/30 M) | beritajatim |
| Belum ditetapkan status | **Rp41.324.023.201** | LK BUMD 2023 |

**B. Hibah APBN:** **2.000 SR gratis** (skema reimburse, PIU Dinas PU Cipta Karya) — Direktur Adi Setiawan, 2019. Sengketa: Fraksi PKS mempertanyakan janji ganti dana pendamping Rp7 M APBD yang belum realisasi pusat (https://beritajatim.com/pks-pertanyakan-janji-dirut-pdam-jember).

**C. DAK 2026 (Kemenkeu) untuk Jember — total Rp140,823 M, termasuk:**
- **DAK Air Minum–Stunting: Rp3,184 M**
- DAK Sanitasi: Rp2,975 M
- Sumber: https://beritajatim.com/pemerintah-pusat-gelontorkan-dana-alokasi-khusus-rp-140-m-untuk-jember (27/9/2025)

**D. Proyek ekspansi pedesaan (DPRKPCK / Dana Desa, Nov 2025):**
- **SPAM Sukowiryo** — sumur bor 100 m
- **Karangpring** — 295 lonjor pipa SNI (125 → 250 RT)
- **Klungkung** — 290 lonjor pipa + penangkap mata air (70 → 200 rumah)
- **Sumber Bulus, Ledokombo** — 700 SR → target 1.000 SR
- Sumber: http://www.jemberkab.go.id/dari-kekeringan-ke-aliran-lancar-dprkpck-jember-percepat-infrastruktur-air-bersih-di-sukowiryo-dan-karangpring/ dan http://www.jemberkab.go.id/dprkpck-jember-percepat-peningkatan-infrastruktur-air-bersih-di-wilayah-pedesaan/

**E. Pamsimas:** sistem Pamsimas desa **mati sejak April 2026** (contoh kasus di wilayah Jelbuk) — gap layanan yang harus diisi Perumdam.

**F. Rencana strategis pemkab:** raperda pembaruan Perumdam (Jun 2026) — PKS minta fokus **NRW + cakupan layanan + kualitas**.

**G. Target PAD:** Bupati Hendy menargetkan **PAD Rp10 M/tahun dari Perumdam** (Jan 2022) — vs realisasi setoran PAD **Rp1,25 M (2023), Rp1,0 M (2022)**. Juga target umum Bupati: PAD Jember dari Rp700 miliar → Rp2,5 triliun (Maret 2021, rapat BUMD).

---

## 10. WILAYAH TERPELU & RAWAN KEKERINGAN

**A. Cakupan: hanya 13 dari 31 kecamatan** (Okt 2021) → lebih dari separuh wilayah tidak terlayani Perumdam.

**B. Desa rawan kekeringan:**
- **32 desa di 15 kecamatan** rawan kekeringan (Jul 2023, RPJMD). https://beritajatim.com/ada-32-desa-di-jember-rawan-kekeringan
- **11 kecamatan** rawan kekeringan menurut **RPJMD**: **Patrang, Jelbuk, Arjasa, Bangsalsari, Tanggul, Sumberbaru, Panti, Sumbersari, Tempurejo, Pakusari, Silo** (Kemiri tidak disebut di RPJMD, namun masuk klaster berita kekeringan 2026).
- Mitigasi: **+10 sumur bor** di Perubahan APBD 2023 (existing 2). https://beritajatim.com/pemkab-jember-siapkan-10-sumur-bor-untuk-atasi-kekeringan

**C. Kondisi kritis 2026 (puncak kemarau):**
- **SK Bupati No. 100.3.3.2/206/1.12/2026 — status siaga darurat kekeringan**
- **1,3 juta liter air** sudah disalurkan; **2.300 KK** terdampak **hingga akhir November 2026**
- Wilayah terdampak: **Kaliwining (Rambipuji), Patrang, Baratan, Jatian (Pakusari), Banjarsari (Bangsalsari), Tegal Gede, Antirogo, Mrawan, Kalisat, Silo, Jelbuk** (sistem Pamsimas mati sejak April 2026)
- Distribusi air bersih ke-**12** di Kalisat (Ags 2026); Mrawan 80 KK dapat 5.000 liter (sumur mengering)
- Sumber: http://www.jemberkab.go.id/bpbd-jember-salurkan-13-juta-liter-air-kekeringan-masih-melanda-2-300-kk-hingga-akhir-november/ (7/10/2026) · http://www.jemberkab.go.id/tanggap-darurat-kekeringan-bpbd-jember-gencarkan-distribusi-air-bersih-ke-sejumlah-kecamatan/

**D. Program "Air Bersih" Pemkab Jember:** berupa respon tanggap darurat BPBD (truk tangki), **sumur bor darurat** (15 sumur bor aktif saat kemarau), program sambungan gratis 2018–2022, proyek SPAM desa 2025 (lihat #9D). **Program "Air Bersih" khusus yang terdokumentasi mentargetkan desa tanpa akses: TIDAK DITEMUKAN dalam bentuk dokumen program tunggal** — hanya melalui gabungan DAK Air Minum, dana desa & program sambungan gratis.

---

## 11. KEUANGAN (KONTEKS BUSINESS CASE)

| Indikator | 2022 | 2023 | Sumber |
|---|---|---|---|
| Pendapatan air | Rp45,61 M | **Rp55,13 M (+20,9%)** | LK BUMD |
| Pendapatan non-air | Rp3,30 M | Rp4,03 M | LK BUMD |
| Pendapatan usaha | Rp48,92 M | **Rp59,16 M** | LK BUMD |
| Laba tahun berjalan | Rp4,39 M | **Rp7,69 M** | LK BUMD |
| Margin laba | 9,0% | **13,0%** | hitung dari LK |
| Setoran PAD | Rp1,0 M | Rp1,25 M | LK BUMD |
| Harga jual air + beban tetap | Rp6.044/m³ | **Rp7.067/m³** | LK BUMD |
| Harga jual murni | Rp4.611/m³ | Rp5.620/m³ | LK BUMD |
| HPP | Rp4.400/m³ | **Rp5.233/m³** | LK BUMD |
| Margin jual-HPP | +Rp213/m³ | **+Rp387/m³** | hitung dari LK |

**Bagi hasil (per Perda 4/1975):** PAD 55% · Cadangan Umum 20% · Dana Sosial & Pendidikan 10% · Dana Pensiun 5% · Jasa Produksi 10%.

---

## 12. TATA KELOLA & POLITIK (berguna untuk analisis case)

- **Ags 2022 — direksi dilantik** (15/8/2022): Dirut **Miftahur Ridho**, Dir. Teknik **Bagus Andi Puspito**, Dir. Umum **Yudho Radityo Utomo**; masa jabatan seharusnya berakhir 15 Agustus 2027. Dewas (6 orang: 3 Perumdam, 3 Kahyangan) juga dilantik Agu 2022. Sumber: http://www.jemberkab.go.id/pelantikan-dewan-pengawas-perumda-perkebunan-kahyangan-dan-perumdam-tirta-pandalungan-jember/
- **Des 2025 — Bupati Muhammad Fawait** (via Kepala Bapenda Achmad Imam Fauzi) **meminta seluruh direksi mengundurkan diri** paling lambat akhir Des 2025 (Dewas Farid Wajdi menolak membuat surat pengunduran). https://beritajatim.com/kepala-bapenda-jember-minta-direksi-dua-bumd-mengundurkan-diri
- **20 Jul 2026 — direksi baru dilantik**: Dirut **Ardani Yusuf**, Umum **Rofiih**, Teknis **Rendra Wirawan**; Bupati Fawait beri waktu **2 pekan** untuk menunjukkan progres (khususnya NRW, cakupan, kualitas). https://beritajatim.com/bupati-fawait-beri-waktu-2-pekan-kepada-direksi-baru-perumdam-jember
- **Riwayat:** seleksi direksi dibuka Januari 2022 (Plt. Direktur M. Syafii). Direktur lama: **Adi Setiawan** (2019).
- LKPJ Bupati: angka kemiskinan Jember 2023 di peringkat 18 se-Jatim (dari peringkat 2 di 2022); pengangguran terbuka menjadi prioritas DPRD → konteks tekanan politis untuk ekspansi layanan air murah.

---

## 13. RINGKASAN KETERBUTUHAN DATA (label jujur)

**Data yang TIDAK DITEMUKAN di sumber yang dapat diakses dari lingkungan ini:**
1. Peringkat BPPSPAM (A/B/C/D/E) 2018–2024 — **domain KemenPU tidak resolve (DNS fail)**; hanya indikator tidak langsung: BPKP 2021 mencatat **penurunan nilai kinerja** (aturan BPPSPAM & Permendagri 47/1999), KAP 2020 **WTP**
2. Data PPSPAM / SIP PDAM KemenPU — **domain tidak dapat diakses**
3. Tabel "Jember Dalam Angka" (BPS) bidang air minum — situs Next.js tidak dapat diekstrak
4. RIPAM Kabupaten Jember — tidak ditemukan dokumen publik
5. **Panjang jaringan pipa (km)** — tidak ada di LK (hanya nilai aset Rp93,18 M)
6. Sertifikasi air minum layak konsumsi Kemenkes / pilot — hanya uji internal 648 sampel/624 memenuhi syarat (96,3%, 2023)
7. Jam pelayanan eksplisit (24 jam?) — hanya "bergiliran" saat kemarau
8. Jumlah pasti IPA & koordinat lengkap sumur bor (nama terkuMPI 5 IPA: Wirolegi, Tegal Gede, Tegal Besar, PPI Puger/Balung, Ajung)
9. Data operasional 2024/2025 (LK 2025 hasil scan, tidak dapat diekstrak)

**Konflik angka antar sumber (sebutkan semuanya dalam analisis):**
- Pelanggan per Agu 2022: **43.000** (Bupati, lisan) vs **43.654** (LK per 31 Des 2022) vs **44.029** (LK per 31 Des 2023)
- Populasi: **2.584.233** total vs **264.174 terlayani** vs **1.032.013 di daerah pelayanan** (LK 2023) → coverage 10,2% atau 25,6% tergantung definisi
- NRW distribusi: **18,49% (2022) → 20,78% (2023)** (membaik? tidak — memburuk)
- Kinerja: BPKP 2021 menilai **turun**, namun CSI SKM 2021 74,61 "kurang baik" sudah buruk sebelumnya → tren menurun konsisten
- Target PAD **Rp10 M** vs realisasi **Rp1,25 M** (2023) → gap 8×
- Target SR **100.000 (2027)** vs realisasi **44.029 (2023)** → perlu ~3× lipat dalam 4 tahun

**Prioritas source paling kuat untuk dipakai di lomba:** Laporan Keuangan BUMD Jember TA2022 & TA2023 (jemberkab.go.id, PDF) — data audited, multi-tahun, lengkap (SR, NRW, kapasitas, kualitas, tekanan, pengaduan, tarif, HPP). Semua angka di atas bersumber dari sana kecuali yang sudah dicantumkan link-nya.

---
**Daftar URL utama:**
- LK audited TA2023: http://www.jemberkab.go.id/wp-content/uploads/2024/09/26.-LK-BUMD-2023.pdf
- LK audited TA2022: http://www.jemberkab.go.id/wp-content/uploads/2023/10/Laporan-Keuangan-BUMD-Perusahan-Daerah.pdf
- LK 2025 (scanned): http://www.jemberkab.go.id/wp-content/uploads/2026/09/11.-LK-KOMPLIT-AUDITED-PDAM-JEMBER-dan-PDP-Kahyangan-Jember-2025.pdf
- Berita kekeringan 2026: http://www.jemberkab.go.id/bpbd-jember-salurkan-13-juta-liter-air-kekeringan-masih-melanda-2-300-kk-hingga-akhir-november/
- SKM 2021 (Google Drive via jemberkab.go.id/skm2021/)
- beritajatim.com (URL per artikel dicantumkan di bagian terkait)
