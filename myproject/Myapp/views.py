# views.py
from django.shortcuts import render
from Myapp.models import SalesData
from datetime import datetime

import csv


def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        stat = request.POST.get('status')
        # qty = request.POST.get('quantity')
        # prices = request.POST.get('price')
        year = request.POST.get('year')

        queryset = SalesData.objects.all()
        # if qty:
        #     queryset = queryset.filter(quantity=qty,status=stat,price=prices,year=year)
        if stat:
            queryset = queryset.filter(status__icontains=stat)
        # if prices:
        #     queryset = queryset.filter(price=prices)
        if year:
            queryset = queryset.filter(year__icontains=year)
        #
        #     upload_csv =SalesData.objects.filter(status__icontain=st)
        #     print("ooooooooooo")

        for row in reader:
            SalesData.objects.create(
                status=row['status'],
                orderno=row['orderno'],
                K=row['K'],
                M=row['M'],
                year=row['year'],
                quantity=row['quantity'],
                price=row['price']
            )


        return render(request, 'tables.html', {'queryset':queryset})
    return render(request, 'home_page.html')

# def filter_results(request):
#     quantity = request.GET.get('quantity')
#     price = request.GET.get('price')
#
#     queryset = SalesData.objects.all()
#     if quantity:
#         queryset = queryset.filter(quantity=quantity)
#     if price:
#         queryset = queryset.filter(price=price)
#
#     context = {'queryset': queryset}
#     return render(request, 'tables.html', context)
