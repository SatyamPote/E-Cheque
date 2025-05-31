from django.contrib import admin
from .models import Cheque, Block

@admin.register(Cheque)
class ChequeAdmin(admin.ModelAdmin):
    list_display = ['payee', 'amount', 'date', 'status']
    actions = ['approve_cheque', 'reject_cheque']

    def approve_cheque(self, request, queryset):
        queryset.update(status='approved')
        self.message_user(request, f"Successfully approved {queryset.count()} cheques.")

    def reject_cheque(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, f"Successfully rejected {queryset.count()} cheques.")

    approve_cheque.short_description = "Approve Selected Cheques"
    reject_cheque.short_description = "Reject Selected Cheques"

admin.site.register(Block)