from django.contrib import admin
from .models import Mechanics


# Register your models here.
class MechanicsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','username', 'email')

admin.site.register(Mechanics, MechanicsAdmin)
