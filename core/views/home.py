from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from src.configs.myproject_configs import redirect


class HomeView(ListAPIView):
    
    
    def get(self, request, *args, **kwargs):
     
        urls = {"Projeto":"API Oracle Docker Redis"

        ,"Endpoints Basicos":"Apenas para conferir funcionamento da API"
        ,"health":f"{redirect.HEALTH} | Método GET | consulta o status do funcionamento da API"
        ,"Endpoints Gerenciais":"CRUD dos dados (Create,Read,Update,Delete)"
        ,"my_project":f"{redirect.MY_PROJECT} | Método GET | Consulta os dados disponiveis no banco da tabela my_project"
        ,"create_my_project":f"{redirect.CREATE_PROJECT} | Método POST | Cria dados no banco da tabela my_project"
        ,"update_my_project":f"{redirect.UPDATE_MY_PROJECT} | Método PUT/PATCH DELETE | Edita/Deleta dados disponiveis no banco da tabela my_project "
        
        }

        return Response(urls)


