from jwt_project.custom_models import CHAR_FIELD_MAX_LENGTH, DefaultMaxLengthCharField
from django.db import models



class Order(models.Model):
    order_id = DefaultMaxLengthCharField(null=True)
    amount = models.PositiveIntegerField(null=True)


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    transaction_id = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    invoice_id = DefaultMaxLengthCharField(null=True)
    vpa = DefaultMaxLengthCharField(null=True)
    bank = DefaultMaxLengthCharField(null=True)
    wallet = DefaultMaxLengthCharField(null=True)
    card_id = DefaultMaxLengthCharField(null=True)
    refund_id = DefaultMaxLengthCharField(null=True)

    def __str__(self):
        return f'{self.amount} | {self.transaction_id}'

    def set_order(self, order):
        self.order = order
        self.save()


class CardInformation(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT)
    name = DefaultMaxLengthCharField()
    last4 = models.CharField(max_length=4)
    network = models.CharField(max_length=25)
    type = models.CharField(max_length=10)
    issuer = models.CharField(max_length=10)
    international = models.BooleanField()
    emi = models.BooleanField()

class Charge(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, null=True)


