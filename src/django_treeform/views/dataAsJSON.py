from django.core import serializers
from django.http import HttpResponse
from django_jstree.core.serializers.jsTreeNode import JSTreeNodeSerializer
import logging
        
def getDataAsJSON(request, appname, treemodelname, leaffieldname=None, nodeid=0):
    logger = logging.getLogger('django.server')
    _imp = __import__(appname+'.models',globals(), locals(), [treemodelname])
    applytypesparm = True if request.GET.get("applyTypes", False) == "True" else False
    treemodel = getattr(_imp, treemodelname)
    myserializer = JSTreeNodeSerializer()
    if nodeid == 0:
        return HttpResponse(content=myserializer.serialize(treemodel.get_root_nodes(), max_depth=2, leaffieldname=leaffieldname, applytypes=applytypesparm), content_type="application/json")      
    else:
        return HttpResponse(content=myserializer.serialize(treemodel.objects.filter(id=nodeid), max_depth=2, leaffieldname=leaffieldname, applytypes=applytypesparm), content_type="application/json")