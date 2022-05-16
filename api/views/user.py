from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError, transaction
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class CreateUserAPIView(APIView):
    """This API view makes it possible to create a new user

    Args:
        APIView (Class): Allows incoming requests to be dispatched to the appropriate method as well as implements various aspects of API policy

    """
   
    def post(self, request):
        result = dict()
        try:
            with transaction.atomic():

                body = request.data

                # create a new user
                user = User.objects.create_user(
                    username = body['username'], 
                    email    = body['email'], 
                    password = body['password'])

                # create a new token
                token = Token.objects.create(user=user)

                result['status_message'] = 'User created successfully'
                result['token']  = token.key
                result['user'] = {
                    'id'       : user.id,
                    'username' : user.username,
                    'email'    : user.email
                }

                return Response(result, status=status.HTTP_201_CREATED)

        except IntegrityError as ie: 
            result['status_message'] = str(ie)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            result['status_message'] = str(e)
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
