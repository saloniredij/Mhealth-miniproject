from django.urls import path
from . import views


urlpatterns = [
     path('',views.index, name='index'),
     path('bmi/',views.bmi , name = 'bmi'),
     path('symptom/',views.symptom , name = 'symptom'),
]









