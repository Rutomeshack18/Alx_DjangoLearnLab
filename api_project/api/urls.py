from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'Book', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token), 
]