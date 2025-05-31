from django.db import models
import hashlib

class Cheque(models.Model):
    class Meta:
        app_label = 'cheques'  # Explicitly set the app label

    payee = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    signature = models.TextField()  # Store the digital signature
    approved = models.BooleanField(default=False)  # Add this line

    def __str__(self):
        return f"Cheque for {self.payee} - {self.amount}"

class Block(models.Model):
    class Meta:
        app_label = 'cheques'  # Explicitly set the app label

    cheque = models.OneToOneField(Cheque, on_delete=models.CASCADE)
    previous_hash = models.CharField(max_length=64, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        self.hash = self.calculate_hash()
        super().save(*args, **kwargs)

    def calculate_hash(self):
        data = str(self.cheque.id) + str(self.previous_hash) + str(self.timestamp)
        return hashlib.sha256(data.encode()).hexdigest()

    def __str__(self):
        return f"Block for Cheque {self.cheque.id} - Hash: {self.hash}"