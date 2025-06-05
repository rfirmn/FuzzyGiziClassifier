# Sistem Fuzzy Penentuan Kecukupan Gizi Balita Usia 7–10 Tahun

Proyek ini merupakan implementasi sistem logika fuzzy berbasis Python untuk menentukan tingkat **kecukupan gizi** pada balita usia 7 hingga 10 tahun. Sistem ini dikembangkan **tanpa menggunakan library fuzzy seperti `skfuzzy`**, melainkan dengan pendekatan **matematika manual** agar dapat memberikan pemahaman mendalam terhadap konsep fuzzy.

## 🧠 Tujuan

Tujuan utama dari sistem ini adalah:
- Memberikan alat bantu untuk menilai status kecukupan gizi balita berdasarkan beberapa parameter kesehatan.
- Mengilustrasikan penerapan logika fuzzy secara manual untuk keperluan edukatif maupun penelitian.
- Mempermudah analisis gizi menggunakan pendekatan berbasis rule (aturan) dan inferensi fuzzy.

## 📊 Parameter Masukan

Beberapa parameter yang digunakan dalam sistem ini meliputi:
- Berat badan
- Tinggi badan
- Usia
- Indikator lainnya yang berkontribusi terhadap penilaian status gizi

(Setiap parameter diasumsikan memiliki fungsi keanggotaan tersendiri seperti *kurus*, *normal*, *gemuk*, dll.)

## 🛠️ Fitur Utama

- **Fungsi Keanggotaan**:
  - `trimf`: Fungsi keanggotaan segitiga
  - `trapmf`: Fungsi keanggotaan trapesium
- **Inferensi Fuzzy Manual**:
  - Penentuan derajat keanggotaan setiap parameter
  - Penilaian berdasarkan aturan *if-then* (basis aturan fuzzy)
- **Defuzzifikasi** (jika diterapkan): untuk menghasilkan nilai crisp dari hasil fuzzy


## 📦 Ketergantungan

Pastikan Anda sudah menginstal pustaka berikut:

```bash
pip install numpy pandas scikit-learn
```

## 🚀 Cara Menjalankan

1. Buka file `.ipynb` menggunakan Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Jalankan seluruh sel dari atas ke bawah untuk melihat hasil evaluasi fuzzy.

## 📈 Output

Sistem akan mengklasifikasikan kecukupan gizi menjadi beberapa kategori seperti:
- Gizi kurang
- Gizi cukup
- Gizi lebih

Hasil evaluasi dapat ditampilkan dalam bentuk numerik maupun kualitatif, bergantung pada model defuzzifikasi.

## 🎯 Konteks Penggunaan

Sistem ini dapat digunakan untuk:
- Penelitian gizi anak
- Proyek akademik terkait sistem cerdas dan logika fuzzy
- Edukasi mengenai konsep fuzzy logic tanpa abstraksi library tingkat tinggi

## 👨‍💻 Pengembang

Proyek ini dibuat oleh **Rio**, mahasiswa Informatika dari Telkom University, sebagai bagian dari eksplorasi implementasi sistem pakar berbasis logika fuzzy.

## 📜 Lisensi

Proyek ini dilisensikan di bawah MIT License – silakan lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.
