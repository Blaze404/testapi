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
            male = random.randint(400, 700)
            female = random.randint(300, 600)
            data[ str(previous_day.day) + ' ' + previous_day.strftime("%B")] = {
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
        data = {}
        start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')
        delta = (end_date - start_date).days
        data['0'] = {
            "male": random.randint(3, 10) * delta,
            "female": random.randint(2, 9) * delta,
        }
        data['10'] = {
            "male": random.randint(2, 9) * delta,
            "female": random.randint(1, 8) * delta,
        }
        data['20'] = {
            "male": random.randint(1, 5) * delta,
            "female": random.randint(1, 5) * delta,
        }
        data['30'] = {
            "male": random.randint(2, 5) * delta,
            "female": random.randint(1, 5) * delta,
        }
        data['40'] = {
            "male": random.randint(3, 6) * delta,
            "female": random.randint(4, 8) * delta,
        }
        data['50'] = {
            "male": random.randint(3, 7) * delta,
            "female": random.randint(3, 8) * delta,
        }
        data['60'] =  {
            "male": random.randint(4, 10) * delta,
            "female": random.randint(5, 10) * delta,
        }
        data['70'] = {
            "male": random.randint(3, 6) * delta,
            "female": random.randint(3, 6) * delta,
        }
        data['80'] = {
            "male": random.randint(1, 3) * delta,
            "female": random.randint(1, 3) * delta,
        }
        data['90'] = {
            "male": random.randint(1, 3) * delta,
            "female": random.randint(1, 3) * delta,
        }
        data['100'] = {
            "male": random.randint(0, 2) * delta,
            "female": random.randint(0, 2) * delta,
        }

        data['meta'] = {
            'ip_address': utilities.get_client_ip(request),
            'request_type': 'get',
            'response_type': 'json',
            'user_agent': request.META['HTTP_USER_AGENT']
        }

        return JsonResponse(data)


def patient_flow(request, start_date, end_date):
    if request.method == 'GET':
        data = {}
        start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')

        delta = (end_date - start_date).days

        data['9:00 a.m.'] = {
            "male": random.randint(5, 10) * delta,
            "female": random.randint(5, 10) * delta,
        }
        data['10:00 a.m.'] = {
            "male": random.randint(4, 9) * delta,
            "female": random.randint(4, 9) * delta,
        }
        data['11:00 a.m.'] = {
            "male": random.randint(4, 8) * delta,
            "female": random.randint(4, 8) * delta,
        }
        data['12:00 p.m.'] = {
            "male": random.randint(2, 5) * delta,
            "female": random.randint(1, 5) * delta,
        }
        data['1:00 p.m.'] = {
            "male": random.randint(2, 6) * delta,
            "female": random.randint(2, 5) * delta,
        }
        data['2:00 p.m.'] = {
            "male": random.randint(1, 3) * delta,
            "female": random.randint(1, 4) * delta,
        }
        data['3:00 p.m.'] = {
            "male": random.randint(0, 5) * delta,
            "female": random.randint(0, 4) * delta,
        }
        data['4:00 p.m.'] = {
            "male": random.randint(2, 4) * delta,
            "female": random.randint(2, 6) * delta,
        }
        data['5:00 p.m.'] = {
            "male": random.randint(3, 10) * delta,
            "female": random.randint(4, 10) * delta,
        }
        data['6:00 p.m.'] = {
            "male": random.randint(4, 13) * delta,
            "female": random.randint(4, 13) * delta,
        }
        data['7:00 p.m.'] = {
            "male": random.randint(3, 9) * delta,
            "female": random.randint(3, 9) * delta,
        }
        data['8:00 p.m.'] = {
            "male": random.randint(3, 9) * delta,
            "female": random.randint(3, 9) * delta,
        }
        data['9:00 p.m.'] = {
            "male": random.randint(2, 8) * delta,
            "female": random.randint(2, 8) * delta,
        }
        data['10:00 p.m.'] = {
            "male": random.randint(1, 4) * delta,
            "female": random.randint(1, 4) * delta,
        }

        data['meta'] = {
            'ip_address': utilities.get_client_ip(request),
            'request_type': 'get',
            'response_type': 'json',
            'user_agent': request.META['HTTP_USER_AGENT']
        }

        return JsonResponse(data)