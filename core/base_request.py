import json
from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer
from core.models import AppUser
from django.contrib.auth.models import AnonymousUser, Group
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework.renderers import BaseRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class SuccessAPIRenderer(BaseRenderer):
    media_type = 'application/json'
    format = 'json'

    def render(self, data: dict, accepted_media_type=None, renderer_context: dict = None):
        if data is not None:
            if data.__contains__('error'):
                return json.dumps(data)
            elif data.__contains__('data'):
                return json.dumps(data)
            else:
                return json.dumps({"data": data})
        return b''

class BaseViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    renderer_classes = (SuccessAPIRenderer, BrowsableAPIRenderer)
    permission_classes = ()

    def get_user(self) -> AppUser:
        user = self.request.user
        if isinstance(user, AnonymousUser):
            raise AuthenticationFailed("User is not valid.")
        return user


class OpenBaseViewSet(BaseViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = ()


class StandardPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        next_page = None
        if self.page.has_next():
            next_page = self.page.next_page_number()

        previous_page = None
        if self.page.has_previous():
            previous_page = self.page.previous_page_number()

        return Response({
            'page': self.request.query_params.get('page', 1),
            'next_page': next_page,
            'next_page_link': self.get_next_link(),
            'previous_page': previous_page,
            'previous_page_link': self.get_previous_link(),
            'count': len(data),
            'max_pages': self.page.paginator.num_pages,
            'total_count': self.page.paginator.count,
            'data': data
        })
    
class AuthenticatedViewSet(BaseViewSet):
    permission_classes = (IsAuthenticated,)

class StandardResultSetPagination(StandardPageNumberPagination):
    page_size = 10  # The default page size
    page_size_query_param = 'page_size'  # Custom page size
    max_page_size = 100


class PaginatedViewSet(BaseViewSet):
    pagination_class = StandardResultSetPagination

class AllowAnyReadOnlyBaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = None
    serializer_class = None
    renderer_classes = (SuccessAPIRenderer, BrowsableAPIRenderer)
    permission_classes = (AllowAny,)
    http_method_names = ['get']


class ReadOnlyBaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = None
    serializer_class = None
    renderer_classes = (SuccessAPIRenderer, BrowsableAPIRenderer)
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']

    def get_user(self) -> AppUser:
        user = self.request.user
        if isinstance(user, AnonymousUser):
            raise AuthenticationFailed("User is not valid.")
        return user