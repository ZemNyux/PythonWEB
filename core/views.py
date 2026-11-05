from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'title': 'Головна'})

def news(request):
    return render(request, 'news.html', {'title': 'Новини'})

def management(request):
    return render(request, 'management.html', {'title': 'Керівництво компанії'})

def about(request):
    return render(request, 'about.html', {'title': 'Про компанію'})

def contacts(request, country=None):
    if country == 'france':
        return render(request, 'france.html')
    elif country == 'ukraine':
        return render(request, 'ukraine.html')
    elif country == 'austria':
        return render(request, 'austria.html')
    else:
        return render(request, 'contacts.html')