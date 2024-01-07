from .models import *
from jwt_project.custom_models import RazorPay
from .base_models import *
from rest_framework import serializers
from .base_serializers import *
from razorpay import Client
from django.db import transaction

# from purchase.custom_models import RazorPay
import razorpay
from jwt_project.settings import RAZORPAY_API, RAZORPAY_SECRET


client: Client = razorpay.Client(auth=(RAZORPAY_API, RAZORPAY_SECRET))


class BookSerializers(serializers.ModelSerializer):
    transaction_id = serializers.CharField(allow_blank=True, trim_whitespace=True, write_only=True, required=True)
    payment_detail = serializers.IntegerField(required=False, write_only=True)
    payment = PaymentSerializer(required=False, read_only=True, source='payment_detail')
    order_id = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = Book


    def payment_status(self, data, order):
        try:
            x = client.payment.capture(data['transaction_id'], order.amount)
        except:
            return 3
        if not x['error_code']:
            return 2
        return 3

    @transaction.atomic()
    def create(self, validated_data: dict):
        print("validated_data", validated_data)
        # if not validated_data['slot'].is_available:
        #     raise ValidationError({"message": 'Slot Not Available'})
        # pop transaction_id & order_id
        transaction_id = validated_data.pop('transaction_id')
        o = validated_data.pop("order_id")
        order = Order.objects.get(pk=int(o))
        print("O = ", o)
        # load razorpay data from API
        razor_pay = RazorPay(transaction_id=transaction_id, purchase_model=self.Meta.model, client=client, order=int(o))
        print("transaction_id=", transaction_id, "purchase_model=", self.Meta.model, "client=", client, "ORDER", o)
        # set payment status
        # validated_data['payment_status'] = razor_pay.get_payment_status()
        print(razor_pay.payment_status,'***********7')
        validated_data['payment_status'] = razor_pay.payment_status
        print(razor_pay.response_data,)

        # set payment method
        validated_data['payment_method'] = razor_pay.get_payment_method()

        # create payment in db and set it here to attach it to purchase model
        payment = self.nested_create(razor_pay.response_data, PaymentSerializer, transaction_id=transaction_id)

        # set order on payment
        payment.set_order(order)

        self.nested_create(razor_pay.response_data, ChargeSerializer, payment=payment)

        # if paid by card, get and save card details as well
        if validated_data.__contains__("card_id"):
            card_info = client.card.fetch(validated_data["card_id"])
            self.nested_create(card_info, CardInformationSerializer, payment=payment)

        validated_data['payment_detail'] = payment

        # finally create entry
        instance = super().create(validated_data)
        # slot = validated_data['slot']
        # slot.is_available = False
        # slot.save()

        return instance