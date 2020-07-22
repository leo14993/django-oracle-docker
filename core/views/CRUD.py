from core.models.model_myproject import MyProject
from core.functions.serializers import MyProject_Serializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView, ListCreateAPIView
                                    , RetrieveUpdateDestroyAPIView, CreateAPIView)



#/project/create
class CreateMyProjectView(CreateAPIView):

    queryset = MyProject.objects.values()
    serializer_class = MyProject_Serializer
   

#project
class MyProjectView(ListAPIView):
    
    queryset = MyProject.objects.values()
    serializer_class = MyProject_Serializer
    def get(self,request,*args,**kwargs):
        return Response(MyProject.objects.values())

#project/update
class MyProject_Modifyview(RetrieveUpdateDestroyAPIView):

    queryset = MyProject.objects.values()
    serializer_class = MyProject_Serializer

    def get_queryset(self):
            return MyProject.objects.values()

    def get_object(self):
        queryset = MyProject.objects
        return get_object_or_404(queryset, pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(status=200,data={"content": f'O projeto  foi deletado' })
    
    def put(self, request, *args, **kwargs):
        put_project = self.update(request, *args, **kwargs)
        return put_project     