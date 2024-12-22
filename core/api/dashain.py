from rest_framework.views import APIView
from rest_framework.response import Response

class dashainAPIView(APIView):
    def get(self, response, *args, **kwargs):
        response = ("dashain offer")
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        pass
