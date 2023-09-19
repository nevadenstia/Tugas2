README TUGAS 3

1. Apa perbedaan antara form POST dan form GET dalam Django?
- Metode POST Django
Digunakan untuk mengirim data ke server untuk diproses yang dapat di akses dengan request.POST. Data dari form dikirim jadi body request maka tidak ditampilkan dalam bentuk URL. Dalam Tugas 3, metode POST digunakan saat menginput data dalam create_product.html serta diproses dalam fungsi create_product menggunakan parameter request.
- Metode GET Django
Digunakan untuk mengirim data kepada server untuk permintaan data. Data yang dikirim melalui metode GET ditampilkan di URL sebagai query parameters. Karena terbatas pada URL maka data dengan metode GET tidak dianjurkan merupakan data sensitif atau data besar.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML (eXtensible Markup Language): Digunakan untuk mendefinisikan struktur data yang dapat di-customize. Biasanya digunakan dalam berbagai aplikasi untuk pertukaran data, tetapi memiliki format yang verbose dan kompleks.
- JSON (JavaScript Object Notation): Format yang ringkas dan mudah dibaca yang digunakan untuk pertukaran data antara aplikasi. Digunakan secara luas dalam pengembangan web modern karena ringan, cepat, dan mudah diinterpretasikan oleh bahasa pemrograman.
- HTML (Hypertext Markup Language): Bahasa markah yang digunakan untuk membuat struktur dan tampilan halaman web. Biasanya digunakan untuk menampilkan konten dan tata letak pada browser web. Pada Tugas 3 ini, HTML banyak digunakan terutama dalam pemindahan data add new product pada halaman main.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON adalah format data yang ringkas, mudah dibaca, dan mudah diinterpretasikan oleh bahasa pemrograman. JSON mendukung tipe data kompleks seperti objek dan array, yang berguna untuk merepresentasikan data yang rumit. JSON dapat digunakan dengan berbagai bahasa pemrograman, menjadikannya pilihan yang serbaguna untuk pertukaran data antara berbagai teknologi. JSON biasanya lebih efisien dalam hal ukuran data daripada XML, sehingga mengurangi penggunaan bandwidth.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Step 1: Membuat input form untuk menambahkan objek model pada app sebelumnya.
- Buat kerangka web base.html pada templates di root folder
- Pisahkan CSS (style) main.html pada Tugas 2 dan dirapihkan dalam base.html
- Buat main.html dan create_product.html dengan kerangka base.html
- Modifikasi models.py menjadi 2 class Main dan class Product
- Buat forms.py dalam main dengan model Product dan fields yang mau diisi
- Tambahkan button add new product di main.html dan buat loop for product in products
- Modifikasi di show_main pada views.py dengan menambahkan products = Product.object.all() yang kemudian merubah context dengan isi 'products' = product.
- Tambahkan total_stock dengan menggunakan models.Sum antara 'amount' dan 'total_stock' pada show_main untuk mentotalkan stock
- Buat create_product pada views.py yang memanggil ProductForm dari forms.py dengan parameter (request.POST)
- Modifikasi urls.py dalam main dengan adanya create-product yang memanggil fungsi create_product
- open virtual environment
- run python manage.py makemigrations dan migrate karena ada perubahan dalam models
- run python manage.py runserver
  
Step 2: Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
- add import HttpResponse dan serializers
- tambahkan show_xml, show_json, show_xml_by_id, show_json_by_id pada views.py
  
Step 3: Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- modifikasi urls.py dengan menambahkan path setiap fungsi ("xml/", "json", "xml/<int:id>/", "json/<int:id>/") dan pastikan import main.views
- open virtual environment
- run python manage.py runserver
  
5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

screenshot /create-product :
![Screenshot (720)](https://github.com/nevadenstia/Tugas2/assets/125188477/0db916cb-2a60-43b5-ac84-d66f3141ebe0)

screenshot /main :
![Screenshot (715)](https://github.com/nevadenstia/Tugas2/assets/125188477/b6ae302d-165c-4cfd-9a2d-17c87019d7b2)

screenshot /xml :
![Screenshot (716)](https://github.com/nevadenstia/Tugas2/assets/125188477/9fd7089d-33e9-4dc6-9472-8558988dfd33)

screenshot /xml by id :
![Screenshot (717)](https://github.com/nevadenstia/Tugas2/assets/125188477/1e0c46df-3100-4db8-941b-65cd3aad217a)

screenshot /json :
![Screenshot (718)](https://github.com/nevadenstia/Tugas2/assets/125188477/683af63a-96a9-4602-a5ed-9db575b63636)

screenshot /json by id:
![Screenshot (719)](https://github.com/nevadenstia/Tugas2/assets/125188477/2e9711c9-143f-4096-b8bd-1a49be8da09f)

########################################################################################################

README TUGAS 2

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
![Bagan Keterkaitan](https://github.com/nevadenstia/Tugas2/assets/125188477/eb4cbe12-3f17-4bb8-9c53-aa3b999ac05f)

Berkas `urls.py` berperan dalam menentukan tampilan yang akan ditampilkan berdasarkan permintaan (request) dari pengguna.
`models.py` berfungsi sebagai perantara antara database dan tampilan saat data sedang diproses.
Pada `views.py`, terdapat fungsi-fungsi yang digunakan untuk menerapkan logika bisnis, dengan bantuan dari model dan template.
Sementara itu, berkas-berkas HTML digunakan untuk menampilkan data yang telah ada.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment untuk mengisolasi dependensi proyek Django dari lingkungan Python global. Ini memungkinkan pengembang untuk mengelola paket Python secara terpisah untuk setiap proyek, menghindari konflik dan masalah kompatibilitas. Walau begitu, tetap memungkinkan untuk membuat aplikasi web berbasis Django tanpa venvn, namun hal tersebut tidak begitu dianjurkan.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC (Model-View-Controller) : Dimana Model menjadi representasi dari data dalam aplikasi, sementara View mengatur tampilan dari data Model, dan Controller yang mengurus permintaan pengguna dan sebagai penyambung untuk mengarahkan ke Model atau View.

- MVT (Model-View-Template) : Sama seperti MVC, Model dan View disini juga memiliki fungsi yang serupa dengan MVC, yaitu sebagai representasi data dan tampilan untuk pengguna. Sementara Template berguna untuk menyimpan HTML yang akan ditampilkan apda browser dan menyambungkan kedua model dan View.

- MVVM (Model-View-ViewModel) : Sama seperti MVT dan MVC, Model dan View juga digunakan untuk representasi data dan tampilan pengguna. Berbedanya dalam ViewModel, dimana ViewModel digunakan untuk menyediakan interface antara model dan view yang memisahkan keduanya.

Perbedaan utama adalah bagaimana komponen-komponen ini berinteraksi dan memisahkan tanggung jawab dalam aplikasi. MVC adalah arsitektur umum yang digunakan dalam pengembangan web, sedangkan MVT adalah konsep yang spesifik untuk Django, dan MVVM sering digunakan dalam pengembangan aplikasi berbasis klien.
