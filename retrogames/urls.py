from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from retroapi.views import register_user, login_user


router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]