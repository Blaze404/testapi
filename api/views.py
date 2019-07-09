from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import datetime
from . import utilities

# Create your views here.
def patient_count(request):
    if request.method == 'GET' or request.method == 'get':
        d = {
            'total_visits': random.randint(500, 700),
            'total_patients': random.randint(300, 500),
            'repeat_patients': random.randint(100, 300),
            'meta': {
                'ip_address': utilities.get_client_ip(request),
                'request_type': 'get',
                'response_type': 'json'
            }
        }
        return JsonResponse(d)


def trend(request, start_date, end_date):
    if request.method == 'GET' or request.method == 'get':
        # start_date = start_date
        start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')
        d = {
            'start_date': start_date,
            'end_date': end_date
        }
        return JsonResponse(d)
