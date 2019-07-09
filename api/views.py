from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random

# Create your views here.
def patient_count(request):
    if request.method == 'GET' or request.method == 'get':
        d = {
            'total_visits': random.randint(500, 700),
            'total_patients': random.randint(300, 500),
            'repeat_patients': random.randint(100, 300)
        }
        return JsonResponse(d)