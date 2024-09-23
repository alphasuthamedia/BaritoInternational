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