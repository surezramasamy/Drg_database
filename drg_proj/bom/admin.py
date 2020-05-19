from django.contrib import admin
from . models import Model_Name,Sub_Assembly,Item_Detail,Material
from import_export import fields,resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

class BookResource(resources.ModelResource):
    Model_Name = fields.Field(column_name='Model_Name',attribute = 'Model_Name',widget=ForeignKeyWidget(Model_Name, 'model'))
    Sub_Assembly_Name = fields.Field(column_name='Sub_Assembly_Name',attribute = 'Sub_Assembly_Name',widget=ForeignKeyWidget(Sub_Assembly, 'sub_assembly'))
    Raw_Material = fields.Field(column_name='Raw_Material',attribute = 'Raw_Material',widget=ForeignKeyWidget(Material, 'material'))

    class Meta:
        model = Item_Detail



class BookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = BookResource
    class Meta:
        model = Item_Detail
    list_display = ['Model_Name','Sub_Assembly_Name','Child_part','Size','Raw_Material','Drawing1','Drawing2','Photo1','Photo2','Process_Instructions']
    search_fields = ['Model_Name','Sub_Assembly_Name','Child_part']
    list_filter = ['Model_Name','Sub_Assembly_Name','Child_part']



admin.site.register(Item_Detail,BookAdmin)
admin.site.register(Model_Name)
admin.site.register(Sub_Assembly)
admin.site.register(Material)
