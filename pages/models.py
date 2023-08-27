from django.db import models


# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    designation = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    # sempre que cria uma def dentro de uma funcao
    # (self) deve ser colocado como parametro

    # Essa funcao normaliza o nome de "Teams" no painel de admin
    def __str__(self):
        return self.first_name
