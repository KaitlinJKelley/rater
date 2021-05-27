from raterapp.models.category import Category
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

class CategoryViewSet(ViewSet):
    def list(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True, context={'request': request})

        return Response(serializer.data)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
