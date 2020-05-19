from django.db import models


class Model_Name(models.Model):
    model =models.CharField(max_length=256)
    def __str__(self):
            return self.model

class Sub_Assembly(models.Model):
    sub_assembly =models.CharField(max_length=256)
    def __str__(self):
        return self.sub_assembly
class Material(models.Model):
    material =models.CharField(max_length=256)
    def __str__(self):
        return self.material

class Item_Detail(models.Model):
    Model_Name = models.ForeignKey(Model_Name,on_delete=models.CASCADE,null=True)
    Sub_Assembly_Name = models.ForeignKey(Sub_Assembly,on_delete=models.CASCADE,null=True)
    Child_part = models.CharField(max_length=256,null=True)
    Size = models.CharField(max_length=256,null=True)
    Raw_Material = models.ForeignKey(Material,on_delete=models.CASCADE,null=True)
    Drawing1 = models.FileField(blank=True,null=True)
    Drawing2 = models.FileField(blank=True,null=True)
    Photo1 = models.ImageField(help_text='optional',upload_to='images/',blank=True,null=True)
    Photo2 = models.ImageField(help_text='optional',upload_to='images/',blank=True,null=True)
    Process_Instructions = models.TextField(help_text='optional',blank=True,null=True)
    #def __str__(self):
        #return self.Size
