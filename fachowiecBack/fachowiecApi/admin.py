from django.contrib import admin
from .models import Kategorie, Rating, Fachowiec, Ogloszenie, Miejscowosci
# Register your models here.

admin.site.register(Kategorie)
admin.site.register(Fachowiec)
admin.site.register(Ogloszenie)
admin.site.register(Miejscowosci)
admin.site.register(Rating)
