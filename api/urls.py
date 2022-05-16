from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 

from api.views.user import CreateUserAPIView

app_name = 'api'

urlpatterns = [
    
    
    path('user/create/' , CreateUserAPIView.as_view(), name="create_user"),
    path('obtain_token/' , obtain_auth_token, name='api_token_auth'),
   
]
