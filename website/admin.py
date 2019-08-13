from django.contrib import admin
from website.models import *

class SlikaVGalerijiInline(admin.TabularInline):
    model = SlikaVGaleriji
    extra = 3

class VideoVGalerijiInline(admin.TabularInline):
    model = VideoVGaleriji
    extra = 1

class PredmetAdmin(admin.ModelAdmin):
    inlines = [ SlikaVGalerijiInline, VideoVGalerijiInline,  ]

admin.site.register(Naslov)
admin.site.register(Zgodba)
admin.site.register(OdpiralniCas)
admin.site.register(Zbirka)
admin.site.register(Predmet, PredmetAdmin)