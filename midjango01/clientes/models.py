from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(verbose_name='nombre')
    edad = models.IntegerField(null=True, verbose_name="edad")
    genero = models.CharField(max_length=10, verbose_name="genero")
    foto = models.ImageField(upload_to='img/', null=True, verbose_name='foto')

    def __str__(self):
        registro = "id:"+str(self.id)+" | nombre:"+ self.nombre+ " | genero:"+self.genero
        return registro