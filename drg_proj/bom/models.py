from django.db import models


class Model_Name(models.Model):
    model =models.CharField(max_length=256)
    def __str__(self):
            return self.model

class Sub_Assembly(models.Model):
    sub_assembly =models.CharField(max_length=256)
    def __str__(self):
        return self.sub_assembly

class Item_Detail(models.Model):
    Model_Name = models.ForeignKey(Model_Name,on_delete=models.CASCADE)
    Sub_Assembly_Name = models.ForeignKey(Sub_Assembly,on_delete=models.CASCADE)
    Size =models.CharField(max_length=256)
    Drawing=models.FileField()
    #def __str__(self):
        #return self.Size
