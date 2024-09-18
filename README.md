URL PWS : http://aditya-dharma31-klikmart.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Membuat Sebuah Proyek Django Baru
Dalam hal ini saya membuat program Django bernama klikmart yang berada pada subdirektori bernama klikmart. Kemudian, saya hubungkan dengan repository di GitHub untuk memudahkan version control.
- Membuat aplikasi dengan nama main pada proyek tersebut
Menambahkan aplikasi main ke dalam proyek dengan melakukan perintah di CMD python manage.py startapp main. Kemudian, main didaftarkan ke dalam file setting.py proyek dibawah INSTALLED_APPS agar terhubung dengan proyek utama.
- Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Untuk menjalankan aplikasi main, kita perlu menambahkan file urls.py dalam proyek utama dan menambahkan rute untuk mengarahkan URL ke aplikasi main.

from django.urls import include, path
urlpatterns = [
    path('main/', include('main.urls')),  # Mengarahkan ke aplikasi main
]

- Membuat model product pada aplikasi main
Pada file models.py dalam aplikasi main, saya mendefinisikan Product dengan atribut name, price, dan description. Model ini akan digunakan untuk mempresentasikan produk dalam database.
- Membuat Fungsi di views.py untuk menampilkan data di template
Membuat fungsi show_info di file views.py yang dapat mengembalikan informasi nama aplikasi, npm, nama, dan kelas. Fungsi tersebut akan mengembalikan data ke dalam file template main.html
- Membuat routing di urls.py aplikasi main
Membuat file urls.py dalam aplikasi main dan menambahkan rute untuk memetakan show_info yang telah di buat dalam file views.py
- Melakukan deployment ke PWS
Setelah aplikasi selesai, kita melakukan deployment ke platform PWS. Kita perlu memastikan agar aplikasi dapat diakses melalui URL yang telah disediakan PWS.
- Membuat README.md
Membuat file README.md yang berisi tautan menuju aplikasi yang sudah di-deploy di PWS dan jawaban atas beberapa pertanyaan terkait.



2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!
![Bagan PBP](https://github.com/user-attachments/assets/5c5376da-98b2-4f31-a3a5-e062c1002a50)

Client melakukan request ->  urls.py (mencocokan URL) -> views.py (menjalankan logika aplikasi) -> models.py (mengambil data dari database) -> views.py (memproses data) -> Template (main.html) -> Respons kembali ke client.



3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah sebuah sistem kontrol versi terdistribusi (Distributed Version Control System, DVCS) yang sangat penting dalam pengembangan perangkat lunak. Berikut adalah beberapa fungsi utama Git dalam pengembangan perangkat lunak:

- Untuk Melakukan Kolaborasi
Git memfasilitasi kerja tim dengan memungkinkan banyak orang bekerja pada proyek yang sama tanpa khawatir akan merusak kode atau mencampurnya. Setiap pengembang dapat membuat perubahan pada kode sumber dan mengirimkannya ke repositori utama, sehingga semua anggota tim dapat melihat dan mengintegrasikan perubahan tersebut.
- Untuk Mengorganisir
Git memungkinkan penyimpanan proyek dalam folder berurutan seperti V1, V2, V3, dengan satu proyek yang menggunakan database khusus berisi semua versi file. Ini membuat mudah untuk melacak dan memulihkan versi kode sumber yang telah digunakan sebelumnya.
- Sebagai Proyek Open Source
Git adalah perangkat lunak open source yang dapat digunakan untuk pengembangan perangkat lunak secara terbuka. Ini memungkinkan komunitas pengembang untuk berkontribusi pada proyek dan membagikan kode sumber mereka dengan mudah.
- Sebagai Platform Fleksibilitas
Git dapat digunakan sebagai platform fleksibilitas dengan layanan hosting seperti Gitlab, GitHub, Bitbucket, dan SourceForge. Ini memungkinkan pengguna untuk menghosting berbagai proyek dan mengelola mereka secara efektif.
- Untuk Melakukan Backup
Git berfungsi sebagai salinan cadangan yang andal untuk kode sumber proyek. Jika terjadi kegagalan sistem atau data hilang, maka Anda masih bisa memulihkan kode sumber dari repositori. Ini memungkinkan pengembang untuk mengembalikan ke versi sebelumnya jika terjadi masalah pada versi terbaru.
- Efisiensi dan Fleksibilitas
Git dirancang dengan optimalitas kinerja, keamanan, dan fleksibilitas. Ini membuat Git sangat cepat dan efisien dalam mengelola perubahan pada kode sumber, bahkan untuk proyek yang sangat besar.

Dengan demikian, Git mempermudah pengembangan perangkat lunak dengan memberikan kemudahan dalam kolaborasi, pengelolaan versi, dan cadangan kode, serta fleksibilitas dalam hosting proyek.



4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena beberapa alasan yang membuatnya sangat relevan dan efektif untuk belajar pengembangan web. Berikut adalah beberapa alasan utama:

- Arsitektur MTV yang Terstruktur
Django menggunakan arsitektur MVT yang memisahkan logika bisnis, tampilan, dan database. Ini membuat pengembangan aplikasi web lebih terstruktur dan mudah dipahami, terutama bagi pemula. Arsitektur ini memungkinkan pengembang untuk fokus pada satu aspek aplikasi tanpa mengganggu aspek lainnya.
- Fitur Bawaan yang Kompleks
Django menyediakan Object-Relational Mapping (ORM) yang memungkinkan pengembang untuk berinteraksi dengan database menggunakan sintaks Python yang clean dan intuitif, tanpa perlu menulis perintah SQL manual. Ini memudahkan pengembang untuk mengelola database dengan cara yang lebih mudah dan efisien. Django juga memiliki panel admin yang kuat, memungkinkan pengembang untuk mengelola data aplikasi dengan antarmuka administrasi yang ramah pengguna. Fitur ini sangat berguna untuk pengembang yang ingin membuat aplikasi web yang dapat diadministrasi dengan mudah. Selain itu, Django memiliki sistem otentikasi yang kuat yang mendukung otentikasi pengguna, manajemen izin, dan sesi. Pengembang dapat dengan mudah menerapkan kontrol akses berbasis peran (RBAC) serta izin yang terperinci untuk mengatur akses ke bagian sensitif aplikasi.
- Keamanan yang Kuat
Django menawarkan proteksi bawaan terhadap kerentanan web yang umum seperti injeksi SQL, XSS (Cross-Site Scripting), CSRF (Cross-Site Request Forgery), dan clickjacking. Perlindungan ini terintegrasi langsung ke dalam inti kerangka kerja, mengurangi potensi risiko keamanan. Django juga menyediakan utilitas untuk mengelola kata sandi pengguna secara aman, termasuk proses hashing, pengasinan, dan validasi. Fitur ini membantu mencegah kerentanan keamanan terkait dengan kata sandi, seperti serangan brute force dan kebocoran kata sandi.
- Komunitas Aktif dan Dukungan
Django memiliki komunitas yang sangat aktif dan mendukung, dengan banyak sumber daya dan dokumentasi yang tersedia. Ini membuat proses belajar lebih mudah dan efektif karena pengembang dapat menemukan banyak contoh, tutorial, dan solusi masalah yang telah dihadapi oleh komunitas lain.
- Skalabilitas Tinggi
Django dirancang untuk membangun aplikasi web yang skalabel. Fitur-fitur bawaan seperti sistem routing URL dan fitur-fitur lainnya memungkinkan pengembang untuk membuat aplikasi web yang dapat menangani banyak permintaan klien dengan baik.
- Pengembangan yang Cepat
Arsitektur MVT dan fitur-fitur bawaan lainnya membantu pengembang untuk menyelesaikan pekerjaan lebih cepat dan efisien. Penggunaan API, library, dan modul yang tersedia juga mempercepat proses pengembangan
- Penggunaan dalam Proyek Nyata
Django telah digunakan dalam proyek-proyek nyata seperti Instagram, National Geographic, Spotify, Mozilla, dan Pinterest. Ini menunjukkan bahwa Django dapat digunakan dalam berbagai jenis proyek, dari media berita hingga platform media sosial dan e-commerce

Dengan demikian, Django dianggap sebagai permulaan yang baik karena kemudahan penggunaannya, fitur-fitur yang kompleks, komunitas yang mendukung, skalabilitas tinggi, keamanan yang kuat, dan pengembangan yang cepat. Semua ini membuat Django sangat relevan dan efektif untuk belajar pengembangan web.



5. Mengapa model pada Django disebut sebagai ORM?

ORM adalah teknologi yang memetakan objek dalam bahasa pemrograman (seperti Python) ke struktur data dalam basis data relasional (seperti SQLite, PostgreSQL, MySQL). Ini memungkinkan pengembang untuk mengelola data menggunakan sintaks Python, bukan SQL. ORM menggunakan Queryset untuk mengelola data. Queryset adalah daftar objek yang dapat di-filter, di-arrange, dan di-manage untuk memudahkan pengembang dalam mengakses dan mengelola data

Model pada Django disebut sebagai Object-Relational Mapping (ORM) karena fitur ini memungkinkan pengembang untuk berinteraksi dengan database menggunakan sintaks Python yang clean dan intuitif, tanpa perlu menulis perintah SQL manual. Berikut adalah beberapa alasan utama:

- Interaksi dengan Database
Dengan ORM, pengembang dapat membuat model yang mewakili struktur data dalam basis data. Model ini kemudian digunakan untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data menggunakan sintaks Python tanpa perlu menulis kode SQL manual.
- Abstraksi Tingkat Tinggi
ORM memberikan abstraksi tingkat tinggi dari SQL, memungkinkan pengembang untuk fokus pada logika bisnis dan aplikasi tanpa harus memikirkan detail SQL. Ini membuat pengembangan lebih cepat dan lebih mudah.
- Kemudahan Penggunaan
Model pada Django dapat dibuat dengan mudah menggunakan kelas Python yang mengextends dari models.Model. Setiap atribut kelas ini mewakili field dalam basis data, sehingga pengembang dapat mengelola data dengan cara yang intuitif. Hubungan antar model Django ORM juga menyederhanakan pengelolaan hubungan antar model, seperti one-to-one, one-to-many, dan many-to-many. Ini membuat pengembang dapat mengelola kompleksitas database dengan lebih mudah.

Dengan demikian, model pada Django disebut sebagai ORM karena fitur ini memungkinkan pengembang untuk berinteraksi dengan database menggunakan sintaks Python yang clean dan intuitif, serta memberikan abstraksi tingkat tinggi dari SQL yang memudahkan pengembangan aplikasi web.





1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery adalah proses pengiriman data yang efektif dan efisien dalam pengimplementasian sebuah platform. Berikut beberapa alasan mengapa data delivery diperlukan:

- Efisiensi Operasional
Data delivery memungkinkan pengiriman data yang cepat dan akurat, sehingga memudahkan pengelolaan operasional. Contohnya, dalam sistem pengiriman barang, data delivery dapat menyajikan informasi real-time tentang status pengiriman, seperti lokasi dan waktu kedatangan, sehingga memperbaiki kepuasan pelanggan dan meningkatkan efisiensi logistik.
- Transparansi dan Akuntabilitas
Data delivery memungkinkan transparansi dalam proses pengiriman data. Contohnya, dalam platform pembayaran pemerintah, data delivery dapat menyajikan informasi transaksi secara digital, meminimalkan biaya penyimpanan dokumen, dan meningkatkan akuntabilitas dalam proses pembayaran.
- Penggunaan Teknologi yang Efektif
Data delivery seringkali menggunakan teknologi seperti IoT (Internet of Things) dan platform seperti Google Cloud Pub/Sub, yang memungkinkan pengiriman data dalam skala besar dengan keandalan tinggi. Contohnya, dalam implementasi IoT oleh Antares, data delivery memungkinkan pengiriman data real-time tentang kebocoran air, meminimalisir kebocoran dan meningkatkan efisiensi pengelolaan air minum.
- Pengurangan Biaya
Data delivery dapat mengurangi biaya operasional dengan mengurangi kebutuhan untuk dokumen fisik dan kurir. Contohnya, dalam implementasi platform pembayaran pemerintah, data delivery memungkinkan transaksi digital tanpa media kertas, mengurangi biaya penyimpanan dokumen dan kurir.
- Peningkatan Kualitas Layanan
Data delivery memungkinkan penyajian informasi yang akurat dan real-time, sehingga meningkatkan kualitas layanan. Contohnya, dalam sistem pengiriman barang, data delivery dapat memberikan ETA (Estimated Time of Arrival) yang akurat, memudahkan pengambilan keputusan dan meningkatkan kepuasan pelanggan.

Dengan demikian, data delivery adalah komponen penting dalam pengimplementasian sebuah platform karena memungkinkan efisiensi operasional, transparansi, akuntabilitas, penggunaan teknologi yang efektif, pengurangan biaya, dan peningkatan kualitas layanan.



2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut analisis dari sumber-sumber yang disediakan, JSON lebih baik dan lebih populer dibandingkan XML karena beberapa alasan berikut:
- Simplicity dan Kompatibilitas
JSON memiliki sintaks yang lebih sederhana dan mudah dibaca, membuatnya lebih fleksibel dan mudah digunakan dalam berbagai konteks, terutama dalam pengembangan web dan aplikasi seluler. XML, meskipun memiliki kelebihan dalam struktur dokumen yang kompleks, memiliki sintaks yang lebih bertele-tele dan memerlukan parser khusus untuk penguraian, sehingga lebih sulit digunakan.
- Kecepatan dan Efisiensi
JSON lebih cepat dalam parsing data karena dapat diuraikan dengan fungsi JavaScript standar, sedangkan XML memerlukan pengurai khusus yang lebih lambat. JSON juga memiliki ukuran yang lebih kecil, sehingga lebih efisien dalam pengiriman data melalui jaringan.
- Kompatibilitas dengan JavaScript
JSON dirancang untuk kompatibilitas dengan JavaScript, sehingga dapat langsung diproses sebagai objek JavaScript, yang membuatnya sangat mudah digunakan dalam pengembangan web. XML, meskipun dapat digunakan dengan berbagai bahasa pemrograman, tidak memiliki integrasi yang sebaik dengan JavaScript seperti JSON.
- Penggunaan dalam Web Development
JSON sangat populer dalam pengembangan web karena dapat digunakan dalam AJAX requests dan REST APIs, serta mendukung penyimpanan data yang lebih ringan dan cepat. XML, meskipun masih digunakan dalam beberapa konteks, tidak sepopuler JSON dalam pengembangan web modern.

Dengan demikian, JSON lebih populer karena kelebihan-kelebihannya dalam hal simpelitas, kecepatan, dan kompatibilitas dengan JavaScript, membuatnya lebih ideal untuk penggunaan dalam pengembangan web dan aplikasi seluler.



3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Metode is_valid() pada form Django adalah sebuah fungsi yang sangat penting dalam proses validasi data. Berikut adalah penjelasan tentang fungsi dan kebutuhan metode tersebut:

Fungsi is_valid()
- Validasi Data 
Metode is_valid() digunakan untuk memvalidasi data yang diinputkan oleh pengguna. Ini berarti bahwa metode ini akan memeriksa apakah data yang diinputkan memenuhi semua aturan validasi yang telah ditetapkan untuk form tersebut.
- Pengecekan Aturan Validasi 
Metode ini akan memeriksa setiap field form dan memastikan bahwa data yang diinputkan tidak mengandung kesalahan. Jika semua data valid, maka metode is_valid() akan mengembalikan nilai True, sedangkan jika ada kesalahan, maka akan mengembalikan nilai False.
- Penggunaan dalam Model Forms 
Pada model forms, metode is_valid() juga akan memanggil metode full_clean() pada instance model untuk memvalidasi data secara lebih lanjut, termasuk memastikan bahwa field-field yang unik memenuhi syarat unikitas.

Kebutuhan Metode is_valid()
- Menghindari Kesalahan 
Dengan menggunakan metode is_valid(), pengembang dapat menghindari kesalahan yang mungkin terjadi karena input yang tidak valid. Ini memastikan bahwa data yang disimpan ke dalam database adalah akurat dan valid.
- Meningkatkan Kualitas Aplikasi 
Metode ini membantu meningkatkan kualitas aplikasi Django dengan memastikan bahwa pengguna tidak dapat menyimpan data yang tidak valid. Hal ini juga meningkatkan kepercayaan pengguna terhadap aplikasi.
- Mengurangi Kerusakan Data 
Dengan memvalidasi data sebelum disimpan, metode is_valid() dapat mengurangi kerusakan data yang mungkin terjadi karena input yang tidak valid. Ini sangat penting dalam aplikasi yang membutuhkan data yang akurat dan terpercaya.

Dalam keseluruhan, metode is_valid() adalah komponen penting dalam pengembangan aplikasi Django karena membantu memastikan bahwa data yang diinputkan oleh pengguna adalah valid dan akurat.



4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token (Cross-Site Request Forgery token) adalah sebuah fitur keamanan yang sangat penting dalam Django untuk mencegah serangan Cross-Site Request Forgery (CSRF). Berikut adalah alasan mengapa kita membutuhkan csrf_token:

- Mencegah Serangan CSRF
CSRF adalah serangan yang memanfaatkan keadaan pengguna sudah terautentikasi di suatu situs web. Serangan ini dapat membuat pengguna melakukan aksi yang tidak mereka inginkan, seperti transfer dana, perubahan email, dan lain-lain. Dengan menggunakan csrf_token, Django dapat memastikan bahwa setiap permintaan POST yang masuk dari pengguna adalah valid dan berasal dari pengguna yang sudah terautentikasi.

Jika kita tidak menambahkan csrf_token pada form Django, maka penggunaan form tersebut dapat terbuka bagi serangan CSRF. Berikut adalah apa yang dapat terjadi:

- Serangan CSRF Berhasil
Tanpa csrf_token, serangan CSRF dapat berhasil dan membuat pengguna melakukan aksi yang tidak mereka inginkan. Contohnya, serangan dapat membuat pengguna transfer dana atau perubahan email tanpa mereka sadari.
- Kerusakan Data dan Keamanan
Serangan CSRF yang berhasil dapat menyebabkan kerusakan data dan keamanan. Hal ini karena serangan dapat memanfaatkan keadaan pengguna sudah terautentikasi untuk melakukan aksi yang tidak sah.

Penyerang dapat memanfaatkan kekurangan csrf_token dengan cara berikut:

- Membuat Link atau Form Malicious
Penyerang dapat membuat link atau form yang mengandung permintaan POST yang tidak valid. Jika pengguna yang sudah terautentikasi mengklik link atau mengisi form tersebut, maka permintaan POST tersebut akan dijalankan tanpa memeriksa apakah memiliki csrf_token yang valid.
- Menggunakan Token Lain
Penyerang juga dapat mencoba menggunakan token lain yang tidak valid untuk mengelabui sistem. Namun, karena csrf_token di-Django selalu diubah secara acak setiap kali pengguna login, maka kemungkinan ini sangat kecil.

Dengan demikian, menambahkan csrf_token pada form Django adalah sangat penting untuk mencegah serangan CSRF dan menjaga keamanan aplikasi.



5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Langkah 1 : Membuat Input Form untuk Menambahkan Objek Model
- Menentukan Model
- Membuat Form untuk Model
- Membuat View untuk Form Input
- Membuat Template
Langkah 2 : Membuat 4 Fungsi Views untuk Menampilkan Data dalam Format XML dan JSON
- View untuk Menampilkan Semua Objek dalam Format JSON
- View untuk Menampilkan Semua Objek dalam Format XML
- View untuk Menampilkan Objek Berdasarkan ID dalam Format JSON
- View untuk Menampilkan Objek Berdasarkan ID dalam Format XML
Langkah 3 : Membuat Routing URL untuk Setiap Views
- Menambahkan URL pada urls.py
Langkah 4 : Testing dan Penyempurnaan
- Testing
- Penyempurnaan


json by id
![alt text](<Screenshot (339)-1.png>)
xml by id
![alt text](<Screenshot (338).png>)
json
![alt text](<Screenshot (337)-1.png>)
xml
![alt text](<Screenshot (336).png>)