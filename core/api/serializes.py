from rest_framework import serializers
# from core.models import Product, Author, ProductCart, Genre
from core.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name", "description"]