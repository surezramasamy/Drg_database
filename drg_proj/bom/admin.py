from django.contrib import admin
from . models import Model_Name,Sub_Assembly,Item_Detail
from import_export import fields,resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin


class BookResource(resources.ModelResource):
    Model_Name = fields.Field(attribute = 'Model_Name',)
    Sub_Assembly_Name = fields.Field(attribute = 'Sub_Assembly_Name',)

    class Meta:
        model = Item_Detail
    export_order = ('Model_Name','Sub_Assembly_Name','Size','Drawing')


class BookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = BookResource
    class Meta:
        model = Item_Detail
    list_display = ['Model_Name','Sub_Assembly_Name','Size','Drawing']
    search_fields = ['Model_Name','Sub_Assembly_Name']
    list_filter = ['Model_Name','Sub_Assembly_Name']



admin.site.register(Item_Detail,BookAdmin)
admin.site.register(Model_Name)
admin.site.register(Sub_Assembly)
