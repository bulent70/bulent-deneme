from django.contrib import admin
from .models import Iletisim

class IletisimAdmin(admin.ModelAdmin):
    list_display = ('id', 'isim', 'ilan', 'email', 'iletisim_tarihi')
    list_display_links =('id', 'isim')
    search_fields = ('isim', 'email', 'ilan')
    list_per_page = 25


admin.site.register(Iletisim, IletisimAdmin)