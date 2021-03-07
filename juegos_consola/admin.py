from django.contrib import admin
from .models import Retrojuego, Console

class RetrojuegoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'console', 'serial_number', 'region', 'genre_name')
    search_fields = ('title', 'console__name', 'serial_number', 'genre__name')
    list_filter = ('title', 'console__name', 'serial_number', 'genre__name')

    def genre_name(self, obj):
        return ", ".join([g.name for g in obj.genre.all().order_by('name')])
    genre_name.short_description = 'Género'

admin.site.register(Retrojuego, RetrojuegoAdmin)
admin.site.register(Console)