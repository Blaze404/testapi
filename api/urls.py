from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('patient/count', views.patient_count, name='patient_count'),
    path('trend/<slug:start_date>/<slug:end_date>', views.trend, name='trend'),
]