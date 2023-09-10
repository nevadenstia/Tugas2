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
1. Buat template HTML dengan nama TokoPedia



2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.