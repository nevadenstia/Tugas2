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


