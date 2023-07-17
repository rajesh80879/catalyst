from decimal import Decimal
from django.shortcuts import render, redirect
import csv
from .models import Record
from django.contrib import messages
import io
from rest_framework import generics
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer
from django.db.models import Q

# Create your views here.

def query_builder(request):
    industry_data = Record.objects.values_list('industry', flat=True).distinct()
    year_founded = Record.objects.values_list('year_founded', flat=True).distinct()
    city = Record.objects.values_list('city', flat=True).distinct()
    state = Record.objects.values_list('state', flat=True).distinct()
    country = Record.objects.values_list('country', flat=True).distinct()


    return render(request, "query.html",
                  {"industry":industry_data,
                    "year":year_founded,
                    "city":city,
                    "state":state,
                    "country":country
                    })


def upload_data(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        if file:
            reader = csv.DictReader(io.TextIOWrapper(file, encoding='utf-8'))
            records = []
            for row in reader:
                year_founded_str = row['year founded']
                year_founded = Decimal(year_founded_str.replace(',', ''))  
                locality_parts = row['locality'].split(',')
                city = locality_parts[0].strip()
                state = locality_parts[1].strip()
                country = locality_parts[2].strip()
                record = Record(
                    name=row['name'],
                    domain=row['domain'],
                    year_founded=year_founded,
                    industry=row['industry'],
                    size_range=row['size range'],
                    city=city,
                    state=state,
                    country=country,
                    linkedin_url=row['linkedin url'],
                    current_employees=int(row['current employee estimate']),
                    total_employees=int(row['total employee estimate'])
                )
                records.append(record)
        else:
            messages.error(request, "Please upload a valid document")
            return redirect("dashboard")

        try:
            Record.objects.bulk_create(records)
            messages.success(request, "Data uploaded successfully")
            return redirect("dashboard")

        except Exception as ep:
            messages.error(request, "Something went Wrong")
            return redirect("dashboard")


class RecordCountView(generics.RetrieveAPIView):
    serializer_class = RecordSerializer
    
    def get(self, request, *args, **kwargs):
        industry = self.request.query_params.get('industry')
        year_founded = self.request.query_params.get('year')
        city = self.request.query_params.get('city')
        state = self.request.query_params.get('state')
        country = self.request.query_params.get('country')
        keyword = self.request.query_params.get('keyword')
        
        records = Record.objects.all()

        if keyword:
            records = records.filter(
                Q(industry__icontains=keyword) |
                Q(year_founded__icontains=keyword) |
                Q(city__icontains=keyword) |
                Q(state__icontains=keyword) |
                Q(country__icontains=keyword)
            )

        if industry:
            records = records.filter(industry__icontains=industry)

        if year_founded:
            records = records.filter(year_founded=year_founded)

        if city:
            records = records.filter(city=city)

        if state:
            records = records.filter(state=state)

        if country:
            records = records.filter(country=country)

        record_count = records.count()
        messages.success(request, f"{record_count} records found for the query")

        return render(request,"query.html")
