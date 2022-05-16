from django.urls import path

from api.views.user import CreateUserAPIView

app_name = 'api'

urlpatterns = [
    
    
    path('user/create/' , CreateUserAPIView.as_view(), name="create_user"),

   
]
