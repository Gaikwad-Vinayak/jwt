from django.shortcuts import render
from core.base_request import OpenBaseViewSet, AuthenticatedViewSet,PaginatedViewSet
from .models import *
from .serializers import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

# Create your views here.
class PurchaseTestViewSet(AuthenticatedViewSet, PaginatedViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    razorpay_client = razorpay.Client(auth=(RAZORPAY_API, RAZORPAY_SECRET))
    http_method_names = ['post', 'get','patch']

    @action(detail=False, methods=['POST'])
    def initiate_book_slot(self, request):
        serializer = OrderSerializer2(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def order_test_slot(self, request):
        param = request.data
        print("Param = ", param)
        param['user'] = self.request.user.pk
        print(param['user'])
    
        serializer = BookSerializers(data=request.data, context={"data": param})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)