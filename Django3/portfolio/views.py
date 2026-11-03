from django.shortcuts import render


def bio_view(request):
  return render(request, 'bio.html')


def facts_view(request):
  return render(request, 'facts.html')


def city_info_view(request):
  return render(request, 'city_info.html')


def city_places_view(request):
  return render(request, 'city_places.html')