from django.shortcuts import render
from .models import Flows, Users
from rest_framework import viewsets
from .serializers import FlowSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
#from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    ##customize permissions
    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class FlowViewSet(viewsets.ModelViewSet):
    queryset = Flows.objects.all()
    serializer_class = FlowSerializer
    lookup_field = 'pk'
    TokenAuthentication.keyword = 'Bearer'
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)