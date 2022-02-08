from django.contrib import admin

from .models import Excursion, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


admin.site.register(Image)