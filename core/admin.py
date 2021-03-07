from django.contrib import admin
from .models import Artist, Category, Genre, Studio, Developer, Produced, Extension, Resolution, Language, Country, Director, Guion, Music, Staff

class OpcionesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    fields = [('name')]

admin.site.register(Artist, OpcionesAdmin)
admin.site.register(Category, OpcionesAdmin)
admin.site.register(Genre, OpcionesAdmin)
admin.site.register(Studio, OpcionesAdmin)
admin.site.register(Developer, OpcionesAdmin)
admin.site.register(Produced, OpcionesAdmin)
admin.site.register(Extension, OpcionesAdmin)
admin.site.register(Resolution, OpcionesAdmin)
admin.site.register(Language, OpcionesAdmin)
admin.site.register(Country, OpcionesAdmin)
admin.site.register(Director, OpcionesAdmin)
admin.site.register(Guion, OpcionesAdmin)
admin.site.register(Music, OpcionesAdmin)
admin.site.register(Staff, OpcionesAdmin)