from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views.api_views import *
from .views.web_views import *

# router = DefaultRouter()
# router.register('user', UserViewSet)
# #from .views import (listar_users, cadastrar_user, obter_user)

urlpatterns=[
    # path('api/', include(router.urls)),
    path('api/user', User.as_view(), name = 'usuarioApi'),
    path('api/user/<int:id>', User.as_view(), name = 'idUsuario'),
    path('api/login', Login.as_view(), name='loginAPI'),
    path('api/GetDadosUsuarioLogado', GetDadosUsuarioLogado.as_view(), name = 'GetDadosUsuarioLogado'),
    path('home/', home, name = "home"),
    # path('criarAluno/', CriarAluno, name= "CriarAluno"),
    path('login/', login, name='login'),
    path('criarUsuario/', criarUser, name='usuario'),
    path('criarUsuario/<int:id>', criarUser, name='usuarioEdicao'),
    #path('alunos/', listar_alunos, name='listar_alunos'),
    #path('alunos/cadastrar/', cadastrar_aluno, name='cadastrar_aluno'),
    #path('alunos/<int:id>/', obter_aluno, name='obter_aluno'),
    ]
