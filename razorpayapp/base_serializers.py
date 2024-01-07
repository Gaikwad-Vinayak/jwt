from base_models import *
from rest_framework import serializers
from razorpay import Client
import razorpay
from jwt_project.settings import RAZORPAY_API, RAZORPAY_SECRET

client: Client = razorpay.Client(auth=(RAZORPAY_API, RAZORPAY_SECRET))


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInformation

class ChargeSerializer(serializers.ModelSerializer):
    payment = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Charge

    def validate(self, attrs):
        """
        Razorpay sends amount 500.00 as 50000, so divided by 100 in order to get the correct amount.
        """
        if attrs['tax'] and attrs['fee']:
            attrs['tax'] = attrs['tax'] / 100
            attrs['fee'] = attrs['fee'] / 100

        return attrs


class PaymentSerializer(serializers.ModelSerializer):
    card = CardSerializer(source='cardinformation', read_only=True)
    transaction_id = serializers.CharField(trim_whitespace=True, required=False)
    charge = ChargeSerializer(read_only=True)
    status = serializers.IntegerField(source='purchasedcourse.payment_status', read_only=True)

    class Meta:
        model = Payment

    @staticmethod
    def validate_amount(amount):
        """
        Razorpay sends amount 500.00 as 50000, so divided by 100 in order to get the correct amount.
        """
        return amount / 100
    

class CardInformationSerializer(serializers.ModelSerializer):
    payment = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CardInformation


class OrderSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Order

    def create(self, validated_data: dict):
        data = {'amount': str(validated_data['amount']), 'currency': "INR"}
        validated_data.update(self.create_order(data))

        return super().create(validated_data)

    @staticmethod
    def create_order(data):
        order = client.order.create(data, )
        return {"order_id": order.get("id")}
