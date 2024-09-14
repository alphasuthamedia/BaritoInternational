from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductEntryForm
from django.http import HttpResponse
from django.core import serializers

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

# Create your views here.
def show_main(request):
    # sementara semua produk diletakkan disini
    # karena belum belajar database
    product = Product.objects.all()

    context = {
        'tagline' : 'Everything You Need, All in One Place.',
        'product_entries' : product
    }

    return render(request, "main.html", context)

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