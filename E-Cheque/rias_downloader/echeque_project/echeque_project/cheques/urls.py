from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_cheque/', views.create_cheque, name='create_cheque'),
    path('blockchain/', views.blockchain, name='blockchain'),
    path('verify_cheque_form/', views.verify_cheque_form, name='verify_cheque_form'),
    path('verify_cheque_result/', views.verify_cheque_result, name='verify_cheque_result'),
    path('create_cheque/', views.create_cheque, name='create_cheque'),
]