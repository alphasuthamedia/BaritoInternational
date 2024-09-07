from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'tagline' : 'Everything You Need, All in One Place.'
    }

    return render(request, "main.html", context)