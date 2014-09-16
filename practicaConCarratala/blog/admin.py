from django.contrib import admin

# Register your models here.

from django.contrib import admin
from blog.models import Entrada, Comentario

admin.site.register(Entrada)
admin.site.register(Comentario)