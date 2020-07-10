from django.db import models

class treeForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(default='', blank=True)
    appname = models.CharField(max_length=255)
    parentmodelname = models.CharField(max_length=255)
    attributemodelname = models.CharField(max_length=255)
    attributevaluemodelname = models.CharField(max_length=255)
    additionalJS = models.TextField(default='', blank=True)
    
    def __str__(self):
        return self.name
