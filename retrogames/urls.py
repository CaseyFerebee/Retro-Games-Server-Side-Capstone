from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from retroapi.views import register_user, login_user, GameView, OwnerView, ConsoleView, GenreView, ControllerView, ConsoleCollectionView, ControllerCollectionView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'owners', OwnerView, 'owner')
router.register(r'consoles', ConsoleView, 'console')
router.register(r'genres', GenreView, 'genre')
router.register(r'controllers', ControllerView, 'controller')
router.register(r'consolecollections', ConsoleCollectionView, 'consolecollection')
router.register(r'controllercollections', ControllerCollectionView, 'controllercollection')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]