from rest_framework import serializers
from core.models.model_myproject import MyProject


class MyProject_Serializer(serializers.ModelSerializer):
    
     class Meta:
          model = MyProject
          fields = '__all__'

