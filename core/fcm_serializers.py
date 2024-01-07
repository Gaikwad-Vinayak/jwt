from rest_framework import serializers
from fcm_django.models import FCMDevice


class FCMSerializers(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = '__all__'



class FCMNotificationSerializer(serializers.Serializer):
    to = serializers.CharField()
    data = serializers.DictField()