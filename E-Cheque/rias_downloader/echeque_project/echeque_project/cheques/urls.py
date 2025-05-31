from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the home URL
    path('create_cheque/', views.create_cheque, name='create_cheque'),
    path('blockchain/', views.blockchain, name='blockchain'),
    path('verify_cheque/', views.verify_cheque, name='verify_cheque'),
    path('bank1_approve/<int:cheque_id>/', views.bank1_approve, name='bank1_approve'), # Added URL pattern
]