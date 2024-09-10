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
