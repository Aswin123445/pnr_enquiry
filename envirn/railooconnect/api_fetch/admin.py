from django.contrib import admin
from .models import PNR
# Register your models here.
@admin.register(PNR)
class PNRAdmin(admin.ModelAdmin):
    list_display = ('pnr', 'train_number', 'source_station', 'destination_station', 'distance', 'user')
    search_fields = ('pnr', 'train_number', 'source_station', 'destination_station')
