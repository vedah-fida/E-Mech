from django.contrib import admin
from garages.models import RegisterGarage
# Register your models here.

class RegisterGarageAdmin(admin.ModelAdmin):
    list_display = ('garage_name', 'garage_location', 'garage_email', 'garage_telephone')
admin.site.register(RegisterGarage, RegisterGarageAdmin)

