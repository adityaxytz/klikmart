from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'klikmart',
        'npm' : '2306240074',
        'name': 'Aditya Dharma',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

# Create your views here.
