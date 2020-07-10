from django.db import models
from treebeard.mp_tree import MP_Node

VALUE_TYPE_CHOICES = [
  ('', 'None'),
  ('AutoInt', 'Automaticly Assigned Integer'),
  ('AutoUUID', 'Automaticly Assigned UUID'),
  ('Boolean', 'Boolean'),
  ('Char', 'String'),
  ('Choice', 'List of Choices'),
  ('Credential', 'Credential'),
  ('Date', 'Date'),
  ('DateTime', 'Date and Time'),
  ('Email', 'Email'),
  ('File', 'File Upload Chooser'),
  ('Float', 'Float'),
  ('Image', 'Image Upload Chooser'),
  ('Integer', 'Integer'),
  ('GenericIPAddress', 'IP'),
  ('MultipleChoice', 'List of Choices with the ability to choose more than one'),
  ('MultipleInstance', 'List of Choices that you can have more than one of the same'),
  ('NullBoolean', 'True/False/None'),
  ('Regex', 'Regex'),
  ('Slug', 'Slug'),
  ('Time', 'Time'),
  ('URL', 'URL'),
  ('UserList', 'User List'),
  ('Password', 'Password'),
  ('YesNo', 'Yes/No')
]

class TreeFormItemAttribute(MP_Node):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(default='', blank=True)
    valueType = models.CharField(max_length=25, choices=VALUE_TYPE_CHOICES, blank=True, default='')
    valuePrompt = models.CharField(max_length=254, blank=True, default='')
    valueDefault = models.TextField(default='', blank=True)
    
    node_order_by = ['name']
    
    def __str__(self):
        return self.name