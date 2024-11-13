from .views import CustomAuthToken
from django.urls import path, include

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view())
]



