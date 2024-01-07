# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status

# from django.contrib.auth.models import AnonymousUser
# from django.test import TestCase, RequestFactory

# class ViewRequestFactoryTestMixin(object):
#     """Mixin with shortcuts for view tests."""
#     longMessage = True  # More verbose messages
#     view_class = None
#     def get_response(self, method):
#         factory = RequestFactory()
#         req = getattr(factory, method)('/')
#         req.user = AnonymousUser()
#         return self.view_class.as_view()(req, *[], **{})
#     def is_callable(self):
#         resp = self.get_response('get')
#         self.assertEqual(resp.status_code, 200)

# class SendNotificationTest(TestCase):

#     def test_send_notification_view(self):
#         url = reverse('send-notification')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200) 