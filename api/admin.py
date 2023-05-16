from django.contrib import admin
from .models import ContactForm,JoinUsForm, Building,BuildingImage
from django.utils.html import format_html
# Register your models here.




class ContactFormAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactForm
        fields = "__all__"


class BuildingImageInline(admin.TabularInline):
    model = BuildingImage
    extra = 0
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        return format_html('<img src="{url}" width="200" height="200" />'.format(url=obj.image.url))
    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_type','building_category','state')
    list_editable = ('state',)
    list_filter = ('building_type','building_category','state')
    ordering = ('state',)
    class Meta:
        model = Building
        fields = "__all__"
        verbose_name = "العقار"

    inlines = [BuildingImageInline,]
class BuildingImageAdmin(admin.ModelAdmin):
    class Meta:
        model = BuildingImage
        fields = "__all__"
        verbose_name = "صور العقار"


admin.site.register(ContactForm)
admin.site.register(JoinUsForm)
admin.site.register(Building,BuildingAdmin)
admin.site.register(BuildingImage)