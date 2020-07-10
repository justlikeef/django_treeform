from django.core.serializers.json import Serializer
from django.conf import settings

class JSTreeNodeSerializer(Serializer):
    def _init_options(self):
        self.max_depth = self.options.pop('max_depth', 0)
        self.leaffieldname = self.options.pop('leaffieldname', 0)
        self.applytypes = self.options.pop('applytypes', False)
        if self.leaffieldname.find(','):
          self.leaffieldname = self.leaffieldname.split(',')
        else:
          self.leaffieldname = [self.leaffieldname]
        super()._init_options()

    def get_dump_object(self, obj, curdepth = 0):
        data = {'id': str(obj.path)+'_'+str(obj.id), 'text':str(obj), 'children': [], 'icon':'jstree-root' if curdepth == 0 else 'jstree-branch'}
        if self.applytypes == True:
            if hasattr(obj, 'getTreeNodeType'):
                data["type"] = obj.getTreeNodeType()
            else:
                data["type"] = obj.__class__.__name__
        
        if curdepth <= self.max_depth:
            if obj.get_children_count() > 0:
                for child in obj.get_children():
                    data['children'].append(self.get_dump_object(child, curdepth+1))
            else:
                data['children'] = False
        else:
            data['children'] = True if obj.get_children_count() > 0 else False
               
        for curleaffield in self.leaffieldname:
          if (hasattr(obj, curleaffield)):
              if eval(''.join(['obj.', curleaffield, '.count()'])) > 0:
                  if isinstance(data['children'], bool):
                      data['children'] = []
                   
                  for curleafobj in eval(''.join(['obj.', curleaffield, '.all()'])):
                      childdata = {'id':''.join([str(obj.path),'_',str(obj.id),'_',curleaffield,"_",str(curleafobj.id)]), 'text':str(curleafobj), 'icon':"".join(['jstree-leaf jstree-',curleaffield,'-leaf']), 'children':False}
                      if self.applytypes == True:
                          if hasattr(curleafobj, 'getTreeNodeType'):
                              childdata["type"] = curleafobj.getTreeNodeType()
                          else:
                              childdata["type"] = curleafobj.__class__.__name__
                      
                      data['children'].append(childdata)
                  
        if data['children'] == False:
            data.pop('children')
        return data