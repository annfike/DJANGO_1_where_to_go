from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Excursion, Image
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]
    def preview(self, obj):
        return format_html('<img src= {} height=100 />', mark_safe(obj.photo.url))


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = (ImageInline,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('excursion', 'photo', 'preview', 'number')
    readonly_fields = ["preview"]
    raw_id_fields = ("excursion",)
    def preview(self, obj):
        return format_html('<img src= {} height=200 />', mark_safe(obj.photo.url))
        