from django.db import models

class TreeFormItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name
