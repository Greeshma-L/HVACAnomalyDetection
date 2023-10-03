from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_form, name='input_form'),
    path('predict_anomaly/', views.predict_anomaly, name='predict_anomaly'),
    path('input_form/', views.input_form, name='input_form'),
]
