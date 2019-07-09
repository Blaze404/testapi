from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('', views.index, name="homepage"),
    path('patient/count', views.patient_count, name='patient_count'),
]