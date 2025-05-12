# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Domain Proyek
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 
Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.
Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. 

### Permasalahan Bisnis
Berdasarkan latar belakang perusahaan **Jaya Jaya Maju**, berikut adalah 3 permasalahan utama yang perlu dianalisis untuk membantu manajer HR dalam mengelola tingkat attrition yang tinggi:

 1. Apa saja faktor-faktor yang mempengaruhi tingginya attrition rate di perusahaan?
 2. Bagaimana perbedaan tingkat attrition berdasarkan jenis kelamin, usia, atau status pernikahan?
 3. Menggunakan Model apa yang relevan untuk mengidentifikasi prediksi karyawan yang keluar dari perusahaan?
 4. Bagaimana cara menampilkan hasil analisis yang mudah dipahami oleh HRD?

### Cakupan Proyek
Berdasarkan permasalahan bisnis yang telah dijabarkan, proyek ini akan mencakup beberapa aspek analisis dan implementasi sebagai berikut:
1. **Analisis Faktor-Faktor yang Mempengaruhi Tingginya Attrition Rate**  
   - Melakukan eksplorasi terhadap data perusahaan untuk mengidentifikasi faktor-faktor yang mempengaruhi tingkat attrition karyawan. Faktor-faktor tersebut dapat meliputi keseimbangan kehidupan kerja, kepuasan kerja, overtime, tingkat keterlibatan kerja, status pekerjaan, dan lainnya.
2. **Analisis Perbedaan Tingkat Attrition Berdasarkan Demografi**  
   - Mengelompokkan dan membandingkan tingkat attrition berdasarkan **jenis kelamin**, **usia**, dan **status pernikahan** karyawan untuk menemukan pola yang relevan dan untuk menentukan apakah faktor-faktor demografis mempengaruhi tingkat keluar-masuknya karyawan.
3. **Pembangunan Model Prediksi untuk Identifikasi Karyawan yang Keluar**  
   - Membangun model prediksi menggunakan teknik seperti **Logistic Regression**, **Decision Trees**, atau **Random Forest** untuk mengidentifikasi karyawan yang berisiko keluar dari perusahaan berdasarkan faktor-faktor yang telah dianalisis.
4. **Penyajian Hasil Analisis dalam Bentuk Dashboard yang Mudah Dipahami oleh HRD**  
   - Menyajikan hasil analisis dalam bentuk **dashboard interaktif** yang mudah dipahami oleh manajer HR. Dashboard ini akan menampilkan visualisasi yang jelas mengenai faktor-faktor penyebab attrition, prediksi karyawan yang berisiko keluar, dan perbandingan attrition berdasarkan kategori demografis.
## Persiapan

**Sumber Data**: [Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

#### Setup Environment:

```bash
# Install dependencies
pip install -r requirements.txt
```
### Membuka `notebook.ipynb`

1. Pastikan seluruh **dependensi** yang diperlukan telah terinstal dengan benar sesuai dengan daftar di `requirements.txt`.
    
2. Buka dan jalankan seluruh isi **`notebook.ipynb`** di Google Colab atau IDE Python yang mendukung notebook (misalnya Jupyter Notebook, VSCode).
    
3. Di dalam notebook ini, Anda akan melakukan analisis data, menemukan pola-pola yang relevan, dan mendapatkan **insight** terkait attrition karyawan berdasarkan berbagai faktor.
    
4. Setelah notebook berjalan, temukan visualisasi, statistik, dan insight yang diperoleh untuk memahami hubungan antara faktor-faktor penyebab tingginya attrition.

### Menjalankan `prediction.py`

1. Pastikan semua **dependensi** yang diperlukan sudah terinstal dengan benar sesuai `requirements.txt`.
    
2. **Jalankan `prediction.py`** di IDE lokal yang Anda gunakan, seperti **VSCode** atau IDE lainnya yang mendukung Python.
    
   **Script ini memuat**:
   - Fungsi preprocessing sederhana untuk menyesuaikan data dengan fitur yang digunakan model.
   - **Model** yang telah dilatih (`model_rf.pkl`) yang dimuat menggunakan **joblib**.
   - Pembuatan data baru yang dibuat secara acak untuk keperluan simulasi prediksi.
   - Prediksi untuk menentukan apakah karyawan akan **keluar** (Attrition: Yes) atau **bertahan** (Attrition: No).

3. Untuk menjalankan prediksi:
   - **Pastikan file `model_rf.pkl` berada di direktori yang sama** dengan script `prediction.py`.
   - **Jalankan file `prediction.py` di VSCode atau terminal**.
   - Hasil prediksi akan ditampilkan langsung di terminal atau konsol, dan prediksi tersebut juga akan ditambahkan ke data yang sudah ada.

### Menjalankan Dashboard

Untuk menjalankan dashboard secara lokal, Anda dapat menggunakan **Metabase**. Pastikan Anda sudah menginstal aplikasi **Docker** di perangkat Anda.

#### Langkah-langkah untuk menjalankan Metabase menggunakan Docker:

1. **Unduh image Metabase** dari Docker Hub dengan menjalankan perintah berikut:

    ```bash
    docker pull metabase/metabase:latest
    ```

2. **Jalankan container Metabase** dengan perintah berikut:

    ```bash
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```

3. **Login ke Metabase**:
    - Buka **[http://localhost:3000/setup](http://localhost:3000/setup)** di browser.
    - Gunakan kredensial berikut untuk login:
        - **Username**: root@mail.com
        - **Password**: root123

4. **Set up Business Dashboard**:
    - Setelah login berhasil, Anda dapat membuat dashboard interaktif untuk memonitor faktor-faktor yang mempengaruhi attrition rate, serta memvisualisasikan hasil analisis dan prediksi menggunakan Metabase.
    - Dashboard ini akan membantu manajer HR untuk memantau secara langsung faktor-faktor kunci dan tren yang berhubungan dengan tingkat keluar karyawan.



## Business Dashboard


### Ringkasan Dashboard
Dashboard ini memberikan gambaran visual yang jelas tentang faktor-faktor yang mempengaruhi keputusan karyawan untuk keluar dari perusahaan, dengan fokus pada analisis data karyawan yang ada di **Jaya Jaya Maju**. Dashboard ini menggabungkan beberapa grafik untuk menggambarkan **attrition** (tingkat keluar) berdasarkan berbagai fitur, seperti **Overtime**, **Usia**, **Jenis Kelamin**, dan **Status Pernikahan**.

### Faktor Utama
1. **Attrition Berdasarkan Overtime**:
   - Karyawan yang **sering overtime** lebih cenderung keluar dibandingkan dengan mereka yang tidak overtime.
   
2. **Attrition Berdasarkan Umur**:
   - Karyawan di kategori **Dewasa (26-45 tahun)** menunjukkan tingkat keluar yang lebih tinggi dibandingkan dengan kategori **Remaja (18-25 tahun)** dan **Paruh Baya (46-60 tahun)**.
   
3. **Attrition Berdasarkan Jenis Kelamin**:
   - Perbandingan **Jenis Kelamin** menunjukkan bahwa **Pria** memiliki lebih banyak karyawan yang keluar dibandingkan dengan **Wanita**.
   
4. **Attrition Berdasarkan Status Pernikahan**:
   - Karyawan yang berstatus **Divorced** dan **Single** memiliki tingkat keluar yang lebih tinggi dibandingkan dengan yang **Married**.

### Fitur yang Paling Berpengaruh Terhadap Keputusan Karyawan untuk Keluar dari Perusahaan
Berdasarkan hasil analisis di dashboard, berikut adalah **10 fitur yang paling berpengaruh** terhadap keputusan karyawan untuk keluar dari perusahaan:

1. **Overtime**:
   - Karyawan yang sering melakukan **overtime** memiliki kemungkinan keluar yang lebih tinggi, dengan persentase attrition yang signifikan di antara mereka yang bekerja lembur.

2. **JobSatisfaction**:
   - Karyawan dengan tingkat **kepuasan kerja rendah** lebih cenderung keluar. Kepuasan kerja yang tinggi membantu meningkatkan retensi.

3. **StockOptionLevel**:
   - Karyawan dengan **opsi saham rendah** atau tanpa opsi saham lebih cenderung keluar daripada yang memiliki opsi saham.

4. **EnvironmentSatisfaction**:
   - Kepuasan terhadap **lingkungan kerja** memiliki pengaruh besar. Karyawan yang tidak puas dengan lingkungan kerjanya lebih sering keluar.

5. **JobInvolvement**:
   - Karyawan dengan tingkat **keterlibatan kerja tinggi** lebih cenderung bertahan, sedangkan yang merasa kurang terlibat lebih cenderung keluar.

6. **YearsAtCompany**:
   - Karyawan yang lebih lama bekerja di perusahaan cenderung lebih loyal dan bertahan. Karyawan yang baru bekerja beberapa tahun lebih berisiko untuk keluar.

7. **WorkLifeBalance**:
   - Keseimbangan kerja dan kehidupan sangat mempengaruhi keputusan karyawan untuk tetap bertahan atau keluar.

8. **YearsWithCurrentManager**:
   - Hubungan yang baik dengan **manajer langsung** dapat mengurangi tingkat attrition, karyawan yang lebih lama dengan manajer yang sama lebih cenderung bertahan.

9. **JobLevel**:
   - Karyawan dengan **jabatan lebih tinggi** lebih cenderung bertahan di perusahaan, sementara posisi yang lebih rendah memiliki tingkat attrition yang lebih tinggi.

10. **BusinessTravel**:
   - Karyawan yang sering **pergi bisnis** atau **jarang** bepergian untuk pekerjaan lebih cenderung keluar dibandingkan dengan mereka yang tidak melakukan perjalanan bisnis sama sekali.

### Distribusi dan Pola Karyawan Keluar
- **Karyawan dengan Overtime** memiliki lebih banyak yang keluar (Attrition = 1.0) dibandingkan dengan yang tidak melakukan Overtime, dengan **29%** karyawan yang melakukan overtime keluar.
- **Karyawan Dewasa (26-45 tahun)** menunjukkan pola keluar yang signifikan dibandingkan kategori usia lainnya.
- **Jenis kelamin pria** lebih cenderung keluar, dengan grafik menunjukkan lebih banyak karyawan pria yang keluar dibandingkan wanita.
- Berdasarkan **status pernikahan**, kategori **Single** dan **Divorced** menunjukkan tingkat keluar yang lebih tinggi daripada yang sudah **Married**.

### Hasil Prediksi Menggunakan Random Forest

Berikut adalah perbandingan hasil prediksi untuk berbagai model yang digunakan dalam analisis ini:

| Model           | Accuracy | Precision | Recall  | F1 Score |
|-----------------|----------|-----------|---------|----------|
| **Decision Tree**| 0.764151 | 0.392157  | 0.512821| 0.444444 |
| **Random Forest**| 0.867925 | 0.720000  | 0.461538| 0.562500 |
| **SVM**          | 0.853774 | 0.633333  | 0.487179| 0.550725 |

- **Accuracy**: Model **Random Forest** memiliki **akurasi 86.79%**, yang menunjukkan bahwa model ini cukup baik dalam memprediksi karyawan yang akan keluar atau bertahan.
- **Precision**: **Random Forest** memiliki **precision 72%**, yang berarti 72% dari karyawan yang diprediksi akan keluar benar-benar keluar dari perusahaan, menunjukkan kinerja yang lebih baik daripada model lainnya.
- **Recall**: Model ini memiliki **recall 46.15%**, yang menunjukkan bahwa hampir setengah dari karyawan yang benar-benar keluar dapat diprediksi, namun masih ada ruang untuk perbaikan.
- **F1 Score**: **Random Forest** memiliki **F1 score 56.25%**, menunjukkan keseimbangan antara precision dan recall meskipun recall bisa ditingkatkan.


## Conclusion


### 10 Fitur yang Paling Berpengaruh Terhadap Attrition

Berdasarkan analisis data dan hasil prediksi yang dilakukan, berikut adalah **10 fitur yang paling berpengaruh** terhadap keputusan karyawan untuk keluar dari perusahaan (attrition):

1. **Overtime**: Karyawan yang sering overtime memiliki kemungkinan keluar yang lebih tinggi dibandingkan dengan mereka yang tidak melakukan overtime.
2. **JobSatisfaction**: Karyawan dengan tingkat kepuasan kerja rendah cenderung lebih cepat untuk keluar dari perusahaan.
3. **StockOptionLevel**: Karyawan yang tidak memiliki opsi saham atau memiliki opsi saham yang rendah lebih cenderung keluar.
4. **EnvironmentSatisfaction**: Kepuasan terhadap lingkungan kerja memainkan peran penting, dengan karyawan yang tidak puas lebih sering keluar.
5. **JobInvolvement**: Karyawan yang tidak terlibat dalam pekerjaannya cenderung lebih cepat untuk meninggalkan perusahaan.
6. **YearsAtCompany**: Karyawan yang lebih lama bekerja di perusahaan biasanya lebih loyal dan cenderung bertahan.
7. **WorkLifeBalance**: Keseimbangan antara kehidupan pribadi dan pekerjaan berpengaruh pada keputusan karyawan untuk tetap bertahan atau keluar.
8. **YearsWithCurrManager**: Karyawan yang memiliki hubungan baik dengan manajer mereka lebih cenderung bertahan di perusahaan.
9. **JobLevel**: Karyawan di level pekerjaan yang lebih rendah memiliki tingkat keluar yang lebih tinggi dibandingkan dengan karyawan di level yang lebih tinggi.
10. **MonthlyIncome**: Karyawan dengan gaji yang lebih tinggi memiliki kecenderungan untuk bertahan di perusahaan, sementara mereka dengan gaji lebih rendah cenderung keluar.

### Model Prediktif yang Dipilih

Setelah melakukan perbandingan antar model prediktif, **Random Forest** dipilih sebagai model terbaik berdasarkan performa yang diberikan oleh **Accuracy**, **Precision**, **Recall**, dan **F1 Score**. Berikut adalah alasan memilih model **Random Forest**:

- **Accuracy**: Model **Random Forest** memiliki akurasi tertinggi (**86.79%**), menunjukkan kemampuannya dalam mengklasifikasikan karyawan yang keluar dan bertahan dengan tepat.
- **Precision**: Dengan **precision 72%**, model ini berhasil memprediksi karyawan yang keluar dengan sangat baik.
- **Recall**: Meskipun **recall** model ini adalah **46.15%**, menunjukkan bahwa model ini mampu menangkap hampir setengah dari karyawan yang benar-benar keluar.
- **F1 Score**: **F1 score 56.25%** menunjukkan bahwa model ini memiliki keseimbangan yang cukup baik antara precision dan recall.

Karena kemampuan **Random Forest** dalam menangani dataset besar dan kompleks, serta kemampuannya untuk memberikan prediksi yang lebih stabil dan akurat, model ini menjadi pilihan utama untuk memprediksi karyawan yang berisiko keluar dari perusahaan.

### Rekomendasi Action Items

Berdasarkan hasil analisis dan model prediktif yang telah diterapkan, berikut adalah beberapa **rekomendasi tindakan** yang dapat dilakukan oleh manajer HR untuk mengurangi tingkat attrition karyawan:

1. **Mengelola OverTime**: Mengurangi tingkat **overtime** di antara karyawan, atau memastikan bahwa karyawan yang melakukan overtime mendapatkan kompensasi yang setimpal. Kelelahan akibat overtime dapat mempengaruhi keputusan karyawan untuk keluar dari perusahaan.
   
2. **Meningkatkan JobSatisfaction**: Menyusun program untuk meningkatkan **kepuasan kerja**, seperti melalui **pelatihan**, **penghargaan**, atau pengembangan karir yang lebih baik untuk meningkatkan retensi karyawan.

3. **Menawarkan Opsi Saham atau Insentif**: Menyediakan lebih banyak **opsi saham** atau insentif untuk karyawan agar mereka merasa lebih terikat dengan perusahaan, terutama pada level pekerjaan yang lebih rendah.

4. **Meningkatkan Lingkungan Kerja**: Memperbaiki **lingkungan kerja** dengan menciptakan suasana yang lebih positif dan mendukung kesejahteraan karyawan, yang dapat mengurangi tingkat **attrition**.

5. **Memperbaiki WorkLifeBalance**: Menyediakan fleksibilitas **work-life balance** untuk meningkatkan kebahagiaan dan produktivitas karyawan. Program seperti **kerja remote** atau **waktu liburan tambahan** dapat membantu.

6. **Meningkatkan Keterlibatan Kerja**: Meningkatkan tingkat **job involvement** karyawan melalui komunikasi yang lebih baik, pemberian tugas yang lebih bermakna, atau peran yang lebih terlibat dalam pengambilan keputusan.

7. **Program Pengembangan Karir**: Memberikan peluang pengembangan bagi karyawan yang lebih lama bekerja di perusahaan, sehingga mereka merasa dihargai dan lebih cenderung bertahan.

8. **Fokus pada Hubungan Manajer dan Karyawan**: Memperkuat hubungan antara **manajer dan karyawan** dengan pelatihan untuk manajer tentang cara memimpin secara efektif dan mendukung karyawan mereka.

9. **Tinjau Struktur Penggajian**: Memastikan bahwa **gaji dan tunjangan** yang diberikan sesuai dengan kinerja dan kebutuhan karyawan, serta kompetitif dengan perusahaan lain.

10. **Program Pemantauan Karyawan Berisiko**: Menggunakan model prediktif seperti **Random Forest** untuk memantau karyawan yang berisiko tinggi untuk keluar dan memberikan intervensi dini yang sesuai, seperti penyesuaian beban kerja atau peningkatan kepuasan kerja.
