from django.shortcuts import render
from django_treeform.models.TreeForm import Treeform
from django_jstree.models.nodeType import nodeType
import random
import json

def jsTreeBuildMenuDef(menuItem):
    menuItemDef = {
        "separator_before":menuItem.seperatorBefore,
        "separator_after":menuItem.seperatorAfter,
        "label":menuItem.menuLabel,
        "title":menuItem.menuTooltip,
        "action":menuItem.menuClickJSFunction,
        "icon":menuItem.menuItemClass,
        "shortcut":menuItem.shortcut,
        "shortcut_label":menuItem.shortcutLabel,
        "submenu":{}
    }
    
    if menuItem.childMenuItems.count() > 0:
        for curChild in menuItem.childMenuItems.all():
            print(curChild);
            menuItemDef["submenu"][curChild.name] = jsTreeBuildMenuDef(curChild)
        
    return menuItemDef

def showJSTreeByName(request, treename, rootnode = 0):
    try:
      jstobj = jstree.objects.get(name__exact=treename)
    except jstree.DoesNotExist:
      print("The requested {} tree does not exist", treename)

    _imp = __import__(jstobj.appname+'.models',globals(), locals(), jstobj.treemodelname)
    model = getattr(_imp, jstobj.treemodelname)
    
    typedef = {}
    popupMenuJSON = "{}"
    if jstobj.applyTypes == True:
        popupMenuDef = {}
        # Get the node types for this tree
        for curNodeType in jstobj.nodeTypes.all():
            # Build list of valid child nodes
            typedef[curNodeType.name] = { 
                "max_children":curNodeType.maxChildren,
                "max_depth":curNodeType.maxDepth,
                "valid_children":"",
                "icon":curNodeType.iconClass,
                "li_attr":curNodeType.liAttributes,
                "a_attr":curNodeType.aAttributes
            }
            for curChildType in curNodeType.childNodeTypes.all():
                typedef[curNodeType.name]["valid_children"] += curChildType.name + ","

            if len(typedef[curNodeType.name]["valid_children"]) > 0:
                typedef[curNodeType.name]["valid_children"] = typedef[curNodeType.name]["valid_children"][:-1]    
        
            popupMenuDef[curNodeType.name] = {}
            for curMenuItem in curNodeType.popupMenuItems.all().order_by('nodetypepopupmenuitem__displayOrder'):
                popupMenuDef[curNodeType.name][curMenuItem.name] = jsTreeBuildMenuDef(curMenuItem)
        
        popupMenuJSON = json.dumps(popupMenuDef)  
    
    context = { 'treename':treename,
                'appname':jstobj.appname,
                'treemodelname':jstobj.treemodelname,
                'leaffieldname':jstobj.leaffieldname,
                'startnode':rootnode,
                'menudef':popupMenuJSON,
                'typedef':typedef,
                'enableCheckbox':jstobj.enableCheckbox,
                'enableContextmenu':jstobj.enableContextmenu,
                'enableSearch':jstobj.enableSearch,
                'enableFuzzySearch':jstobj.enableFuzzySearch,
                'showOnlyMatches':jstobj.showOnlyMatches,
                'showOnlyMatchesChildren':jstobj.showOnlyMatchesChildren,
                'enableDND':jstobj.enableDND,
                'enableSort':jstobj.enableSort,
                'enableState':jstobj.enableState,
                'applyTypes':jstobj.applyTypes,
                'enableUnique':jstobj.enableUnique,
                'enableWholerow':jstobj.enableWholerow,
                'enableChanged':jstobj.enableChanged,
                'additionalJS':jstobj.additionalJS
              }
    return render(request, "jstree/jsTree.html", context)