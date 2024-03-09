# websites/admin.py

from django.contrib import admin
from .models import *


class IndexAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Index._meta.get_fields()]


admin.site.register(Index, IndexAdmin)
