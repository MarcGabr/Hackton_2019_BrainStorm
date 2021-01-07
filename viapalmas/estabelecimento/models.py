from django.db import models
# Create your models here.
class Turista(models.Model):
    nome = models.CharField('Nome', max_length=255)
    telefone = models.CharField('Telefone', max_length=50)
    email = models.EmailField('Email', max_length=255)
    foto = models.ImageField('Foto', upload_to='turista/imagens/')
    curriculo = models.URLField('Curriculo', max_length=255, blank=True, null=True)
    twitter = models.URLField('Twitter', max_length=255, blank=True, null=True)
    facebook = models.URLField('Facebook', max_length=255, blank=True, null=True)
    instagram = models.URLField('Instagram', max_length=255, blank=True, null=True)
    skype = models.CharField('Skype', max_length=255, blank=True, null=True)


    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pesssoa'
        verbose_name_plural = 'Pesssoas'
        ordering = ['nome', 'criado_em', 'atualizado_em']
