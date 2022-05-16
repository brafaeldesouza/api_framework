import json
import requests
from django.db import IntegrityError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User


from api.models import Log, Register



class GetListRegisterAPIView(APIView):
    """This API view makes it possible to obtain details a graph

    Args:
        APIView (Class): Allows incoming requests to be dispatched to the appropriate method as well as implements various aspects of API policy

    """
    
    # determines the need to be authenticated to access the methods
    permission_classes = (IsAuthenticated,)
    status_message = 'Registers returned successfully.'
    
    def get(self, request):
        result = dict()
        result['data'] = {}
        try:

            response = requests.get('https://jsonplaceholder.typicode.com/todos', headers = {} )
            
            data_list = json.loads(response.text)
            temp_list = []
            for data in data_list[:5]:
                temp_list.append({
                    "id": data['id'],
                    "title": data['title']
                })
               
            result['status_message'] = self.status_message
            result['data'] = temp_list
            status_code = status.HTTP_200_OK
        
        except IntegrityError as ie: 
            result['error'] = {
                "reson" : str(ie) 
            }
            self.status_message = str(ie)
            status_code = status.HTTP_400_BAD_REQUEST

        except Exception as e:
            result['error']  = {
                "reason": str(e)
            } 
            self.status_message = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        Log.objects.create(
            data           = result['data'],
            user           = request.user,
            status_message = self.status_message,
            status_code    = status_code
        )
        return Response(result, status=status_code)

