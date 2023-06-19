from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/login/', TokenObtainPairView.as_view()),
]   