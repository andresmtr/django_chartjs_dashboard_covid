# Generated by Django 3.1.2 on 2021-08-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=120, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Correo electronico')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('imagen_referencial', models.ImageField(blank=True, null=True, upload_to='autores/', verbose_name='Imagen referencial')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('github', models.URLField(blank=True, null=True, verbose_name='Github')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('github', models.URLField(verbose_name='Github')),
                ('linkedin', models.URLField(verbose_name='Linkedin')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
            },
        ),
    ]
