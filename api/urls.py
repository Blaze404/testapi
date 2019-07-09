from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('patient/count', views.patient_count, name='patient_count'),
]