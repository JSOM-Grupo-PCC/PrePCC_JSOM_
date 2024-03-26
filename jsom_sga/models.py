from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    peso = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Treino(models.Model):
    nome = models.CharField(max_length=90)

    CATEGORIA_CHOICES = [
        ('Treino(A)', 'Treino-A'),
        ('Treino(B)', 'Treino-B'),
        ('Treino(C)', 'Treino-C'),
        ('Treino(D)', 'Treino-D'),
        ('Treino(E)', 'Treino-E'),
    ]

    categoria = models.CharField(max_length=9, choices=CATEGORIA_CHOICES)
    imagem = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    descricao = models.TextField(blank=True)
    status = models.BooleanField(default=False)  # Adicionando o campo status
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.nome} {self.descricao}'
    