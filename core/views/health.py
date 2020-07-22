from rest_framework import generics,status
from rest_framework.response import Response
from datetime import datetime



# @/health
class HealthView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            return Response(f" Status API: OK", status=status.HTTP_200_OK)
        except Exception as e :
            return Response("A API não está conectada! Erro : {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#@/status
class StatusView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            return Response(f"Status API: OK -- ", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"A API não está conectada! --  Tipo do erro: {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

