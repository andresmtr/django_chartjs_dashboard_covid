from django.db import models

# Create your models here.

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False ,auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de eliminación', auto_now=True, auto_now_add=False)

    class  Meta:
        abstract = True

class Autor(ModeloBase):
    nombre = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=120)
    email = models.EmailField('Correo electronico', max_length=200, unique = True) 
    descripcion = models.TextField('Descripción')
    imagen_referencial = models.ImageField('Imagen referencial', null=True, blank=True, upload_to= 'autores/')
    web = models.URLField('Web', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    github = models.URLField('Github', null=True, blank=True)
    linkedin = models.URLField('Linkedin', null=True, blank=True)

    class  Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0} {1}'.format(self.nombre,self.apellidos)

class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')
    github = models.URLField('Github')
    linkedin = models.URLField('Linkedin')
    web = models.URLField('Web', null=True)

    class  Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook