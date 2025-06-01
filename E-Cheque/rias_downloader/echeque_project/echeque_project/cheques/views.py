from django.shortcuts import render, redirect
from .models import Cheque, Block
from .utils import sign_cheque, verify_cheque
from django.http import HttpResponse
from django.contrib import messages
import datetime
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import qrcode
from io import BytesIO
import base64

def home(request):
    return render(request, 'cheques/home.html')

def create_cheque(request):
    print("create_cheque view called!")
    if request.method == 'POST':
        print("Form data received:", request.POST)
        payee = request.POST['payee']
        amount = request.POST['amount']
        date_str = request.POST['date']
        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date format. Use YYYY-MM-DD.")
            return render(request, 'cheques/create_cheque.html')

        # Calculate Initial Hash
        data = f"{payee}{amount}{date_str}"
        initial_hash = hashlib.sha256(data.encode()).hexdigest()

        signature = sign_cheque(payee, amount, date_str)
        cheque = Cheque.objects.create(payee=payee, amount=amount, date=date, signature=signature)

        try:
            block = Block.objects.create(cheque=cheque, previous_hash=Block.objects.all().last().hash if Block.objects.exists() else None)
            print("Block created successfully!")  # Add this line
        except Exception as e:
            messages.error(request, f"Error creating block: {e}")
            print(f"Error creating block: {e}")  # Add this line
            return render(request, 'cheques/create_cheque.html')

        messages.success(request, "Cheque created successfully!")
        return redirect('bank1_approve', cheque_id=cheque.id)  # Redirect to bank1_approve
    else:
        print("GET request received")
        return render(request, 'cheques/create_cheque.html')

def blockchain(request):
    blocks = Block.objects.all().order_by('-timestamp')
    for block in blocks:
        cheque = block.cheque
        # Create QR code data
        data = f"Payee: {cheque.payee}\nAmount: {cheque.amount}\nDate: {cheque.date}\nStatus: {cheque.status}\nHash: {block.hash}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Convert QR code to base64 for embedding in HTML
        img = qr.make_image(fill_color="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        qr_code_base64 = base64.b64encode(buffered.getvalue()).decode()

        # Attach QR code to the block object for rendering in the template
        block.qr_code = qr_code_base64

    return render(request, 'cheques/blockchain.html', {'blocks': blocks})

def verify_cheque(request):
    cheques = Cheque.objects.all()
    return render(request, 'cheques/verify_cheque.html', {'cheques': cheques})

def bank1_approve(request, cheque_id):
    cheque = Cheque.objects.get(pk=cheque_id)
    return render(request, 'cheques/bank1_approve.html', {'cheque': cheque})

def cheque_management(request):
    cheques = Cheque.objects.all()
    if request.method == 'POST':
        cheque_id = request.POST.get('cheque_id')
        action = request.POST.get('action')

        if cheque_id and action:
            cheque = Cheque.objects.get(pk=cheque_id)
            if action == 'approve':
                cheque.status = 'approved'
            elif action == 'reject':
                cheque.status = 'rejected'
            cheque.save()
        return redirect('cheque_management')  # Redirect to the same page after action

    return render(request, 'cheques/cheque_management.html', {'cheques': cheques})