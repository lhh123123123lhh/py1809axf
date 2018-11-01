from django.contrib import admin

# Register your models here.
from app.models import Wheel, Nav

admin.site.register(Nav)

admin.site.register(Wheel)
