
from modules.base.model_inheritance import ModelExtension
from django.db import models
class TeacherExtension(ModelExtension):
    _inherit = 'base.partner'
    teacher=models.BooleanField(default=False)
    address=models.CharField(max_length=255,blank=True,null=True)
    age_group=models.ForeignKey('academy.AgeGroup', on_delete=models.CASCADE,blank=True,null=True)


