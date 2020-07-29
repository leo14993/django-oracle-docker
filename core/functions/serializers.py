from rest_framework import serializers
from core.models.model_myproject import MyProject


class MyProject_Serializer(serializers.ModelSerializer):
    
     class Meta:
          model = MyProject
          fields = '__all__'


class ListaMyproject(serializers.ModelSerializer):
     cor = serializers.ReadOnlyField(source='Myproject.cor')
     valor = serializers.SerializerMethodField()
     class Meta:
          model = MyProject
          fields = ['cor','valor']
     
     def get_periodo(self, obj):
          return obj.get_periodo_display()
