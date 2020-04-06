from aplication.models import *
from aplication.serializers import *
from rest_framework import generics

class AppGETView(generics.ListAPIView):
    
    serializer_class = AppSerializer
    queryset = App.objects.all()

class AppPOSTView(generics.CreateAPIView):

    serializer_class = AppSerializer
    queryset = App.objects.all()

class AppPUT_DELETEview(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = AppSerializer
    queryset = App.objects.values()


    def get_queryset(self):
        return App.objects.values()

    def get_object(self):
 
        queryset = App.objects
        return get_object_or_404(queryset, pk=self.kwargs['id'])
    
    def delete(self, request, *args, **kwargs):
        delete_project = self.destroy(request, *args, **kwargs)
        return Response(status=200,data={"content": f'O projeto  foi deletado' })
    
    def put(self, request, *args, **kwargs):
        put_project = self.update(request, *args, **kwargs)
        return put_project