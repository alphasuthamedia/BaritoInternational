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

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Setelah berhasil mengimplementasikan Skeleton sebagai Kerangka Views, maka proyek kita kali ini sudah dinamik. Sebelum membuat form input data dan memasukkannya ke dalam model, ada baiknya kita ubah primary key yang tadinya incremental integer menjadi UUID, hal ini akan melindungi kita dari vulnerability IDOR. Sekarang tinggal kit abuat form nya yaitu forms.py di dalam direktori main yang nantinya berfungsi menjadi struktur from untuk menerima input dari user.
```py
    from django.forms import ModelForm
    from main.models import Product

    class ProductEntryForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "quantity"]
```
Setelah demikian, lakukan import redirect from django.shortcuts dan jangan lupa untuk import class ProductEntryForm yang telah kita buat di dalam forms.py tadi. lakukan ini di dalam views.py.
```py
    from django.shortcuts import render, redirect
    from main.forms import ProductEntryForm
```
Setelah ini, tambahkan fungsi dengan parameter request untuk mengirim form dan menambahkan Product jika dan hanya jika form yang diisi telah valid melalui request.POST buat juga fungsi yang mengecek apakah yang diinput oleh user merupakan input yang valid yang sesuai dengn apa yang kita inginkan. hal ini masih berada di views.py
```py
    def create_product_entry(request):
        form = ProductEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product_entry.html", context)
```

Kemudian pada fungsi show_main() di dalam views.py rubahlah variabel targe product menjadi product = Product.objects.all(), sebelumnya kita menghardcode product productnya, sekarang kita tinggal mengambilnya dari databse.
```py
    def show_main(request):
        product = Product.objects.all()

        context = {
            'tagline' : 'Everything You Need, All in One Place.',
            'product_entries' : product
        }

        return render(request, "main.html", context)
```
sekarang kita import fungsi create_product_entry dari dalam main.views ke dalam urls.py hal ini kita lakukan agar saya dapat menambahkannya kedalam urlpatterns dan buatlah path routingnya
```py
    from main.views import show_main, create_product_entry,

    path('create_product_entry', create_product_entry, name='create_product_entry'),
```
setelah demikian, kita tinggal buat create_product_entry.html di dalam main/templates, ini sebagai template form yang akan mengirim request ke view create_product_entry(request). sampai sini, kita sudah berhasil untuk membuat form meminta data data dari produk, mulai dari template, variable yang dimiliki oleh produk, hingga memasukkannnya kedalam databse. perlu di ingat, jika database tidak kosong sebelum kita mengganti format id menjadi UUID, kita harus menghapusnya terlebih dahulu (file db.sqlite3) mungkin ada cara untuk mengkonversinya, namun yang jelas hal tersebut tidak atau belum dicover untuk saat ini.

Sekarang kita tinggal tambahkan 4 fungsi di dalam views.py
```py
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
fungsi fungsi tersebut menserealisasi objek objek menjadi xml atau json sekaligus 2 fungsi paling bawah selain menampilkan objek objek yang telah terserealisasi, juga mengambilkan objek objek berdasarkan id.
terakhir, kita hanya perlu untuk mengimpur fungsi fungsi tersebut dan menambahkan routing di dalam urls.py yang ada di dalam main agar kita bisa mengakses fungsi fungsi tersebut berdasarkan routing yang kita inginkan
```py
    from main.views import show_main, create_product_entry, show_xml, show_json, show_json_by_id,show_xml_by_id

    path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. show_xml()
![show_XML](https://github.com/user-attachments/assets/954224cb-10d4-4092-a7ca-3f28f1154f01)
2. show_json()
![show_JSON](https://github.com/user-attachments/assets/69996a7c-7efa-4214-bcab-fffed2d08929)
3. show_xml_by_id()
![show_XML_by_id](https://github.com/user-attachments/assets/1e095555-c155-4181-bb53-7f89b79619ec)
4. show_json_by_id()
![show_JSON_by_id](https://github.com/user-attachments/assets/4cfde129-4661-42e4-88f7-4c35e80faab8)


---
## Tugas 4 - PBP 24/25

## Apa perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect() adalah method yang menghasilkan respon HTTP untuk melakukan redirecting ke URL tertentu. HttpResponseRedirect akan mengirimkan code status HTTP 302 kepada brower, hal ini untuk memberitahu kepada browser untuk mengunjungi url terrtenut.

example :
```py
from django.http import HttpResponseRedirect

def some_view(request):
    return HttpResponseRedirect('/my-personal-jokes/')
```

hal ini jika fungsi some_view tereksekusi baik melalui button dsb. maka akan mengredirect ke /my-personal-jokes/

redirect() adalah method yang sebenarnya mirip dengan HttpResponseRedirect, hanya saja redirect dapat menerima input berupa objek, model, view, or url. Dengan demikian method redirect memberikan kita fleksibilitas yang lebih.

```py
from django.shortcuts import redirect

def some_view(request):
    return redirect('/url/')  # Redirect ke URL spesifik (sama seperti HttpResponseRedirect)
    
def some_view_agai(request):
    return redirect('view_name')  # Redirect ke sebuah view yang ditunjuk
```

## Jelaskan cara kerja penghubungan model Product dengan User!
Model Product bisa saja dihubungkan dengan User melalui ForeignKey, sehingga Product akan dialokasikan berbeda sesuai dengan keynya, dengan kata lain akan selalu berbeda untuk setiap user yang telah login.
```py
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    quantity = models.IntegerField(default=0)

    # Representasi dari object
    def __str__(self):
        return (self.name + ' - ' + str(self.price) + ' - ' + self.description)
        
```
Setiap kali pengguna membuat Product maka entri product akan dikaitkan dengan user yang sedang login. parameter on_delete=models.CASCADE artinya jika pengguna dihapus, maka setiap entri Product juga akan dihapus.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Autentikasi (Authentication): Proses untuk memverifikasi identitas dari seseorang atau entitas. Dalam autentikasi, sistem memastikan bahwa pengguna atau entitas adalah benar siapa yang mereka klaim. Contoh autentikasi adalah login menggunakan username dan password, atau menggunakan biometrik seperti sidik jari atau pengenalan wajah.

Tujuan: Memastikan siapa pengguna tersebut.
Contoh: Pengguna memasukkan email dan password untuk mengakses akun mereka.

Proses : dalam django, autentikasi dapat dilakukan dengan melalui login, dimana pengguna dapat memasukkan kredensial mereka

Otorisasi (Authorization): Proses yang terjadi setelah autentikasi, di mana sistem menentukan apakah pengguna yang telah terautentikasi memiliki izin untuk mengakses sumber daya atau melakukan suatu tindakan. Otorisasi berfokus pada hak akses pengguna terhadap sumber daya tertentu dalam sistem.

Tujuan: Memastikan apa yang diizinkan untuk dilakukan oleh pengguna.
Contoh: Seorang pengguna dengan peran sebagai "admin" dapat mengakses dashboard manajemen, sementara pengguna biasa hanya bisa melihat profil mereka sendiri.
Perbedaan utama:

Autentikasi adalah tentang mengenali identitas pengguna.
Otorisasi adalah tentang mengontrol hak akses setelah identitas dikenali.
Secara umum, autentikasi terjadi sebelum otorisasi. Misalnya, setelah pengguna login (autentikasi), sistem memeriksa apakah mereka memiliki hak untuk melakukan tindakan tertentu (otorisasi).

proses : setelah pengguna berhasil melakukan autentikasi, django akan memeriksa hak atau izin yang dimiliki oleh pengguna tersebut

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django dapat mengingat pengguna yang telah login menggunakan Session, dan Cookies

Server : saat seorang pengguna telah berhasil melakukan login, maka django akan membuat catatan session untuk pengguna tersebut. informasi catatan session tersebut akan disimpan di dalam server dengan sebuah ID yang unik.

Cookies : Django akan mengirimkan ID session kepada pengguna (kepada browser pengguna) dalam bentuk Cookie. Cookie ini akan disimpan di dalam browser pengguna (ada kerentanan) dan nanti akan dikim kembali kepada server dalam setiap request berikutnya.

hal ini ketika pengguna masuk ke dalam sebuah lama, django akan memeriksa cookie yang telah dikirim dari klien, jika memang dirasa ID sesion masih valid (dan belum diterminate), django akan otomatis mengidentifikasi pengguna tersebut berdasarkan sesi terakhir yang disimpan di dalam server.

Kegunaan lain dari Cookies:
- Cookies dapat digunakan untuk menyimpan preferensi pengguna     seperti tema, mode gelap, dll. sehingga pengguna tidak perlu mengatur kembali setiap mengunjungi situs tersebut.
- Cookies juga dapat digunakan untuk menyimpan token otentikasi untuk API dan aplikasi web. sehingga memudahkan pengguna untuk tetap terautentikasi saat melakukan surf ke dalam sebuah laman.

Apakah semua cookies aman untuk digunakan? jawabnnya tidak. jika seseorang atau sebut saja attacker berhasil mengambil cookie kita, entah karena komputer telah terinfeksi dengan malware atau dengan menggunakan teknik yang lain, otomatis semua session ID yang tersimpan dalam cookies dan yang belum diterminate oleh server akan dapat dimanfaatkan oleh attacker untuk melakukan autentikasi menggunakan akun yang kita gunakan, karena cookies akan match dengan session yang masih disimpan oleh server.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Buatlah template untuk melakukan login dan registrasi, sebagai contoh saya menggunakan UserCreationForm.html dan login.html, ini berguna sebagai template yang nantinya akan dirender bersama views.py, letakkan dalam folder template aplikasi, lalu atur views.py sebagai berikut
```py
...
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
...

... (ini hanya simbol beberapa bagian dari views)
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')
...
```
2. Jangan lupa tambahkan dekorator agar user harus login terlebih dahulu dengan cara import :
```py
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/login')
def show_main():
    ...
```
3. Jangan lupa atur routingnya dengan menambahkan path yang mengcall fungsi fungsi yang ada di views serta buatkan atau reservasikan alamat seperti "/login/" , "/logout/" dll untuk nantinya diapangan ke dalam url atau diroutingkan kesitu.

4. tambahkan detail last_login dalam template. karena kita telah mengatur context maka data akan terpass ke template tersebut.
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
5. Hubungkan model dengan user -- telah dijelaskan diatas
6. jangan lupa untuk lakukan migrasi model dan aplikasikan migrasi yang telah kita buat sebelumnya
5. Buat akun pengguna dengan cara melakukan registrasi pada laman yang telah tersedia yaitu localhost:8000 lalu anda akan pasti diarahkan ke login page, namun anda dapat mengklik button register dan silahkan registrasi (2 user), didalamnya anda dapat langsung membuat keterangan mengenai produk, hal ini akan otomatis tersimpan berdasarkan user.

---
## Tugas 5 - PBP 24/25

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
prioritas css selector sebagai berikut:
1. origin & importance
2. selector spesificity 
3. order of appearance 
4. Initial & Inherited Properties (default values)

# origin
Author: CSS is provided by front-end developers.
User: The browser user can customize styles, such as font and color, for their own browser.
User-Agent: Browsers apply default styles, which can vary across different browsers.
# importance (!important
prioritas penerapan CSS tersebut bergantung pada spesifisitas. Spesifisitas adalah cara browser memilih gaya mana yang akan diterapkan ketika terdapat aturan yang bertentangan. Setiap selector memiliki tingkat spesifisitas yang berbeda, dengan urutan prioritas sebagai berikut:

!important
Deklarasi !important memiliki prioritas tertinggi. Ketika ditambahkan, aturan tersebut akan mengesampingkan aturan lain, bahkan jika spesifisitasnya lebih rendah.

Inline styles
Gaya yang ditulis langsung dalam atribut style elemen HTML memiliki prioritas tinggi, kecuali bila dibandingkan dengan !important.

ID selector (#id)
Selector berbasis ID memiliki spesifisitas lebih rendah dari inline styles, tetapi lebih tinggi dibandingkan class selector.

Class selector (.class), Attribute selector ([attr]), dan Pseudo-class (
)
Selector ini memiliki tingkat spesifisitas yang sama.

Element selector (tag) dan Pseudo-element (::before, ::after)
Kedua selector ini juga memiliki nilai spesifisitas yang sama, tetapi di bawah class selector.

Universal selector (*) dan Combinators (+, >, ~, " ")
Selector ini memiliki prioritas terendah.

Selain itu, ada dua aturan tambahan:

Cascading: Jika ada dua aturan dengan spesifisitas yang sama, aturan yang ditulis paling akhir akan diprioritaskan.
Inheritance: Beberapa properti CSS diwariskan dari elemen induk ke anaknya, tetapi aturan yang langsung diterapkan pada elemen akan lebih diutamakan.
Spesifisitas dapat dihitung sebagai empat angka (a-b-c-d), di mana:

a = jumlah inline styles
b = jumlah ID selectors
c = jumlah class, attribute, dan pseudo-class selectors
d = jumlah element dan pseudo-element selectors)

Spesifisitasnya adalah 0-1-2-1:

0 (inline style)
1 (ID selector: #content)
2 (class selectors: .data dan .highlight)
1 (element selector: td)

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Desain responsif telah menjadi salah satu konsep kunci dalam pengembangan aplikasi web masa kini, terutama karena pola perilaku pengguna yang semakin beragam. Di era digital saat ini, orang mengakses konten web menggunakan berbagai macam perangkat dengan ukuran layar yang bervariasi, mulai dari perangkat kecil seperti smartphone, hingga perangkat berukuran menengah seperti tablet, dan perangkat berlayar besar seperti laptop serta desktop. Setiap perangkat memiliki karakteristik tampilan yang berbeda, baik dari segi resolusi, orientasi layar, maupun interaksi pengguna.

Desain responsif bertujuan untuk memberikan pengalaman terbaik bagi pengguna, terlepas dari perangkat apa yang mereka gunakan. Hal ini dicapai dengan menerapkan teknik-teknik seperti grid fleksibel, media query, serta gambar dan elemen yang dapat beradaptasi dengan ukuran layar. Dengan desain responsif, konten dan tata letak website dapat berubah secara dinamis agar sesuai dengan ukuran layar, memastikan bahwa pengguna dapat mengakses dan menjelajahi situs web dengan mudah dan nyaman tanpa harus memperbesar atau menggulir secara berlebihan.

Selain memberikan pengalaman yang konsisten dan optimal bagi pengguna, desain responsif juga lebih efisien dari segi pengelolaan situs web. Daripada membuat versi terpisah untuk desktop dan mobile, yang memerlukan pemeliharaan dan pengembangan ganda, satu situs responsif memungkinkan pengembang untuk memelihara hanya satu basis kode. Hal ini tidak hanya menghemat waktu dan sumber daya, tetapi juga memastikan bahwa semua pengguna, tanpa memandang perangkat yang mereka gunakan, selalu mendapatkan versi situs yang terbaru dan teroptimalisasi. Ini membuat desain responsif menjadi solusi yang lebih ekonomis dan efektif dalam jangka panjang bagi pengembang dan pemilik situs.

# Aplikasi yang Sudah Menggunakan Desain Responsif:
Facebook
Facebook menggunakan desain responsif yang memastikan tampilannya optimal di berbagai perangkat, dari smartphone hingga desktop, sehingga pengguna mendapatkan pengalaman yang konsisten.

Twitter
Twitter menerapkan desain responsif dengan baik, memungkinkan pengguna untuk mengakses dan menavigasi konten dengan nyaman di semua ukuran layar.

Amazon
Amazon memiliki desain responsif yang memungkinkan pelanggan untuk berbelanja dengan mudah dari perangkat apapun, baik itu smartphone, tablet, atau desktop.

YouTube
YouTube memastikan bahwa antarmuka pengguna dan kontennya berfungsi dengan baik di semua perangkat, sehingga pengguna dapat menonton video dan berinteraksi dengan situs tanpa masalah.

Google
Situs pencarian dan produk-produk Google seperti Gmail, Google Drive, dan Google Docs memiliki desain responsif yang dioptimalkan untuk berbagai perangkat, memberikan pengalaman yang konsisten dan nyaman.

# Aplikasi yang Belum Menggunakan Desain Responsif:
Craigslist
Craigslist, situs iklan baris, masih memiliki desain yang sangat dasar dan belum sepenuhnya responsif. Pengalaman pengguna di perangkat mobile sering kali tidak optimal, dengan teks dan gambar yang sulit diakses.

Reddit (versi lama)
Versi lama Reddit tidak responsif dan sulit digunakan di perangkat mobile. Meskipun Reddit kini telah diperbarui dengan desain responsif, pengguna versi lama mungkin masih merasakan pengalaman yang tidak optimal di layar yang lebih kecil.

Aplikasi Internal Perusahaan Lama
Banyak aplikasi web internal dari perusahaan-perusahaan besar yang belum diperbarui ke desain responsif. Aplikasi ini sering kali didesain hanya untuk desktop dan memberikan pengalaman yang buruk ketika diakses dari perangkat mobile.

Beberapa Situs Pemerintah Tua
Beberapa situs web pemerintah yang lebih tua masih menggunakan desain yang tidak responsif. Mereka biasanya hanya dioptimalkan untuk tampilan desktop, dan pengguna di perangkat mobile mungkin kesulitan mengakses konten atau navigasi.

Small Niche Websites
Banyak situs web kecil atau blog niche yang belum diperbarui dengan desain responsif, terutama jika mereka dibangun sebelum responsif menjadi standar. Ini menyebabkan tampilan yang kurang baik pada perangkat mobile.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin adalah ruang di luar batas elemen yang memisahkan elemen tersebut dari elemen lain di sekitarnya. Margin bersifat transparan.
- Border adalah garis yang mengelilingi padding dan konten elemen. Border dapat terlihat, namun juga bisa dibuat tidak terlihat (invisible).
- Padding adalah ruang antara konten elemen dan bordernya. Padding juga bersifat transparan.

```css
    .element {  /* Selector */
    margin: 10px;                 /* Semua sisi */
    margin: 10px 20px;            /* Atas-bawah | Kiri-kanan */
    margin: 10px 20px 15px 25px;  /* Atas | Kanan | Bawah | Kiri */
    margin-top: 15px;             /* Khusus untuk sisi tertentu */
}

```

```css
    .element {  /* Selector */
    border: 1px solid black;      /* Lebar | Gaya | Warna */
    border-width: 2px;            /* Khusus lebar */
    border-style: dashed;         /* Khusus gaya */
    border-color: red;            /* Khusus warna */
    border-radius: 5px;           /* Untuk sudut melengkung */
}

```

```css
.element {  /* Selector */
    padding: 10px;                 /* Semua sisi */
    padding: 10px 20px;            /* Atas-bawah | Kiri-kanan */
    padding: 10px 20px 15px 25px;  /* Atas | Kanan | Bawah | Kiri */
    padding-left: 15px;            /* Khusus untuk sisi tertentu */
}

```
Perlu diperhatikan bahwa margin, border, dan padding semuanya mempengaruhi ukuran total elemen. Misalnya, jika lebar elemen diatur menjadi 100px dengan padding 10px di setiap sisi, maka lebar total elemen tersebut akan menjadi 120px (100px + 10px + 10px).

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox adalah metode tata letak satu dimensi yang digunakan untuk mengatur elemen dalam baris atau kolom. Flexbox menyediakan cara yang lebih efektif untuk mendistribusikan ruang dan menyelaraskan konten dalam sebuah container, bahkan ketika ukurannya bersifat dinamis atau belum diketahui. Flexbox sangat berguna saat kita ingin mengatur tata letak dalam satu arah (baik horizontal maupun vertikal). Contohnya, jika Anda ingin menempatkan beberapa elemen di tengah halaman, flexbox adalah pilihan yang tepat. Selain itu, flexbox memberikan fleksibilitas lebih dalam menyelaraskan setiap item secara individual.flexbox berguna Mengatur elemen secara dinamis dalam satu baris atau kolom, memungkinkan elemen untuk menyesuaikan ukuran dengan memperbesar atau memperkecil sesuai ruang yang tersedia.

Grid layout adalah sistem tata letak dua dimensi yang memudahkan pengembang dalam menciptakan desain halaman yang lebih kompleks dan konsisten menggunakan baris dan kolom. Grid layout memungkinkan pengaturan konten secara simultan dalam baris dan kolom, memberikan fleksibilitas untuk membagi halaman menjadi area yang terdefinisi dengan jelas. Pengembang dapat dengan mudah membuat struktur grid dengan baris dan kolom yang berbeda serta menyesuaikan ukuran setiap sel, yang memberikan kontrol lebih besar atas keseluruhan layout. Grid layout sangat ideal untuk menciptakan tampilan yang rapi dengan kolom yang tetap lebar dan tata letak yang terstruktur secara tepat. grid layout dapat digunakan untuk Menyusun tata letak dua dimensi dengan baris dan kolom, sangat ideal untuk desain yang terstruktur serta membutuhkan fleksibilitas dalam penyesuaian lebar baris dan kolom.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. konfigurasikan static files django, tambahkan baris kode ini pada settings.py
```py
# Static files (CSS, JavaScript, Images)
# Dokumentasi: https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'# Static files (CSS, JavaScript, Images)
```
STATIC_URL adalah URL yang dapat diakses oleh publik, yang digunakan untuk mengakses dan mendapatkan file statis, seperti gambar, CSS, dan JavaScript, dari aplikasi. URL ini memungkinkan pengguna untuk mengambil file statis yang diperlukan untuk menampilkan konten halaman web dengan benar.

STATIC_ROOT adalah path absolut yang menunjuk ke direktori tempat file statis akan dikumpulkan ketika perintah collectstatic dijalankan dalam proyek. Direktori ini digunakan untuk menyimpan semua file statis agar dapat diakses ketika aplikasi berada dalam mode produksi (dengan pengaturan DEBUG=False di settings.py), sehingga konten statis dapat diakses oleh pengguna.

2. Install Framwork TilWind
Dengan menggunakan framework tailwind, memudahkan kita untuk melakukan styliing pada website kita. Pemasangan tailwind dapat menggunakan Play CDN (seperti pada tutorial) atau menggunakan TailWind via npm.

3. Buat tempplate template yang diperlukan seperti product_card.html
```html
<div class="bg-gray-300 rounded-lg p-6 max-w-xs m-4">
    <h2 class="text-gray-700 font-bold text-xl mb-2">{{ product_entry.name }}</h2>
    <p class="text-gray-700 mb-4">{{ product_entry.description }}</p>
    <p class="text-gray-600 font-semibold">Price: Rp {{ product_entry.price }}</p>
    <p class="text-gray-600">Quantity: {{ product_entry.quantity }}</p>
    
    <div class="mt-4 flex justify-start">
      <!-- Edit button -->
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg transform hover:scale-105 transition duration-300 ease-in-out py-2 px-4 rounded">
        Edit
      </a> 
      
      <!-- Delete button with margin left -->
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="text-white bg-red-500 hover:bg-red-600 hover:scale-105 transition duration-300 ease-in-out py-2 px-4 ml-10 rounded">
        Delete
      </a>
    </div>
    
  </div>
```
Product card digunakan untuk menampilkan produk kita dalam bentuk card-card, karena kita men include product_card.html kita dalam main, maka data yang dikirim dari view ke main akan dikirim ke product_card
Selain itu kita buat navbar.html yang berguna untuk menampilkan navigation bar
```html
<nav class="">
    <div class="max-w-full mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16 items-center">
        <!-- Welcome text on the left -->
        <div class="flex items-center">
          {% if user.is_authenticated %}
            <div class="flex flex-col">
                <span class="text-gray-300 text-2xl font-mono">Welcome, {{ user.username }}</span>
                <span class="text-gray-300 text-sm font-mono">Sesi terakhir login: {{ last_login }}</span>
            </div>
          {% endif %}
        </div>
        
        <!-- Login/Logout buttons on the right -->
        <div class="hidden md:flex items-center group">
            <a href="/" class="text-center font-sans bg-violet-700 hover:bg-violet-800 text-white font-bold py-2 
              px-9 rounded-lg shadow-lg transform hover:scale-105 transition duration-300 ease-in-out mr-4">
              Home
            </a>
          {% if user.is_authenticated %}
            <a href="{% url 'main:logout' %}" class="text-center font-sans bg-red-500 hover:bg-red-600 text-white font-bold py-2 
            px-6 rounded-lg shadow-lg transform hover:scale-105 transition duration-300 ease-in-out">
              Sign Out
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Register
            </a>
          {% endif %}
          
        </div>
  
        <!-- Mobile menu button on the right -->
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
  
    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
      <div class="flex flex-col pt-2 pb-3 space-y-1 mx-auto">
        <div class="text-center font-sans bg-violet-700 hover:via-violet-800 text-white font-bold py-2 px-6
           rounded shadow-lg transform hover:scale-105 transition duration-300 ease-in-out">
            <a href="/" class="text-center text-white font-bold py-2 px-6 rounded-lg font-sans">
              Home
            </a>
          </div>
        {% if user.is_authenticated %}
          <a href="{% url 'main:logout' %}" class="text-center font-sans bg-red-500 hover:bg-red-600 text-white font-bold py-2 
          px-6 rounded shadow-lg transform hover:scale-105 transition duration-300 ease-in-out">
            Sign Out
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
    </div>
    
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
  
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
</nav>
```
tambahkan edit_product.html yang bisa kita gunakan untuk mengedit atau merubah objek objek objek yan gusdah ditambahkan sebelumnya
```html
{% extends 'base.html' %}

{% load static %}

{% block content %}

<div class="bg-gradient-to-b from-black via-[#121212] to-[#292929] min-h-screen">
      <!-- Navbar -->
    <div class="p-6">
        {% include 'navbar.html' %}
    </div>

    <h1 class="flex justify-center text-4xl font-sans mb-6 mt-12 text-white">Edit Product Entry</h1>

    <div class=" flex justify-center mt-4 items-center">
        <div class="bg-gray-300 shadow-lg rounded-lg p-8 max-w-4xl w-full">
            <!-- Form Section -->
            <form method="POST" class="grid grid-cols-2 gap-6 w-full">
                {% csrf_token %}
                
                <!-- Left Column for product name, price, quantity, and submit button -->
                <div class="space-y-6">
                <!-- Product name Input -->
                <div>
                    <label for="name" class="font-sans">Nama Produk</label>
                    <input type="text" name="name" id="name" placeholder="Masukkan nama produk"
                    value= "{{ product.name }}" 
                    class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none font-sans text-gray-900" 
                    required>
                </div>

                <!-- Product price Input -->
                <div>
                    <label for="price" class="font-sans">Harga Produk</label>
                    <input type="number" name="price" id="price" placeholder="Masukkan harga produk" 
                    class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none font-sans text-gray-900 appearance-none"
                    value="{{ product.price }}"
                    min="1" oninput="this.value = Math.abs(this.value)" required>
                </div>

                <!-- Product quantity Input -->
                <div>
                    <label for="quantity" class="font-sans">Jumlah Produk</label>
                    <input type="number" name="quantity" id="quantity" placeholder="Masukkan jumlah produk" 
                    class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none font-sans text-gray-900 appearance-none"
                    value="{{ product.quantity }}"
                    min="1" oninput="this.value = Math.abs(this.value)" required>
                </div>

                <!-- Submit button -->
                <div class="mt-6">
                    <input type="submit" value="Edit Product Entry"
                    class="w-full font-sans bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg transform hover:scale-105 transition duration-300 ease-in-out py-2 px-4 rounded">
                </div>
                </div>

                <!-- Right Column for product description -->
                <div class="flex flex-col justify-start">
                <!-- Product description Input -->
                <label for="description" class="font-sans">Deskripsi Produk</label>
                <textarea name="description" id="description" placeholder="Deskripsikan produk anda" 
                    class="w-full h-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none font-sans text-gray-900"
                    required>{{ product.description }}</textarea>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```
pastikan anda telah membuat routing untuk edit produk di urls.py
```py
    from main.views import edit_product
    ...
    path('edit/<uuid:id>', edit_product, name='edit_product'),
    ...
```

dan jangan lupa konfigurasikan views, dan kirim data berupa pk dari object yang kita select
```py
def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form,
               'product': product,
               'last_login': request.COOKIES['last_login'],}
    return render(request, "edit_product.html", context)
```

selanjutnya kita dapat menyesuaikan setiap komponen dalam dbms jika memang kita ingin mendesain website kita sedemikian rupa, seperti contoh saya merubah beberapa fungsi di dalam vies sehingga saya dapat memastikan data data yang saya butuhkan di passed ke dalam template yang dirender.

temp val untuk push pws attemt-6

---
## Tugas 6 - PBP 24/25

## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript berperan penting dalam membuat halaman web menjadi dinamis, interaktif, serta meningkatkan pengalaman pengguna. Dengan JavaScript, pengembang dapat menambahkan fitur-fitur interaktif yang tidak bisa diwujudkan hanya dengan HTML dan CSS, seperti form validasi dan dropdown. JavaScript memiliki ekosistem pengembangan web yang unggul, didukung oleh komunitas besar serta beragam library dan framework seperti React, Angular, dan Vue.js untuk pengembangan front-end, serta Node.js untuk back-end. JavaScript telah menjadi standar yang diakui oleh semua browser modern, dan fleksibilitasnya memungkinkan pengembangan web yang responsif dan lintas platform.

Keunggulan JavaScript dalam pengembangan aplikasi web meliputi kemampuannya untuk membuat elemen interaktif, memanipulasi elemen di halaman web secara dinamis (DOM), serta memungkinkan komunikasi asinkron dengan server menggunakan XMLHttpRequest atau fetch(), yang membuat aplikasi lebih responsif tanpa perlu memuat ulang halaman. JavaScript juga mendukung pengembangan aplikasi lintas platform karena dapat berjalan di hampir semua browser modern. Dengan framework atau library seperti React, Angular, dan Vue, JavaScript memungkinkan pembuatan aplikasi web yang efisien dengan konsep Single Page Application (SPA), di mana hanya sebagian halaman yang diperbarui untuk menjaga performa.

## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
fetch() adalah fungsi bawaan JavaScript yang digunakan untuk mengambil data dari URL dan mengembalikannya dalam bentuk Promise, yang bisa berhasil (resolve) atau gagal (reject). Keyword await memungkinkan JavaScript untuk menunggu hingga Promise selesai (resolved) sebelum melanjutkan ke kode berikutnya, namun hanya bisa digunakan dalam fungsi yang bersifat asynchronous (dideklarasikan dengan kata kunci async). Saat kita menggunakan await bersama fetch(), kita menunda eksekusi fungsi asynchronous hingga respons dari server diterima, membuat kode lebih mudah dibaca karena terlihat seperti operasi synchronous. Tanpa menggunakan await, kode berikutnya akan dieksekusi segera setelah fetch() dipanggil, tanpa menunggu data sepenuhnya diambil, yang dapat menyebabkan masalah jika data belum tersedia ketika diperlukan. Selain await, kita juga dapat menggunakan then() untuk menangani Promise dari fetch(), tetapi penggunaan then() dapat membuat kode sulit dibaca, terutama jika ada banyak operasi asynchronous yang saling bergantung.

```py
  const response = fetch('url'); // Mengembalikan Promise
  const data = response.json();   // Ini akan dieksekusi sebelum response selesai
```

```py
  const response = await fetch('url');
  const data = await response.json(); // Menunggu response selesai
```

## Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Decorator csrf_exempt memungkinkan Django untuk mengabaikan pengecekan csrf_token pada POST request yang dikirimkan ke fungsi tersebut.

Decorator @csrf_exempt digunakan untuk mengecualikan view dari perlindungan Cross-Site Request Forgery (CSRF) di Django. Mekanisme CSRF biasanya digunakan untuk mencegah serangan di mana pengguna secara tidak sengaja mengirim permintaan yang berbahaya. Namun, dalam beberapa situasi seperti saat menggunakan AJAX untuk POST request, token CSRF tidak selalu terkirim secara otomatis, sehingga bisa muncul error jika POST dilakukan tanpa token CSRF yang valid. Dengan menambahkan @csrf_exempt pada view, Django akan mengabaikan pemeriksaan token CSRF pada request tersebut.

Namun, menonaktifkan CSRF harus dilakukan dengan hati-hati dan hanya jika benar-benar diperlukan karena dapat menimbulkan risiko keamanan. Alternatif yang lebih aman adalah menyertakan token CSRF dalam header AJAX request.


Token CSRF tidak otomatis dikirim bersama POST request yang dilakukan melalui AJAX karena mekanisme pengiriman token CSRF pada permintaan HTTP berbeda dengan cara AJAX beroperasi. Secara default, Django mengharapkan token CSRF untuk dikirim bersama form submission dalam request POST melalui cookie atau sebagai bagian dari form data. Namun, dalam AJAX request, permintaan dilakukan secara programatis menggunakan JavaScript, dan tidak selalu mengikuti alur pengiriman form standar.

Ada beberapa alasan mengapa token CSRF tidak dikirim otomatis dalam AJAX request:

- Header Tidak Disertakan Secara Default: AJAX request tidak secara otomatis mengirimkan token CSRF di header atau body request. Untuk melakukannya, token CSRF perlu secara eksplisit disertakan oleh JavaScript dalam header atau payload POST request.

- Perbedaan dengan Form HTML Biasa: Saat menggunakan form HTML biasa, Django secara otomatis menambahkan token CSRF ke form melalui tag tersembunyi (<input type="hidden" name="csrfmiddlewaretoken">). Namun, dalam AJAX, karena pengiriman dilakukan melalui JavaScript dan bukan form HTML, token ini tidak disertakan kecuali diproses secara manual.

- Cross-Domain Request: Jika AJAX request dilakukan ke domain yang berbeda, browser tidak akan menyertakan cookie CSRF secara otomatis untuk alasan keamanan, sehingga token harus disertakan dengan metode lain.

##  Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Jika pembersihan hanya dilakukan di frontend, penyerang masih bisa menyuntikkan kode berbahaya ke dalam input dan mengirimkannya ke backend. Backend yang tidak melakukan validasi ulang dapat mengeksekusi kode tersebut, memungkinkan penyerang untuk mencuri data pengguna, merusak situs web, termasuk melakukan SQL Injection. Serangan SQL Injection memungkinkan penyerang menyuntikkan kode SQL ke dalam input pengguna untuk memanipulasi basis data. Jika pembersihan hanya dilakukan di frontend, penyerang dapat melewati validasi dan mengeksekusi perintah SQL berbahaya di backend.

## Step By Step Minggu ini
Pada dasrnya kita akan membuat Adjax GET dan AJAX POST

Lakukan Perubahan pada fungsi yang ada di views.py yaitu ganti filtering product menjadi seperti berikut
```py
  data = Product.objects.filter(user=request.user)
```
mengapa? karena data dari show_json nantinya lah yang akan kita GET 

buatlah ajax getProductEntries di dalam berkas main.html

```html
  async function getProductEntries(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json());
    }
```

pastikan kita mengset async, dikarenakan kita ingin get produknya asinkronuss, nah dari sinilah show_json akan di get berdasarkan user dan akan dilakukan parse pada data JSON menjadi objek js

setelah selesai semua, rubah template main yang tadinya menggunakan product card, dan card ambil data secara langsung, kini sesuaikan di main.html dan pengambilan data secara asinkronus tadi menggunakan js.

```html
// Jika tidak ada produk, tampilkan gambar "sedih-banget"
      if (productEntries.length === 0) {
        const name = DOMPurify.sanitize(item.fields.name);
        const description = DOMPurify.sanitize(item.fields.description);
        htmlString = `
          <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-72 h-72"/>
            <p class="text-center text-gray-600 mt-4">Belum ada data produk pada sistem.</p>
          </div>
        `;
      } else {
        // Tampilkan data produk dalam bentuk card
        productEntries.forEach((item) => {
          htmlString += `
            <div class="bg-gray-300 rounded-lg p-3 min-w-[250px] max-w-md m-4">
              <h2 class="text-gray-700 font-bold text-xl mb-2">${item.fields.name}</h2>
              <p class="text-gray-700 mb-4">${item.fields.description}</p>
              <p class="text-gray-600 font-semibold">Price: Rp ${item.fields.price}</p>
              <p class="text-gray-600">Quantity: ${item.fields.quantity}</p>

              <!-- Tombol Edit dan Hapus -->
              <div class="flex justify-end space-x-2 mt-4">
                <a href="/edit/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                  </svg>
                </a>
                <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                </a>
              </div>
            </div>
          `;
        });
      }

      // Masukkan HTML produk ke dalam kontainer
      productContainer.innerHTML = htmlString;
    }
```
sampai disini kita sudah mengimplementasikan GET menggunakan ajax

Sekarang kita akan mengimplementasikan method POST dengan menggunakan ajax
pertama kita setup function yang ada di views.py
```py
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    quantity = request.POST.get("quantity")
    user = request.user
    
    new_product = Product(
        name=name, price=price,
        description=description, quantity=quantity,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```
function ini nanti akan di call, oleh karena itu kita membutuhkan routing
kedua kita buat routingn yang digunakan sebagai tombol 
tambahkan saja 
```py
path('create-product-entry-ajax', add-product_entry_ajax, name='add-product_entry_ajax'),
```
di dalam urlpatterns yang ada di urls.py

setelah 2 hal tersebut disetup, sekarang kita siapkan modal sebagai form untuk menambahkan product
```html
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
  <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
    <!-- Modal header -->
    <div class="flex items-center justify-between p-4 border-b rounded-t">
      <h3 class="text-xl font-semibold text-gray-900">
        Add New Mood Entry
      </h3>
      <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
        <span class="sr-only">Close modal</span>
      </button>
    </div>

    <!-- Modal body -->
    <div class="px-6 py-4 space-y-6 form-style">
      <form id="productEntryForm">
        <div class="mb-4">
          <label for="name" class="block text-sm font-medium text-gray-700">Product Name</label>
          <input type="text" id="name" name="name" class="mt-1 block w-full border text-black border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter your product name" required>
        </div>
        <div class="mb-4">
          <label for="description" class="block text-sm font-medium text-gray-700">Product Description</label>
          <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border text-black border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Describe your product(s)" required></textarea>
        </div>
        <div class="mb-4">
          <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
          <input type="number" id="price" name="price" min="1" class="mt-1 block w-full border text-black border-gray-300 rounded-md p-2 hover:border-indigo-700" required placeholder="Enter the product's price">
        </div>
        <div class="mb-4">
          <label for="quantity" class="block text-sm font-medium text-gray-700">Quantity</label>
          <input type="number" id="quantity" name="quantity" min="1" class="mt-1 block w-full border text-black border-gray-300 rounded-md p-2 hover:border-indigo-700" required placeholder="Enter the quantity">
        </div>
      </form>
    </div>
    <!-- Modal footer -->
    <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
      <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
      <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
    </div>
  </div>
</div>
```

lalu dengan bantuan html dom, kita buat agar modal yang sudah kita buat bisa berfungsi (show / hided)
```js
// Tambahkan event listener untuk tombol "Add New Product Entry"
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modal.classList.remove('hidden'); 
        setTimeout(() => {
          modalContent.classList.remove('opacity-0', 'scale-95');
          modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
          modal.classList.add('hidden');
        }, 150); 
    }

    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);
```

Sekarang tinggal kita tambahkan button ajah (ni ga selese selesai dah)
```html
<!-- Add New Product Button -->
    <div class="flex justify-end px-6 mt-8 gap-x-4">
      <a href="{% url 'main:create_product_entry' %}">
        <button class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
          Add New Product Entry
        </button>
      </a>
      <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
        Add New Product Entry by AJAX
      </button>
    </div>
```

namun modal yang kita buat tadi masih belum bisa mengirimkan data, kita butuh bantuan js untuk ini dengna cara
```js
function addProductEntry() {
    fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => refreshProductEntries())

    document.getElementById("productEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
    }
```

setelah itu bikin event listener agar jika submit ada event dia akan call 2 fungsi salah satunya addMoodEntry()
```js
document.getElementById("productEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProductEntry();
    })
```

DONE -__-, dah yak PBP, jangan ngereog bismillah UTS 100/100 ameeeeeen