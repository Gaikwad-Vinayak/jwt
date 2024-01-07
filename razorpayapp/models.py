from django.db import models
from core.models import UserMixin
from .base_models import Payment

# Create your models here.
class Book(UserMixin):
    class PaymentMethod(models.IntegerChoices):
        card = 1, 'card'
        upi = 2, 'upi'
        netbanking = 3, 'netbanking'
        wallet = 4, 'wallet'
        cash = 5, 'Cash'

    class PaymentStatus(models.IntegerChoices):
        in_progress = 1, 'in_progress'
        paid = 2, 'paid'
        unpaid = 3, 'unpaid'
        failed = 4, 'failed'
        refund = 5, 'refund'
        non_refundable = 6, 'non_refundable'

    payment_detail = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    payment_method = models.PositiveSmallIntegerField(default=1, choices=PaymentMethod.choices)
    payment_status = models.PositiveSmallIntegerField(default=4, choices=PaymentStatus.choices)