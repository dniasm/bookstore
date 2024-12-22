from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Genre
from core.api.serializes import GenreSerializer

class BookListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        genre = Genre.objects.all().values("name")
        serializer = GenreSerializer(genre, many=True)

        # response = ({"name": "Think and grow rich", "author": "Napoleon"})

        response = {"genres": serializer.data}
        return Response(response)
    
        # print(type genre)
    
    def post(self, request, *args, **kwargs):

        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # search = request.query_params.get("search")
        # genre = Genre.objects.filter(name__icontains=search)
        # serializer = GenreSerializer(genre, many=True)

        # print(request.query_params)
        # print(request.data)
        # return Response({"response": "request recieved"})

        return Response(serializer.data)
    
