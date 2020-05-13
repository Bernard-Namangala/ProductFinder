from django.contrib import admin
from .models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """
    store admin
    """
    prepopulated_fields = {'slug':('name',)}