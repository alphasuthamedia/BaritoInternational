# BaritoInternational

Everything You Need, All in One Place.

### Deployment
[Barito International, visit here](http://alpha-sutha-baritointernational.pbp.cs.ui.ac.id/)

---
## Tugas 2 - PBP 24/25

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1.  Pertama pastikan python telah terinstall dengan sempurna, setelah python terinstall dengan sempurna, pastikan    telah membuat virtual environment (venv). Setelah berhasil membuat venv, pastikan anda telah mengaktifkan venv yang baru saja dibuat.
2.  Buat sebuah text file (ex : requirements.txt) yang berisi paket atau modul yang akan di install ke dalam
environment python yang telah dibuat. requirements.txt ini berisi:
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```    
    Setelah demikian, lakukan "pip install requirements.txt"
3.  Selanjutnya, buat proyek Django dengan perintah "`django-admin startproject [yourprojectname] .`"
4.  Tambahkan permission host lokal yang dibolehkan pada file settings.py
    ```
        ALLOWED_HOSTS = ["localhost", "127.0.0.1", <config-pws>]
    ```
5.  Buat aplikasi `main` meggunakan perintah `python manage.py startapp main` di dalam Command Prompt (CMD)
6.  Setelah aplikasi main selesai dibuat, sekarang buat modelnya dengan mendefinisikan seperti apa model 
    kita selanjutnya, dengan cara menuliskan kode didalam `models.py`, kode tersebut sebagai berikut:
    ```python
    from django.db import models
    # Create your models here.
    class Product(models.Model):
          name = models.CharField(max_length=255)
          price = models.IntegerField()
          description = models.TextField()
    ```
    Perlu diketahui bahwa kita dapat membuat model menjadi lebih kompleks, dengan menambahkan atribut lain,
      namun kewajiban utamanya, kita membuat 3 atribut seperti diatas.
7.  Setelah kita buat model basis data (baru), lakukan migrasi. Hal ini bertujuan untuk mengubah struktur tabel
    basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru. Lakukan migrasi dengan
    menjalankan perintah pada CMD 
    ```s
        python manage.py makemigrations # perintah untuk membuat migrasi model
        python manage.py migrate # perintah untuk menerapkan migrasi ke dalam basis data lokal
    ```
8.  Sekarang, kita hanya tinggal hubungkan view dan template, dengan ini kita tidak perlu mengubah (hardcode)
    kode html kita setiap data dimasukkan. Buat folder baru di dalam aplikasi main bernama `templates`, folder
     ini berupa file html yang akan kita hubungkan dengan view, sebagai contoh saya menggunakan `main.html`
9.  Kemudian integrawsikan komponen MVT dengan membuat fungsi `show_main` di `views.py` yang akan mengembalikan
    _response_ berupa _template_ HTML yang menampilkan nama aplikasi dan nama serta kelas saya.
    ```python
    from django.shortcuts import render
       def show_main(request):
        Product = [
    {
           'name': 'Dell XPS 13',
           'price': 1200,
           'description': 'Powerful ultrabook with stunning 4K display and incredible performance for multitasking.',
           'quantity': 15
    },.... (dan beberapa produk yang lain)
       ]
        context = {
           'tagline' : 'Everything You Need, All in One  Place.',
           'products' : Product
        }
        return render(request, "main.html", context)
    ```
    `request` berarti sebuah objek permintaan HTTP yang dikirim oleh pengguna.
    `main.html` adalah berkas template yang akan digunakan untuk me-render tampilan
    `context` adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.
    `Product` adalah dictionary yang berisi data produk, yang mana akan diteruskan untuk dieksekusi oleh 
   context dengan memanggilnya `'products' : Product` dan akan diteruskan ke tampilan oleh tugas `context`
10. Sekarang kita hanya perlu mengatur routing, agar pemetaan MVT yang telah kita buat dapat tereksekusi dengan
    tepat. Pertama kita atur routing, lakukan routing URL Aplikasi main dengan cara buat berkas urls.py di dalam
    direktori main. lalu tuliskan sintaks sebagai berikut di dalamnya :
    ``` py
    from django.urls import path
    from main.views import show_main
    app_name = 'main'
    urlpatterns = [
           path('', show_main, name='show_main'),]
    ```
    Impor path dari django.urls untuk mendefinisikan pola URL.
    Gunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkaitdiakses.
    Nama app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi.      
    Setelah itu, lakukan konfigurasi routing URL proyek, yaitu melalui urls.py 
    yang ada di folder proyek kita (BaritoInternational) bukan yang berada di folder main dengan sintaks:
    ```py
    from django.contrib import admin
    from django.urls import path, include
    urlpatterns = [
        path('', include('main.urls')),
        path('admin/', admin.site.urls),
    ]
    ```
    Fungsi include digunakan untuk mengimpor rute URL dari aplikasi lain (dalam hal ini, dari aplikasi main) kedalam berkas urls.py proyek.
    Path URL '' akan diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main. Path URL dibiarkanberupa string kosong agar halaman aplikasi main dapat diakses secara langsung.
    admin/ berarti jika kita mengakses "localhost:8000/admin" kita akan dirouting ke dalam page admin (Django)     
11. Terakhir tinggal jalakan servernya secara lokal, dengan cara mengeksekusi perintah berikut di CMD:
     ```s
        python manage.py runserver
    ```
    setelah ini, server kita telah berjalan secara lokal dan dapat diakses melalui browser pada tautan
    "http://localhost:8000" atau "http://127.0.0.1:8000/" 8000 merupakan port default untuk Django
12. Lakukan pengunggahan berkas pada PWS dengan cara buat proyek di home page dari PWS dan push kedalamnya
    jangan lupa tambahkan ALLOWED_HOST dengan URL deployment yang di miliki dengan konfogurasi :
    `<username-sso>-<nama proyek>.pbp.cs.ui.ac.id`, selanjutnya lakukan add dan commit lalu push ke pws
    dengan sintaks `git push pws main:master`
13. Bahagia `:)`

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Django_Routing](https://github.com/user-attachments/assets/47cd7ebc-a5a7-4c3c-a065-5d34cd7ee088)

Alur DBMS Django
1.  Client mengirimkan request ke Django.
2.  urls.py mencocokkan URL dengan view.
3.  views.py mengeksekusi logika aplikasi.
4.  models.py berinteraksi dengan database jika diperlukan.
5.  views.py merender data ke dalam template HTML.
6.  HTTP response dikirimkan kembali ke Client sebagai tampilan web.

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git merupakan version control yang pasti digunakan oleh para developer. Dengan bantuan version kontrol seperti git, para developer dapat berkoklaborasi dengan dengan developer yang lain sehingga memudahkan pembuatan proyek dan membuat pembuatan proyek menjnadi lebih efisein. Dengan git, para developer dapat mengembangkan proyeknya dengan lebih rapi dan terstruktur. Kesimpulannya, Git membantu para developer bekerja secara lebih efisien, aman, dan terorganisir.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django adalah framework yang lengkap dengan banyak fitur bawaan, seperti autentikasi pengguna, panel admin,      penanganan form, dan fitur keamanan yang kuat. Hal ini membuat developer tidak perlu melakukan konfigurasi dari awal, sehingga mempercepat proses pengembangan aplikasi.

Struktur MVT (Model-View-Template) pada Django membantu pemula untuk lebih mudah memahami pengembangan aplikasi web. Pemisahan antara front-end dan back-end dilakukan dengan baik, sehingga aplikasi lebih terstruktur dan mudah dikelola.

Django juga dirancang untuk memiliki scalability yang tinggi, sehingga mampu menangani proyek mulai dari yang sederhana hingga yang sangat kompleks. Ini memberikan pengalaman nyata kepada pengembang dalam mengelola proyek dengan skala besar.

Keunggulan lain yang dimiliki Django adalah komunitas yang aktif dan dokumentasi yang lengkap. Dukungan komunitas yang luas memudahkan developer untuk menemukan solusi, sementara dokumentasi yang komprehensif sangat membantu dalam memahami fitur dan fungsionalitas Django.

Selain itu, Django juga memiliki ORM (Object-Relational Mapping) bawaan yang memudahkan pengembang berinteraksi dengan database tanpa harus menulis query SQL secara manual. Hal ini meningkatkan efisiensi dalam mengelola data dalam aplikasi.

## Mengapa model pada Django disebut sebagai ORM?
Model Django disebut ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara objek Python dan tabel dalam database relasional. Dengan ORM, pengembang bisa mengelola data melalui objek tanpa harus menulis query SQL secara manual. ORM memudahkan operasi CRUD (Create, Read, Update, Delete), menyediakan portabilitas antar-database, serta meningkatkan keamanan dengan melindungi aplikasi dari SQL injection.


---
## Tugas 3 - PBP 24/25

##  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian sebuah platform untuk memastikan bahwa data dapat diakses, diproses, dan didistribusikan secara efisien dan andal di antara berbagai komponen sistem dan end user. Hal ini berpengaruh terhadap performa secara keseluruhan, bila mana data tidak dikirimkan dengan tepat waktu maka akan terjadi kegagalan dalam pengiriman atau waiting sehingga menyebabkan keterlambatan bahkan kehilagan data atau paket (paket loss). Selain itu, data delivery juga memungkinkan integrasi antar berbagai layanan atau modul dalam platform, serta mendukung pengalaman pengguna yang lancar dan efisien.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, saya lebih menyukai XML dariapada JSON, mengapa? mungkin dikarenaan saya lebih terbiasa untuk membaca file dalam format XML daripada JSON. JSON sendiri lebih populer dibandingkan dengna XML dikarenakan JSON lebihi simpel (ringkas) dan fleksibel. Selain itu, JSON sendiri juga mendapat dukungan langsung dari JavaScript menjadikannya lebih mudah diimplementasikan dalam aplikasi berbasis WEB. Terakhir, mungkin sebagian orang merasa JSON lebih mudah dipahami karena sintaks yang lebih sederhana.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi is_valid() yang telah kita buat bertujuan untuk memvalidasi input user sesuai dengan tipe input yang kita inginkan. Jika data valid, maka method ini akan mengembalikan return True dan data dapat diproses lebih lanjut, seperti disimpan di dalam database atau di operasikan terlebih dahulu seperti operasi aritmatika dsb. baru dimasukkan kedalam database. Jika method ini mengembalika return False maka input user tidaklah valid sesuai apa yang kita inginkan (yang kita definisika input tipe datanya di dalam dbms). Tanpa menggunkana method ini kita tidak dapat memastikan apakah input yang dilakukan oleh user sudah sesuai dengan yang kita ingikan (valid) atau belum, hal ini dapat mengancam integritas data dan keamanan aplikasi itu sendiri.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token berguna untuk melindungi aplikasi dari serangan Cross-Site Request Forgery. Serangan ini terjadi ketika seorang attacker mengirimkan malicious request ke server. Jika kita tidak menyertakan csrf_token dalam form Django, penyerang dapat membuat skrip atau tautan yang secara otomatis mengirimkan permintaan ke server menggunakan kredensial pengguna yang sedang aktif. Tanpa token ini, server tidak dapat memverifikasi apakah permintaan yang diterima berasal dari sumber yang sah, sehingga memungkinkan penyerang untuk melakukan tindakan yang tidak diinginkan atas nama pengguna, seperti mengubah data atau melakukan transaksi tanpa izin. CSRF token berfungsi sebagai kunci unik yang dikirim bersama setiap permintaan formulir, memungkinkan server untuk memverifikasi bahwa permintaan tersebut berasal dari sumber yang sah dan bukan dari pihak ketiga yang berniat jahat. Dengan menggunakan csrf_token, aplikasi dapat mencegah tindakan yang tidak diinginkan atau berbahaya, seperti perubahan data atau transaksi tanpa izin, sehingga meningkatkan keamanan dan integritas aplikasi web.

