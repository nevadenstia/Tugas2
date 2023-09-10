Tautan aplikasi Adaptable 	: https://tugas2.adaptable.app/
Tautan Repositori GitHub 	: https://github.com/nevadenstia/Tugas2.git

Pertanyaan
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

STEP 1: Membuat sebuah proyek Django baru
1. Membuat repo public GitHub dan folder baru dengan nama 'Tugas2'
2. Buka cmd lakukan perintah git init dan git config untuk menghubungkan.
3. Menjalankan perintah git branch -M main untuk membuat branch serta remote add origin menggunakan URL Repo.
4. Buat requirements.txt serta file .gitignore sama seperti tutorial.
5. Jalankan virtual environment di cmd dan beri perintah pip install -r requirements.txt
6. Buat proyek Django dengan nama Tugas2 dengan "django-admin startproject Tugas2"

STEP 2: Membuat aplikasi dengan nama main
1. Run python manage.py startapp main
2. Edit settings.py dan tambahkan 'main' pada INSTALLED_APPS
3. Buka models.py dan buat class bernama Main dengan name (Charfield), item_name (Charfield), npm (IntegerField), kelas (TextField), amount (IntegerField), description (Textfield), rating (Charfield) dan reviews (Textfield).

STEP 3: Membuat fungsi views.py
1. Buat template HTML dengan nama main.html menggunakan attribute yang ada
2. Buat fungsi pada show_main views.py menggunakan render yang memberi context untuk isi dari HTML pada main.html.

STEP 4: Membuat routing pada urls.py pada aplikasi main
Membuat urlpatterns yang memanggil show_main pada main.views.py menggunakan path dari django.urls.

STEP 5: Melakukan deployment di Adaptable
Lakukan git add, git commit, dan git push lalu buka Adaptable dan tunggu deployment selesai.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment untuk mengisolasi dependensi proyek Django dari lingkungan Python global. Ini memungkinkan pengembang untuk mengelola paket Python secara terpisah untuk setiap proyek, menghindari konflik dan masalah kompatibilitas. Walau begitu, tetap memungkinkan untuk membuat aplikasi web berbasis Django tanpa venvn, namun hal tersebut tidak begitu dianjurkan.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC (Model-View-Controller) : Dimana Model menjadi representasi dari data dalam aplikasi, sementara View mengatur tampilan dari data Model, dan Controller yang mengurus permintaan pengguna dan sebagai penyambung untuk mengarahkan ke Model atau View.

- MVT (Model-View-Template) : Sama seperti MVC, Model dan View disini juga memiliki fungsi yang serupa dengan MVC, yaitu sebagai representasi data dan tampilan untuk pengguna. Sementara Template berguna untuk menyimpan HTML yang akan ditampilkan apda browser dan menyambungkan kedua model dan View.

-MVVM (Model-View-ViewModel) : Sama seperti MVT dan MVC, Model dan View juga digunakan untuk representasi data dan tampilan pengguna. Berbedanya dalam ViewModel, dimana ViewModel digunakan untuk menyediakan interface antara model dan view yang memisahkan keduanya.

Perbedaan utama adalah bagaimana komponen-komponen ini berinteraksi dan memisahkan tanggung jawab dalam aplikasi. MVC adalah arsitektur umum yang digunakan dalam pengembangan web, sedangkan MVT adalah konsep yang spesifik untuk Django, dan MVVM sering digunakan dalam pengembangan aplikasi berbasis klien.
