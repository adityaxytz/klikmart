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


