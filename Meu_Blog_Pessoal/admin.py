from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Eu)
class EuAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email')

@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('nivel_de_escolaridade', 'curso', 'instituição')
