from django.shortcuts import render

def branches_list(request):
    return render(request, 'branches_list.html', {'title': 'Філії'})

def odesa(request):
    return render(request, 'odesa.html', {'title': 'Філія в Одесі'})

def orleans(request):
    return render(request, 'orleans.html', {'title': 'Філія в Орлеані'})