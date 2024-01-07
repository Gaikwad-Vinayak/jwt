from django.db import models

CHAR_FIELD_MAX_LENGTH = 500


class DefaultMaxLengthCharField(models.CharField):
    # 100 characters default limit field
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = CHAR_FIELD_MAX_LENGTH
        super(DefaultMaxLengthCharField, self).__init__(*args, **kwargs)




class RazorPay:
    def __init__(self, transaction_id, purchase_model, client, order):
        self.transaction_id = transaction_id
        self.client = client
        self.purchase_model = purchase_model
        self.order: Order = order
        # self.response_data = self.get_razorpay_response(transaction_id, order)
        self.response_data = self.fetch_txn_details(transaction_id)
        self.payment_status = self.get_payment_status()

    def get_razorpay_response(self, transaction_id, order):
        # for testing purposes
        # return self.client.payment.fetch(transaction_id)
        return self.client.payment.capture(transaction_id, order.amount, {"currency": "INR"})

    def fetch_txn_details(self, transaction_id):
        return self.client.payment.fetch(transaction_id)

    def get_payment_status(self):
        if self.response_data['status'] == 'captured':
            return 2

        elif self.response_data['status'] == 'authorized':
            return 1

        elif self.response_data['status'] == 'failed':
            return 4

    def get_payment_method(self):
        method = self.response_data.get("method", None)
        return self.purchase_model.PaymentMethod.__getattr__(method).value
