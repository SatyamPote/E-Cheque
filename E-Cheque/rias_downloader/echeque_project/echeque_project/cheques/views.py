from django.shortcuts import render, redirect
from .models import Cheque, Block
from .utils import sign_cheque, verify_cheque
from django.http import HttpResponse
from django.contrib import messages
import datetime

def home(request):
    return render(request, 'cheques/home.html')

def create_cheque(request):
    print("create_cheque view called!")  # Add this line for debugging
    if request.method == 'POST':
        print("Form data received:", request.POST)  # Add this line for debugging
        payee = request.POST['payee']
        amount = request.POST['amount']
        date_str = request.POST['date']
        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date format. Use YYYY-MM-DD.")
            return render(request, 'cheques/create_cheque.html')

        signature = sign_cheque(payee, amount, date_str)
        cheque = Cheque.objects.create(payee=payee, amount=amount, date=date, signature=signature)

        try:
            block = Block.objects.create(cheque=cheque, previous_hash=Block.objects.all().last().hash if Block.objects.exists() else None)
        except Exception as e:
            messages.error(request, f"Error creating block: {e}")
            return render(request, 'cheques/create_cheque.html')

        messages.success(request, "Cheque created successfully!")
        return redirect('blockchain')
    else:
        print("GET request received") # Add this line for debugging
        return render(request, 'cheques/create_cheque.html')

def blockchain(request):
    blocks = Block.objects.all().order_by('-timestamp')
    return render(request, 'cheques/blockchain.html', {'blocks': blocks})

def verify_cheque_form(request):
    return render(request, 'cheques/verify_cheque.html')

def verify_cheque_result(request):
    if request.method == 'POST':
        payee = request.POST['payee']
        amount = request.POST['amount']
        date_str = request.POST['date']
        signature = request.POST['signature']

        is_valid = verify_cheque(payee, amount, date_str, signature)
        return render(request, 'cheques/verify_cheque_result.html', {'is_valid': is_valid})
    return HttpResponse("Invalid request.")