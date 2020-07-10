from django.contrib import admin
from django.urls import path
from django_treeform.views import treeForm
from django_treeform.views import treeFormByName
from django_treeform.views import dataAsJSON
from django_treeform.views import formAsJSON


urlpatterns = [
    path('django_treeform/getdata/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>/<int:nodeid>', NodeAsJSONJSTree.showNodeAsJSONJSTree),
    path('django_treeform/getform/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>/<int:rootnode>', jsTree.showJSTree),
    path('django_treeform/showform/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>/<int:rootnode>', jsTree.showJSTree),
    path('django_treeform/showform/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>', jsTree.showJSTree),
    path('django_treeform/showform/<slug:treename>', jsTreeByName.showJSTreeByName),
    path('django_treeform/showform/<slug:treename>>/<int:rootnode>', jsTreeByName.showJSTreeByName),
]
