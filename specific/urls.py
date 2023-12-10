from specific.views import *
from django.urls import path
app_name='specific'

urlpatterns=[
    path('pyscho/',pyscho,name='pyscho'),
    path('regaltos/',regaltos,name='regaltos'),
]