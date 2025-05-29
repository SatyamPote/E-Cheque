import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import datetime

def load_keys():
    project_dir = sys.path[0]  # Get the project directory
    key_dir = os.path.join(project_dir, 'keys')
    private_key_path = os.path.join(key_dir, 'private.pem')
    public_key_path = os.path.join(key_dir, 'public.pem')

    with open(private_key_path, 'rb') as f:
        private_key = RSA.import_key(f.read())
    with open(public_key_path, 'rb') as f:
        public_key = RSA.import_key(f.read())
    return private_key, public_key

def sign_cheque(payee, amount, date):
    private_key, _ = load_keys()
    message = f"{payee}{amount}{date}".encode('utf-8')
    hash_object = SHA256.new(message)
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(hash_object)
    return signature.hex()

def verify_cheque(payee, amount, date, signature):
    _, public_key = load_keys()
    message = f"{payee}{amount}{date}".encode('utf-8')
    hash_object = SHA256.new(message)
    verifier = pkcs1_15.new(public_key)
    try:
        verifier.verify(hash_object, bytes.fromhex(signature))
        return True
    except (ValueError, TypeError):
        return False