from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    PER_PAGE = 10
    # stations = []
    with open('data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
        # без фильтрации
        # stations = list(csv.DictReader(csvfile))

        # с фильтрацией
        reader = csv.DictReader(csvfile)
        stations = [{'Name': row['Name'], 'Street': row['Street'], 'District': row['District']} for row in reader]
        # так не работает, хотя видел в лекции пример через точку
        # stations = [{'Name': row.Name, 'Street': row.Street, 'District': row.District} for row in reader]

        # было с фильтрацией
        # reader = list(csv.DictReader(csvfile))
        # for row in reader:
        #     stations.append({
        #         'Name': row['Name'],
        #         'Street': row['Street'],
        #         'District': row['District']
        #     })

    paginator = Paginator(stations, PER_PAGE)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
