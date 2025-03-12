from rest_framework import viewsets, status
from ..models import *
from ..serializers import *
from django.contrib.auth import authenticate, login
from rest_framework.response import Response


from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
class Login(APIView):
    def post(self,request):
        nome = request.data.get("nome")
        senha = request.data.get("senha")
        usuario = authenticate(username=nome, password=senha)
        
        if (usuario):
            login(request, usuario)
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"mensagem": "Usuário não encontrado", "status": status.HTTP_401_UNAUTHORIZED})