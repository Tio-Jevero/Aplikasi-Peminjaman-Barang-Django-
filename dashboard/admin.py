from django.contrib import admin
from . import models

class barangmodels(admin.ModelAdmin):
	readonly_fields = [
        'waktu_kembali'
	]

admin.site.register(models.barang);
