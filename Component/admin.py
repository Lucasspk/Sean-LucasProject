from django.contrib import admin
from .models import Component, GPU, CPU, PSU, Motherboard

# Register your models here.
admin.site.register(Component)
admin.site.register(GPU)
admin.site.register(CPU)
admin.site.register(PSU)
admin.site.register(Motherboard)