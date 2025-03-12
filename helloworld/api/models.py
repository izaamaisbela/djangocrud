from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_aluno = models.BooleanField(default=False)
    

# class Aluno(models.Model):
#     nome = models.CharField(max_length=255, null=False, blank=False)
#     email = models.EmailField()
    
#     def __str__(self):
#         return self.nome

# class Funcionario(models.Model):
#     nome = models.CharField(max_length=255, null=False, blank=False)
#     sobrenome = models.CharField(max_length=255, null=False, blank=False)
#     cpf = models.CharField(max_length=14, null=False, blank=False)
#     tempo_de_servico = models.IntegerField(default=0, null=False, blank=False)
#     remuneracao = models.DecimalField(max_digits = 8, decimal_places=2, null=False, blank=False)
    
    
#     def __str__ (self):
#         return f"{self.nome}{self.sobrenome}"
    
# #783049

# class Produto(models.Model):
#     nome = models.CharField(max_length=255, null=False, blank=False)
#     descricao = models.CharField(max_length=500, null=False, blank=False)
#     preco = models.DecimalField(max_digits= 8, decimal_places=2, null=False, blank=False)
#     quantidade = models.IntegerField(default=0, null=False, blank= False)
    
#     def __str__ (self):
#         return f"{self.nome}{self.descricao}"
    