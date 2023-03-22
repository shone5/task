# views.py
from django.shortcuts import render
from Myapp.models import SalesData
import csv

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        upload_csv =SalesData.objects.all()
        for row in reader:
            SalesData.objects.create(
                status=row['status'],
                year=row['year'],
                quantity=row['quantity'],
                price=row['price']
            )
        return render(request, 'tables.html',{'upload_csv': upload_csv})
    return render(request, 'home_page.html')
