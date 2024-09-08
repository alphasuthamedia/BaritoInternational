from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    # sementara semua produk diletakkan disini
    # karena belum belajar database
    Product = [
        {
            'name': 'Dell XPS 13',
            'price': 1200,
            'description': 'Powerful ultrabook with stunning 4K display and incredible performance for multitasking.',
            'quantity': 15
        },
        {
            'name': 'Apple MacBook Pro 16"',
            'price': 2500,
            'description': 'High-performance laptop with M1 chip, perfect for creative professionals and heavy workloads.',
            'quantity': 8
        },
        {
            'name': 'Asus ROG Strix G15',
            'price': 1800,
            'description': 'Gaming laptop with AMD Ryzen processor, RTX 3070 GPU, and high-refresh-rate display for seamless gaming.',
            'quantity': 20
        },
        {
            'name': 'Logitech MX Master 3',
            'price': 100,
            'description': 'Advanced ergonomic mouse designed for precision and comfort with customizable buttons and smooth scroll wheel.',
            'quantity': 40
        },
        {
            'name': 'Razer DeathAdder V2',
            'price': 60,
            'description': 'Top-tier gaming mouse with ultra-fast response time and ergonomic design for long gaming sessions.',
            'quantity': 35
        },
        {
            'name': 'Corsair K95 RGB Platinum',
            'price': 150,
            'description': 'Premium mechanical keyboard with per-key RGB lighting and dedicated macro keys for maximum productivity.',
            'quantity': 25
        },
        {
            'name': 'HP Spectre x360',
            'price': 1400,
            'description': 'Sleek convertible laptop with 360-degree hinge, ideal for creative professionals and multimedia enthusiasts.',
            'quantity': 12,
        },
        {
            'name': 'Samsung Galaxy Tab S7',
            'price': 750,
            'description': 'High-performance tablet with S Pen, great for drawing, note-taking, and media consumption.',
            'quantity': 30
        },
        {
            'name': 'Sony WH-1000XM5',
            'price': 400,
            'description': 'Industry-leading noise-canceling headphones with long battery life and excellent sound quality.',
            'quantity': 50
        },
        {
            'name': 'Bose SoundLink Revolve',
            'price': 200,
            'description': 'Portable Bluetooth speaker with 360-degree sound, perfect for on-the-go music lovers.',
            'quantity': 45
        }
    ]

    context = {
        'tagline' : 'Everything You Need, All in One Place.',
        'products' : Product
    }

    

    return render(request, "main.html", context)