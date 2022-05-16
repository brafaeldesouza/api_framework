from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 

from api.views.register import GetListRegisterAPIView
from api.views.user import CreateUserAPIView

app_name = 'api'

urlpatterns = [
    
    
    path('user/create/' , CreateUserAPIView.as_view(), name="create_user"),
    path('register/'    , GetListRegisterAPIView.as_view(), name="list_register"),
    path('obtain_token/' , obtain_auth_token, name='api_token_auth'),
   
]
