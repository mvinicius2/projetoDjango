from django.db import models



class Usuario(models.Model):
    id_usuario = models.CharField(max_length=30)
    senha = models.CharField(blank=True, max_length=10)
    dataNascimento = models.DateField(blank=False)

    def __str__(self):
        return self.id_usuario




