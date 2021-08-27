from django.contrib import admin
from .models import Receita

class ListenReceitas(admin.ModelAdmin):
        list_display = ('id', 'nome_receita', 'categoria', 'public')
        list_display_links = ('id', 'nome_receita')
        search_fields = ('nome_receita',)
        list_filter = ('categoria',)
        list_editable = ('public',)
        list_per_page = 20

admin.site.register(Receita, ListenReceitas)
