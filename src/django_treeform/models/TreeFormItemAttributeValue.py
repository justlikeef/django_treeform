from django.db import models

class TreeFormItemAttributeValue(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.TextField(default='')
    treeFormItem = models.ForeignKey("TreeFormItem", on_delete=models.CASCADE)
    treeFormItemAttributeType = models.ForeignKey("TreeFormItemAttribute", on_delete=models.PROTECT)

    def __str__(self):
        return "".join(self.treeFormItem.name, '-', self.treeFormItemAttributeType.name, ':', self.value)