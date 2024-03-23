from django.contrib import admin
from .models import ImageCheck, InfoModel
from django.utils.html import format_html
from web_system.settings import admin_title


class ImageAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'check_result', 'image_tag', 'check_time')

    def image_tag(self, obj):
        if obj.file_url:
            return format_html('<img src="{}" style="width:120px;height:70px;"/>'.format(obj.file_url))
        return ""

    image_tag.allow_tags = True
    image_tag.short_description = '照片'


class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'info')


admin.site.register(ImageCheck, ImageAdmin)
admin.site.register(InfoModel, InfoAdmin)
admin.site.site_header = admin_title
