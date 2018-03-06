from django.contrib import admin
from .models import Services
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name',)

admin.site.register(Services, ServicesAdmin)
