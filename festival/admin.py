from django.contrib import admin
from festival.models import *

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    pass
