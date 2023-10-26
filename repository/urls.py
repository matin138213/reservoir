from rest_framework.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users'),
router.register('passwords', views.PasswordViewSet, basename='passwords'),

urlpatterns = router.urls
