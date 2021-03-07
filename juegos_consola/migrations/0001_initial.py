# Generated by Django 3.1.7 on 2021-03-07 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Sistema')),
                ('console_image', models.ImageField(blank=True, upload_to='videoconsolas/foto/', verbose_name='Foto de Consola')),
                ('console_banner', models.ImageField(blank=True, upload_to='videoconsolas/banner/', verbose_name='Banner')),
                ('release', models.DateField(blank=True, verbose_name='Fecha de Lanzamiento')),
                ('generation', models.CharField(choices=[('PRIMERA', '1ª Generación'), ('SEGUNDA', '2ª Generación'), ('TERCERA', '3ª Generación'), ('CUARTA', '4ª Generación'), ('QUINTA', '5ª Generación'), ('SEXTA', '6ª Generación'), ('SEPTIMA', '7ª Generación')], max_length=100, verbose_name='Generación')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Retrojuego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Título')),
                ('original_title', models.CharField(blank=True, max_length=200, verbose_name='Título Original')),
                ('serial_number', models.CharField(blank=True, max_length=30, verbose_name='Número de Serie')),
                ('players', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, verbose_name='Jugadores')),
                ('date_released', models.DateField(blank=True, verbose_name='Fecha de Publicación')),
                ('cover', models.ImageField(blank=True, upload_to='retrogames/covers', verbose_name='Carátula')),
                ('logo', models.ImageField(blank=True, upload_to='retrogames/logo', verbose_name='Logotipo')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Descripción')),
                ('video', models.FileField(blank=True, upload_to='retrogames/videosnaps', verbose_name='Video')),
                ('namefile', models.CharField(blank=True, max_length=150, verbose_name='Nombre del archivo ejecutable')),
                ('region', models.CharField(blank=True, choices=[('PAL', 'PAL - Europa'), ('NTCSU', 'NTCS-U - America'), ('NTCSJ', 'NTCS-J - Japón')], max_length=10, verbose_name='Región')),
                ('support', models.CharField(blank=True, choices=[('CAR', 'Cartucho'), ('CD', 'CD-ROM'), ('DVD', 'DVD'), ('GD', 'GD-ROM'), ('UMD', 'UMD'), ('TA', 'Tarjeta')], max_length=10, verbose_name='Soporte')),
                ('number_disk', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, verbose_name='Discos')),
                ('screen_one', models.ImageField(blank=True, upload_to='retrogames/screens', verbose_name='Captura 1')),
                ('screen_two', models.ImageField(blank=True, upload_to='retrogames/screens', verbose_name='Captura 2')),
                ('screen_three', models.ImageField(blank=True, upload_to='retrogames/screens', verbose_name='Captura 3')),
                ('screen_four', models.ImageField(blank=True, upload_to='retrogames/screens', verbose_name='Captura 4')),
                ('as_downloaded', models.BooleanField(default=False, verbose_name='Subido')),
                ('download_link', models.URLField(blank=True, verbose_name='Link de Descarga')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos_consola.console', verbose_name='Sistema')),
                ('developer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.developer', verbose_name='Desarrollador')),
                ('extension', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.extension', verbose_name='Formato de Archivo')),
                ('genre', models.ManyToManyField(blank=True, to='core.Genre', verbose_name='Género')),
                ('languages', models.ManyToManyField(blank=True, to='core.Language', verbose_name='Idiomas')),
                ('publisher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.produced', verbose_name='Productora')),
            ],
            options={
                'verbose_name': 'Videojuego de consola',
                'verbose_name_plural': 'Videojuegos de consola',
                'ordering': ['title'],
            },
        ),
    ]