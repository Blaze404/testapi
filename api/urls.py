from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('patient/count', views.patient_count, name='patient_count'),
    path('trend/<slug:start_date>/<slug:end_date>', views.trend2, name='trend'),
    path('age/<slug:start_date>/<slug:end_date>', views.age2, name='age'),
    path('patient_flow/<slug:start_date>/<slug:end_date>', views.patient_flow2, name='flow'),
]