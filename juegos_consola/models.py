from django.db import models
from core.models import Genre, Language, Extension, Developer, Produced

class Console(models.Model):
    GENERATION = [
        ('PRIMERA', '1ª Generación'),
        ('SEGUNDA', '2ª Generación'),
        ('TERCERA', '3ª Generación'),
        ('CUARTA', '4ª Generación'),
        ('QUINTA', '5ª Generación'),
        ('SEXTA', '6ª Generación'),
        ('SEPTIMA', '7ª Generación'),
    ]

    name = models.CharField(max_length = 100, verbose_name = "Sistema")
    console_image = models.ImageField(verbose_name = "Foto de Consola", upload_to = "videoconsolas/foto/", blank = True)
    console_banner = models.ImageField(verbose_name = "Banner", upload_to = "videoconsolas/banner/", blank = True)
    release = models.DateField(verbose_name="Fecha de Lanzamiento", blank = True)
    generation = models.CharField(max_length = 100, verbose_name = "Generación", choices = GENERATION)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Retrojuego(models.Model):
    # Region Select:
    REGION_ZONE = [
        ('PAL', 'PAL - Europa'),
        ('NTCSU', 'NTCS-U - America'),
        ('NTCSJ', 'NTCS-J - Japón')
    ]

    # Number of players:
    PLAYERS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ] 

    # Format System:
    SUPPORTS = [
        ('CAR', 'Cartucho'),
        ('CD', 'CD-ROM'),
        ('DVD', 'DVD'),
        ('GD', 'GD-ROM'),
        ('UMD', 'UMD'),
        ('TA', 'Tarjeta')
    ]

    DISCS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ]

    # Game System:
    console = models.ForeignKey(Console, verbose_name = 'Sistema', on_delete = models.CASCADE)

    # Game Identification:
    title = models.CharField(verbose_name = 'Título', max_length = 200, blank=True)
    original_title = models.CharField(verbose_name = 'Título Original', max_length = 200, blank=True)
    serial_number = models.CharField(verbose_name = 'Número de Serie', max_length = 30, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name = 'Género', blank=True)
    players = models.CharField(verbose_name = 'Jugadores', max_length = 10, choices = PLAYERS)
    developer = models.ForeignKey(Developer, on_delete = models.CASCADE, verbose_name = 'Desarrollador', blank=True)
    publisher = models.ForeignKey(Produced, on_delete = models.CASCADE, verbose_name = 'Productora', blank=True)
    date_released = models.DateField(verbose_name = 'Fecha de Publicación', blank=True)
    cover = models.ImageField(verbose_name = 'Carátula', upload_to = 'retrogames/covers', blank=True)
    logo = models.ImageField(verbose_name = 'Logotipo', upload_to = 'retrogames/logo', blank = True)

    # Game description:
    description = models.CharField(max_length = 500, verbose_name = "Descripción", blank=True)

    # Video Snap
    video = models.FileField(verbose_name = 'Video', upload_to = 'retrogames/videosnaps', blank = True)

    # Specifications:
    namefile = models.CharField(verbose_name = 'Nombre del archivo ejecutable', max_length = 150, blank=True)
    region = models.CharField(verbose_name = 'Región', max_length = 10, choices = REGION_ZONE, blank = True) 
    support = models.CharField(verbose_name = 'Soporte', max_length = 10, choices = SUPPORTS, blank=True)
    number_disk = models.CharField(verbose_name = 'Discos', max_length = 10, choices = DISCS, blank = True)
    languages = models.ManyToManyField(Language, verbose_name = 'Idiomas', blank=True)
    extension = models.ForeignKey(Extension, verbose_name = 'Formato de Archivo', on_delete = models.CASCADE, blank=True)

    # Screenshots
    screen_one = models.ImageField(verbose_name = 'Captura 1', upload_to = 'retrogames/screens', blank=True)
    screen_two = models.ImageField(verbose_name = 'Captura 2', upload_to = 'retrogames/screens', blank=True)
    screen_three = models.ImageField(verbose_name = 'Captura 3', upload_to = 'retrogames/screens', blank=True)
    screen_four = models.ImageField(verbose_name = 'Captura 4', upload_to = 'retrogames/screens', blank=True)

    # Download:
    as_downloaded = models.BooleanField(verbose_name = 'Subido', default = False)
    download_link = models.URLField(verbose_name = 'Link de Descarga', max_length = 200, blank = True)

    # Fecha de edición y creación:
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Videojuego de consola'
        verbose_name_plural = 'Videojuegos de consola'
        ordering = ['title']

    def __str__(self):
        return self.title