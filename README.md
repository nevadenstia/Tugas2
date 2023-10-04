<h1>**README TUGAS 5**
**1.Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya**
Element Selector memungkinkan kita mengubah properti untuk semua elemen yang memiliki tag HTML yang sama. Kita dapat menggunakannya ketika kita ingin menerapkan gaya ke semua elemen dengan tag HTML yang sama dalam dokumen. Misalnya, kita dapat menggunakan Element Selector untuk mengatur gaya teks dalam semua elemen <p> dalam halaman kita.

**Jelaskan HTML5 Tag yang kamu ketahui.**
HTML5 memperkenalkan beberapa tag baru yang memiliki peran khusus dalam membangun struktur halaman web yang lebih jelas dan informatif. Beberapa tag HTML5 yang penting meliputi:
- body
- col
- head
- headere
- img
- nav
- script
- style
- strong
**Jelaskan perbedaan antara margin dan padding.**
Margin dan padding adalah dua properti CSS yang digunakan untuk mengatur ruang di sekitar elemen HTML.
- Margin: Margin adalah ruang di luar elemen, yang memisahkan elemen dari elemen lain di sekitarnya. Margin tidak memiliki latar belakang atau warna dan berfungsi untuk mengatur jarak antara elemen-elemen.
- Padding: Padding adalah ruang di dalam elemen, yang memisahkan isi elemen dari tepi elemen itu sendiri. Padding berada di sekitar isi elemen dan dapat memiliki latar belakang atau warna. Ini digunakan untuk mengatur jarak antara konten elemen dan batasnya.
  
**Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
Tailwind CSS adalah framework CSS yang berfokus pada utilitas. Ini berarti kita menggunakan sejumlah besar kelas CSS yang telah ditentukan sebelumnya untuk membangun tampilan kita. Tailwind memberikan tingkat fleksibilitas yang tinggi, tetapi juga memerlukan pemahaman yang kuat tentang kelas-kelas utilitas yang tersedia. Ini cocok untuk proyek-proyek yang memerlukan penyesuaian dan desain yang unik.

Bootstrap, di sisi lain, adalah framework CSS yang lebih kaku dan datang dengan komponen siap pakai, seperti tombol, jumbotron, formulir, dan banyak lagi. Ini memungkinkan kita membangun situs dengan cepat tanpa perlu menulis banyak kode CSS khusus. Bootstrap cocok untuk proyek-proyek yang perlu dikembangkan dengan cepat dan mengikuti pedoman desain yang sudah ada.

Kapan kita harus menggunakan Bootstrap atau Tailwind tergantung pada kebutuhan proyek kita. Gunakan Bootstrap jika kita ingin cepat dan mengikuti pedoman desain yang jelas. Gunakan Tailwind jika kita ingin fleksibilitas lebih besar dalam desain dan siap untuk menghabiskan waktu memahami kelas-kelas utilitas yang ada.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Karena sebelum Tugas 5 ini aku sudah menggunakan CSS, dengan memisahkan style CSSnya di base.html sehingga hanya perlu memanggil div class di main.html. Tentunya juga beberapa tambahan style lainnya. Serta juga karena pada Tugas 4, aku sudah membuat button add substract dan delete product untuk menghapus daftar inventori. Sehingga pada Tugas 5 ini aku fokus pada kustomisasi halaman .html saja, juga tentunya merubah untuk menggunakan approach card pada daftar inventori.

1. Set dulu background color di base.html. buat .banner .login-container dan .registration-container, ini nantinya akan jadi background image dengan menyisipkan link image pada url();
2. Buat container yang dibutuhkan:
	- login-container: Ini adalah container untuk halaman login. Ini digunakan untuk mengatur posisi elemen-elemen dalam halaman login.
	- .login: Ini adalah container untuk elemen-elemen login seperti formulir login dan tombol login. Ini memiliki latar belakang semi-transparan putih yang memungkinkan teks terbaca.
	- .product-container: Ini adalah container untuk menampilkan daftar produk dalam halaman toko online. Ini memiliki latar belakang abu-abu dan elemen-elemen yang berhubungan dengan produk.
	- .registration-container: Ini adalah container untuk halaman pendaftaran pengguna. Ini digunakan untuk mengatur posisi elemen-elemen dalam halaman pendaftaran.
	- .registration: Ini adalah container untuk elemen-elemen pendaftaran seperti formulir pendaftaran dan tombol pendaftaran. Ini memiliki latar belakang semi-transparan putih yang memungkinkan teks terbaca.
	- .product-box: Ini adalah container untuk setiap kotak produk dalam daftar produk. Setiap kotak ini berisi informasi tentang satu produk, seperti nama produk, gambar, deskripsi, dll.
	- .banner: Ini adalah container untuk header banner di halaman toko online. Ini memiliki latar belakang gambar dan digunakan untuk menampilkan pesan selamat datang dan informasi tentang toko.
	- .image-choose-container: Ini adalah container yang digunakan untuk mengatur elemen-elemen terkait pemilihan gambar.
	- .choose-box: Ini adalah container untuk pemilihan gambar dalam formulir.
	- .new-boxes-container: Ini adalah container untuk mengatur dua kotak (kiri dan kanan) yang mungkin digunakan dalam tampilan yang lebih kompleks. Ini digunakan untuk mengorganisir elemen-elemen di halaman.
2. edit heading sesuai kebutuhan:
- header1 = Heading ini digunakan dalam elemen dengan kelas .banner untuk menampilkan judul besar dalam header banner di halaman toko online.
- header2 = Heading ini digunakan beberapa kali dalam kode Anda, biasanya digunakan untuk menampilkan subjudul atau informasi tambahan dalam halaman, misalnya, Nama, NPM, Kelas, dll.
- header3 = Heading ini digunakan dalam elemen dengan kelas .product-container untuk menampilkan judul yang menyatakan total stok produk.
- header4 = Heading ini digunakan beberapa kali dalam kode Anda untuk menampilkan subjudul atau informasi tambahan, seperti "Item Name:", "Available Stock:", "Description:", "Rating:", "Reviews:", dan lainnya.

3. edit tambahan sesuai kebutuhan (termasuk format image, format daftar inventori, dst)
	- .button-container: Ini adalah kelas yang digunakan untuk mengatur margin atas elemen-elemen tombol dalam container pendaftaran.
	- .quantity-control: Ini adalah kelas yang digunakan untuk mengatur tata letak dari tombol-tombol kontrol kuantitas di setiap produk pada halaman produk.
	- .quantity-button: Ini adalah kelas yang digunakan untuk mengatur tampilan tombol-tombol kontrol kuantitas produk (tombol kurang, tambah, dll).
	- .center-image: Ini adalah kelas yang digunakan untuk mengatur tampilan gambar agar berada di tengah container dan membatasi lebar dan tingginya.
	- .item-details: Ini adalah kelas yang digunakan untuk mengatur tampilan elemen-elemen yang menampilkan detail produk, seperti nama produk, stok, deskripsi, peringkat, ulasan, dll.
	- .image-container: Ini adalah kelas yang digunakan untuk mengatur tampilan kotak yang berisi gambar produk. Ini termasuk dalam elemen dengan kelas .product-box.
	- .left-box dan .right-box: Ini adalah kelas yang digunakan untuk mengatur tampilan dua kotak (kiri dan kanan) dalam container .new-boxes-container.


3. Tambahkan fitur bonus, membedakan warna terakhir dari baris terakhir daftar inventori:

Buat style last-row, last-row adalah kelas yang digunakan untuk mengatur latar belakang elemen terakhir dalam daftar produk untuk memberikan tampilan yang berbeda (mengganti warna latar belakang). Tambahkan  div class="product-box{% if forloop.last %} last-row{% endif %}" diatas product-box namun di dalam loop for product in products.

Kode div class="product-box{% if forloop.last %} last-row{% endif %}" digunakan untuk membuat elemen container dalam loop yang mengulang produk-produk yang ditampilkan di halaman produk Anda. Mari kita jelaskan bagian ini lebih rinci:

div class="product-box": Ini adalah elemen div dengan kelas "product-box". Setiap produk dalam daftar produk Anda dibungkus dalam elemen ini. Ini digunakan untuk mengelompokkan informasi terkait produk bersama-sama, seperti gambar produk, nama produk, deskripsi, dll.

{% if forloop.last %} last-row{% endif %}: Ini adalah struktur pengendali kondisional yang digunakan di dalam atribut kelas elemen. Ini menguji apakah saat ini produk yang sedang diproses adalah produk terakhir dalam loop atau tidak. Jika saat ini produk terakhir, maka akan ditambahkan kelas "last-row" ke elemen.

Jadi, jika produk saat ini adalah produk terakhir dalam loop, maka elemen div ini akan memiliki kelas "product-box last-row". Ini mungkin digunakan untuk memberikan tampilan yang berbeda atau gaya tambahan pada produk terakhir dalam daftar produk, seperti mengganti warna latar belakangnya atau mengatur margin bawah tambahan untuk memisahkan produk terakhir dari produk sebelumnya dalam tampilan halaman.

###############################################################################################################################################################################################
<h1>**README TUGAS 4**

**Pertanyaan**
**1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
Django UserCreationForm adalah salah satu formulir bawaan yang disediakan oleh Django untuk mempermudah pembuatan dan registrasi pengguna dalam aplikasi web. Form ini menyediakan fitur seperti validasi kata sandi, konfirmasi kata sandi, dan validasi email. Kelebihannya adalah menyederhanakan proses pembuatan pengguna, mengurangi kode yang perlu ditulis, dan memastikan data pengguna dibuat dengan benar. Kekurangannya adalah kurangnya fleksibilitas untuk kasus khusus, dan perlu penyesuaian jika Anda memerlukan fitur tambahan.

**2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
Autentikasi adalah proses memverifikasi identitas pengguna (misalnya, memeriksa apakah pengguna telah log masuk), sementara otorisasi adalah proses memberikan atau menolak akses pengguna ke sumber daya tertentu setelah mereka diautentikasi. Keduanya penting dalam Django dan aplikasi web secara umum, karena autentikasi memastikan hanya pengguna yang sah yang memiliki akses ke sistem, sementara otorisasi mengendalikan apa yang dapat dilakukan pengguna setelah diautentikasi, melindungi data sensitif dan sumber daya lainnya.

**3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
Cookies dalam konteks aplikasi web adalah data kecil yang disimpan di sisi klien (biasanya dalam browser) dan digunakan untuk menyimpan informasi sesi pengguna, seperti ID sesi atau preferensi. Django menggunakan cookies untuk mengelola data sesi pengguna dengan menyediakan penggunaan modul seperti django.contrib.sessions. Ini memungkinkan server untuk mengenali pengguna dan menjaga sesi mereka secara konsisten selama navigasi di situs web.

**4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**
Penggunaan cookies dalam pengembangan web tidak selalu aman secara default. Cookies dapat menjadi rentan jika tidak diatur dengan benar. Risiko potensial termasuk peretasan sesi (session hijacking), di mana penyerang mencuri cookie sesi pengguna untuk mengakses akun mereka. Untuk mengurangi risiko ini, Anda harus mengimplementasikan tindakan keamanan seperti HTTPS untuk melindungi data selama transit dan menggunakan praktik terbaik dalam manajemen sesi, seperti menghindari menyimpan data sensitif dalam cookies dan mengatur atribut seperti Secure dan HttpOnly untuk meningkatkan keamanan cookies.

**5.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
1. Membuat fungsi register, login_user, dan logout_user pada main.views yang tetap menggunakan style css dari base.html
2. Membuat urls dengan /register, /login, dan /logout pada main.urls
3. Menambahkan register.html dan login.html pada main/templates
4. retriksi fungsi show_main dengan @login_required
5. Menambahkan pada login_user response.set_cookie untuk login data menggunakan cookie.
6. Tambahkan pada context di show_main last_login yang request.COOKIES
7. edit logout_user dengan response.delete_cookie supaya menghapus cookie
8. Menambahkan user = models.ForeignKey untuk menghubungkan model Product dengan User
9. Karena name pada setiap kali login akan diisi oleh nama user, maka name pada models Main dihapuskan.
10. ubah pada show_main untuk memfilter model Product hanya memilih objects sesuai filter User yang login
11. ubah pada show_main 'name' jadi request.user.username
12. buat fungsi add_item dan subtract_item pada views.py menggunakan import get_objects_or_404 pada Product dengan id menggunakan item_id gunakan .amount +/- dan .save()
13. buat fungsi delete_item pada views.py menggunakan import get_objects_or_404 dan gunakan .delete().
14. ubah urls.py untuk memanggil ketiga fungsi tersebut yaitu add_item/ subtract_item/ dan delete_item/
15. ubah main.html dengan menambahkan tiga button dengan method POST dan href pada main:add_item, main:delete_item, dan main:subtract_item.
16. ubah juga css pada base.html sesuai kebutuhan desain
17. Lakukan migrations dan set data defaultnya dengan ID 1 agar data yang sebelumnya sudah masuk akan masuk kedalam ID 1 user dalam kasus ini dengan username "neva".
18. Add 2 dummy account "neva" dan "orang" dengan password = "abc123abc123" lalu masing-masing isi 3 data products.
19. git add, commit, push ke github.


########################################################
<h1>**README TUGAS 3**

**Pertanyaan**
**1. Apa perbedaan antara form POST dan form GET dalam Django?**

- Metode POST Django
Digunakan untuk mengirim data ke server untuk diproses yang dapat di akses dengan request.POST. Data dari form dikirim jadi body request maka tidak ditampilkan dalam bentuk URL. Dalam Tugas 3, metode POST digunakan saat menginput data dalam create_product.html serta diproses dalam fungsi create_product menggunakan parameter request.
- Metode GET Django
Digunakan untuk mengirim data kepada server untuk permintaan data. Data yang dikirim melalui metode GET ditampilkan di URL sebagai query parameters. Karena terbatas pada URL maka data dengan metode GET tidak dianjurkan merupakan data sensitif atau data besar.

**2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**
- XML (eXtensible Markup Language): Digunakan untuk mendefinisikan struktur data yang dapat di-customize. Biasanya digunakan dalam berbagai aplikasi untuk pertukaran data, tetapi memiliki format yang verbose dan kompleks.
- JSON (JavaScript Object Notation): Format yang ringkas dan mudah dibaca yang digunakan untuk pertukaran data antara aplikasi. Digunakan secara luas dalam pengembangan web modern karena ringan, cepat, dan mudah diinterpretasikan oleh bahasa pemrograman.
- HTML (Hypertext Markup Language): Bahasa markah yang digunakan untuk membuat struktur dan tampilan halaman web. Biasanya digunakan untuk menampilkan konten dan tata letak pada browser web. Pada Tugas 3 ini, HTML banyak digunakan terutama dalam pemindahan data add new product pada halaman main.

**3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
JSON adalah format data yang ringkas, mudah dibaca, dan mudah diinterpretasikan oleh bahasa pemrograman. JSON mendukung tipe data kompleks seperti objek dan array, yang berguna untuk merepresentasikan data yang rumit. JSON dapat digunakan dengan berbagai bahasa pemrograman, menjadikannya pilihan yang serbaguna untuk pertukaran data antara berbagai teknologi. JSON biasanya lebih efisien dalam hal ukuran data daripada XML, sehingga mengurangi penggunaan bandwidth.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
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
  
**5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**

- screenshot / :
![Screenshot (721)](https://github.com/nevadenstia/Tugas2/assets/125188477/edd54d09-297e-4a66-9031-bb0ac5e942d7)

- screenshot /create-product :
![Screenshot (720)](https://github.com/nevadenstia/Tugas2/assets/125188477/0db916cb-2a60-43b5-ac84-d66f3141ebe0)

- screenshot /main :
![Screenshot (715)](https://github.com/nevadenstia/Tugas2/assets/125188477/b6ae302d-165c-4cfd-9a2d-17c87019d7b2)

- screenshot /xml :
![Screenshot (716)](https://github.com/nevadenstia/Tugas2/assets/125188477/9fd7089d-33e9-4dc6-9472-8558988dfd33)

- screenshot /xml by id :
![Screenshot (717)](https://github.com/nevadenstia/Tugas2/assets/125188477/1e0c46df-3100-4db8-941b-65cd3aad217a)

- screenshot /json :
![Screenshot (718)](https://github.com/nevadenstia/Tugas2/assets/125188477/683af63a-96a9-4602-a5ed-9db575b63636)

- screenshot /json by id:
![Screenshot (719)](https://github.com/nevadenstia/Tugas2/assets/125188477/2e9711c9-143f-4096-b8bd-1a49be8da09f)

########################################################################################################

<h1>**README TUGAS 2**

Tautan aplikasi Adaptable 	: https://tugas2.adaptable.app/
Tautan Repositori GitHub 	: https://github.com/nevadenstia/Tugas2.git

**Pertanyaan**
**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

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


**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
![Bagan Keterkaitan](https://github.com/nevadenstia/Tugas2/assets/125188477/eb4cbe12-3f17-4bb8-9c53-aa3b999ac05f)

Berkas `urls.py` berperan dalam menentukan tampilan yang akan ditampilkan berdasarkan permintaan (request) dari pengguna.
`models.py` berfungsi sebagai perantara antara database dan tampilan saat data sedang diproses.
Pada `views.py`, terdapat fungsi-fungsi yang digunakan untuk menerapkan logika bisnis, dengan bantuan dari model dan template.
Sementara itu, berkas-berkas HTML digunakan untuk menampilkan data yang telah ada.

**3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Kita menggunakan virtual environment untuk mengisolasi dependensi proyek Django dari lingkungan Python global. Ini memungkinkan pengembang untuk mengelola paket Python secara terpisah untuk setiap proyek, menghindari konflik dan masalah kompatibilitas. Walau begitu, tetap memungkinkan untuk membuat aplikasi web berbasis Django tanpa venvn, namun hal tersebut tidak begitu dianjurkan.

**4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
- MVC (Model-View-Controller) : Dimana Model menjadi representasi dari data dalam aplikasi, sementara View mengatur tampilan dari data Model, dan Controller yang mengurus permintaan pengguna dan sebagai penyambung untuk mengarahkan ke Model atau View.

- MVT (Model-View-Template) : Sama seperti MVC, Model dan View disini juga memiliki fungsi yang serupa dengan MVC, yaitu sebagai representasi data dan tampilan untuk pengguna. Sementara Template berguna untuk menyimpan HTML yang akan ditampilkan apda browser dan menyambungkan kedua model dan View.

- MVVM (Model-View-ViewModel) : Sama seperti MVT dan MVC, Model dan View juga digunakan untuk representasi data dan tampilan pengguna. Berbedanya dalam ViewModel, dimana ViewModel digunakan untuk menyediakan interface antara model dan view yang memisahkan keduanya.

Perbedaan utama adalah bagaimana komponen-komponen ini berinteraksi dan memisahkan tanggung jawab dalam aplikasi. MVC adalah arsitektur umum yang digunakan dalam pengembangan web, sedangkan MVT adalah konsep yang spesifik untuk Django, dan MVVM sering digunakan dalam pengembangan aplikasi berbasis klien.
