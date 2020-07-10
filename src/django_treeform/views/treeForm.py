from django.shortcuts import render
import random

def showJSTree(request, appname, treemodelname, leaffieldname, rootnode = 0):
    _imp = __import__(appname+'.models',globals(), locals(), [treemodelname])
    model = getattr(_imp, treemodelname)
    treename = request.GET.get('treename', treemodelname+"_"+str(random.getrandbits(32)))
    return render(request, "jstree/jsTree.html", {'treename':treename, 'appname':appname, 'treemodelname':treemodelname, 'leaffieldname':leaffieldname, 'startnode':rootnode})