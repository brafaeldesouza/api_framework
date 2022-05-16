import json
import requests
from django.db import IntegrityError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from api.models import Register



class GetListRegisterPIView(APIView):
    """This API view makes it possible to obtain details a graph

    Args:
        APIView (Class): Allows incoming requests to be dispatched to the appropriate method as well as implements various aspects of API policy

    """
    
    # determines the need to be authenticated to access the methods
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        result = dict()
        try:

            response = requests.get('https://jsonplaceholder.typicode.com/todos', headers = {} )
            
            data_list = json.loads(response.text)
            temp_list = []
            for data in data_list[:5]:
                temp_list.append({
                    "id": data['id'],
                    "title": data['title']
                })
            result['status_message'] = 'Registers returned successfully.'
            result['data'] = temp_list
            return Response(result, status=status.HTTP_200_OK)
        
        except IntegrityError as ie: 
            result['status_message'] = str(ie)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            result['status_message'] = str(e)
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
