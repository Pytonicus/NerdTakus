from django.db import models

class Artist(models.Model):
    name = models.CharField(verbose_name = 'Artista', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name = 'Categoría', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(verbose_name = 'Género', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ['name']

    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(verbose_name = 'Estudio', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Estudio'
        verbose_name_plural = 'Estudios'
        ordering = ['name']

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(verbose_name = 'Desarrollador', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Desarrollador'
        verbose_name_plural = 'Desarrolladora'
        ordering = ['name']

    def __str__(self):
        return self.name
        
class Produced(models.Model):
    name = models.CharField(verbose_name = 'Productor', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Productor'
        verbose_name_plural = 'Productora'
        ordering = ['name']

    def __str__(self):
        return self.name

class Extension(models.Model):
    name = models.CharField(verbose_name = 'Formato', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Formato'
        verbose_name_plural = 'Formato de archivo'
        ordering = ['name']

    def __str__(self):
        return self.name

class Resolution(models.Model):
    name = models.CharField(verbose_name = 'Resolución', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Resolución'
        verbose_name_plural = 'Resolución del archivo'
        ordering = ['name']

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(verbose_name = 'Idioma', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(verbose_name = 'Pais', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['name']

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(verbose_name = 'Director', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'
        ordering = ['name']

    def __str__(self):
        return self.name

class Guion(models.Model):
    name = models.CharField(verbose_name = 'Guión', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Guión'
        verbose_name_plural = 'Guiónistas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Music(models.Model):
    name = models.CharField(verbose_name = 'Compositor / Banda', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Compositor / Banda'
        verbose_name_plural = 'Compositores / Bandas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(verbose_name = 'Reparto', max_length = 100)

    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de actualización', auto_now = True)

    class Meta:
        verbose_name = 'Reparto'
        verbose_name_plural = 'Actores'
        ordering = ['name']

    def __str__(self):
        return self.name