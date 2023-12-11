from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome
