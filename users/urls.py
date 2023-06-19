from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import *

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/login/', TokenObtainPairView.as_view()),
    path('users/<int:user_id>/', UserDetailView.as_view()),
]   