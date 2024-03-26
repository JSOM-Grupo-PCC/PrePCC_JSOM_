from django.contrib import admin
from jsom_sga import models

@admin.register(models.Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'categoria', 'descricao', 'owner', 'status',
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'id', 'nome', 'categoria',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'nome', 'categoria', 'owner', 'status', 
    list_display_links = 'id',

@admin.register(models.UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = 'user_id', 'peso', 'altura', 'data_nascimento', 'id',