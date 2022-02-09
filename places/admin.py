from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Excursion, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 100px;">')


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = (ImageInline,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('excursion', 'photo', 'preview', 'number')
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 200px;">')
        