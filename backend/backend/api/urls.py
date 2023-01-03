from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import UserViewSet, FlowViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register('flows', FlowViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    #path('myself/', ManageUserView.as_view(), name='myself'),
    path('login',obtain_auth_token,name='login'),
    path('', include(router.urls)),
]