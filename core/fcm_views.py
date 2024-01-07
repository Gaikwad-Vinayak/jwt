from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from pyfcm import FCMNotification
from fcm_django.models import FCMDevice
from core.fcm_serializers import FCMNotificationSerializer
# from fcm.fcm import FCMNotification
import firebase_admin

class FCMNotificationView(APIView):
    def get(self, request):
        return Response("hello")
    # def post(self, request):
    #     message = request.data.get('message')
    #     push_service = FCMNotification(api_key="AAAAMKhwzwM:APA91bHUh6T8mrg5tgO-zYKsKxLM5yvejxH8R6OA5sKHU_6C7heEdzlUXfkSMa5j96Y8XLrSDX-6UpH-IuNXs-oTRjU07bO1ig8UtH0bZvj1tKvfQoiYQxOFWBjVisAeILZiINsUWait")
    #     result = push_service.notify_topic_subscribers(
    #         topic_name="broadcast_topic",  # Replace with your topic name
    #         message_title="Your Title",
    #         message_body=message,
    #     )
    #     print(result,'/////////////////////////')
        
    #     return Response(result)
    def post(self, request):
        message = request.data.get('message')
        
        # Initialize the Firebase Admin SDK (make sure you have your service account key configured)
        try:
            firebase_admin.initialize_app()
        except ValueError:
            pass

        # Send the FCM notification
        push_service = FCMNotification(api_key="AAAAMKhwzwM:APA91bHUh6T8mrg5tgO-zYKsKxLM5yvejxH8R6OA5sKHU_6C7heEdzlUXfkSMa5j96Y8XLrSDX-6UpH-IuNXs-oTRjU07bO1ig8UtH0bZvj1tKvfQoiYQxOFWBjVisAeILZiINsUWait")
        result = push_service.notify_topic_subscribers(
            topic_name="broadcast_topic",
            message_title="Your Title",
            message_body=message,
        )
        
        return Response(result)
    # def post(self, request):
    #     serializer = FCMNotificationSerializer(data=request.data)

    #     if serializer.is_valid():
    #         # Get the device registration ID from the JSON data
    #         to = serializer.validated_data['to']

    #         # Get the notification data from the JSON data
    #         data = serializer.validated_data['data']

    #         # Send the FCM notification to the specified device
    #         try:
    #             device = FCMDevice.objects.get(registration_id=to)
    #             device.send_data(data)
    #             return Response({"message": "Notification sent successfully"})
    #         except FCMDevice.DoesNotExist:
    #             return Response({"error": "Device not found"}, status=404)

    #     return Response(serializer.errors, status=400)
    # def post(self, request):
    #     message = request.data.get('message')
        
    #     # Send the message to the "broadcast_topic"
    #     push_service = FCMNotification(api_key="AAAAMKhwzwM:APA91bHUh6T8mrg5tgO-zYKsKxLM5yvejxH8R6OA5sKHU_6C7heEdzlUXfkSMa5j96Y8XLrSDX-6UpH-IuNXs-oTRjU07bO1ig8UtH0bZvj1tKvfQoiYQxOFWBjVisAeILZiINsUWait")
        
    #     result = push_service.notify_topic_subscribers(
    #         topic_name="broadcast_topic",
    #         message_title="Your Title",
    #         message_body=message,
    #     )
        
    #     return Response(result)


    # def post(self, request):
    #     # Get the registration token(s) from the request data
    #     registration_tokens = request.data.get('registration_tokens', [])

    #     # Create an FCM client with your Firebase API Key
    #     push_service = FCMNotification(api_key="AAAAMKhwzwM:APA91bHUh6T8mrg5tgO-zYKsKxLM5yvejxH8R6OA5sKHU_6C7heEdzlUXfkSMa5j96Y8XLrSDX-6UpH-IuNXs-oTRjU07bO1ig8UtH0bZvj1tKvfQoiYQxOFWBjVisAeILZiINsUWait")

    #     # Send a notification to the devices
    #     message_title = request.data.get('title', 'Default Title')
    #     message_body = request.data.get('body', 'Default Body')
    #     result = push_service.notify_multiple_devices(
    #         registration_ids=registration_tokens,
    #         message_title=message_title,
    #         message_body=message_body,
    #     )

    #     return Response(result, status=status.HTTP_200_OK)


import random
import string

def generate_mock_device_token(length=152):
    # Generate a random string (token) of the specified length
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

mock_device_token = generate_mock_device_token()
print("Mock Device Token:", mock_device_token)
