from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import datetime
from . import utilities

# Create your views here.
def patient_count(request):
    if request.method == 'GET' :
        d = {
            'total_visits': random.randint(500, 700),
            'total_patients': random.randint(300, 500),
            'repeat_patients': random.randint(100, 300),
            'meta': {
                'ip_address': utilities.get_client_ip(request),
                'request_type': 'get',
                'response_type': 'json',
                'user_agent': request.META['HTTP_USER_AGENT']
            }
        }
        return JsonResponse(d)


def trend(request, start_date, end_date):
    if request.method == 'GET' or request.method == 'get':
        # start_date = start_date
        start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')

        week_start = start_date - datetime.timedelta(days=start_date.weekday())
        last_week_start = end_date - datetime.timedelta(days=end_date.weekday())


        previous_day = week_start
        next_day = week_start + datetime.timedelta(days=7)

        data = {}

        while next_day <= last_week_start:
            male = random.randint(40, 70)
            female = random.randint(30, 60)
            data[ str(previous_day.day) +  previous_day.strftime("%B")] = {
                'male': male,
                'female': female,
                'week_start': previous_day.strftime("%d/%m/%Y"),
                'week_end': next_day.strftime("%d/%m/%Y"),
            }
            previous_day = next_day
            next_day = next_day + datetime.timedelta(days=7)

        start_date.strftime("%d/%m/%Y")

        data['meta'] = {
                'ip_address': utilities.get_client_ip(request),
                'request_type': 'get',
                'response_type': 'json',
                'user_agent': request.META['HTTP_USER_AGENT']
            }

        return JsonResponse(data)


def age(request, start_date, end_date):
    if request.method == 'GET':
        pass
