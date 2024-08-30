from django.db import models

# Create your models here.

class Sobre(models.Model):   
    nivel_de_escolaridade = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    instituição = models.CharField(max_length=100)
    preferencias = models.CharField(max_length=100)
    habilidades = models.CharField(max_length=100)
    experiência = models.TextField()  
    descricao = models.TextField()
    projetos = models.TextField()
    def __str__(self):
        return f"{self.nivel_de_escolaridade} - {self.curso} - {self.instituição}"

class Eu(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data_de_Nascimento = models.DateField()
    genero = models.CharField(max_length=100)
    estado_cívil = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    sobre = models.ForeignKey('Sobre', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.nome} - {self.idade} - {self.email}"
