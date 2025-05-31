from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the home URL
    path('create_cheque/', views.create_cheque, name='create_cheque'),
    path('blockchain/', views.blockchain, name='blockchain'),
    path('verify_cheque_form/', views.verify_cheque_form, name='verify_cheque_form'),
    path('verify_cheque_result/', views.verify_cheque_result, name='verify_cheque_result'),
    path('bank1_approve/<int:cheque_id>/', views.bank1_approve, name='bank1_approve'), # Added URL pattern
    path('bank2_approve/<int:cheque_id>/', views.bank2_approve, name='bank2_approve'), # Added URL pattern
]