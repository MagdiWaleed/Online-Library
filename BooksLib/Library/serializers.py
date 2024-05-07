from rest_framework import serializers
from .models import SingleBookModel

class SingleBookModelSerializer(ModelSerializer):
    class Meta:
        model = SingleBookModel
        fields = '__all__'  # Include all fields (adjust as needed)
