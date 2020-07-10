from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from depo.models.TreeForm import TreeForm
from depo.models.TreeFormItem import TreeFormItem
from depo.models.TreeFormItemAttribute import TreeFormItemAttribute
from depo.models.TreeFormItemAttributeValue import TreeFormItemAttributeValue

class TreeFormItemAdmin(TreeAdmin):
    form = movenodeform_factory(TreeFormItem)

class TreeFormItemAttributeAdmin(TreeAdmin):
    form = movenodeform_factory(TreeFormItemAttribute)

admin.site.register(TreeForm)
admin.site.register(TreeFormItem, TreeFormItemAdmin)
admin.site.register(TreeFormItemAttribute, TreeFormItemAttributeAdmin)
