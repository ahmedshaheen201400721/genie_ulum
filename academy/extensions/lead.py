
from modules.base.model_inheritance import ModelExtension
from django.db import models
from academy.models import Course
class LeadExtension(ModelExtension):
    _inherit = 'crm.lead'
    courses=models.ManyToManyField(Course,blank=True,related_name='leads')
    teacher=models.ForeignKey('base.partner', on_delete=models.CASCADE,blank=True,null=True,related_name='leads_teachers')
    started_on=models.DateField(blank=True,null=True)
    last_action=models.ForeignKey('academy.LastAction', on_delete=models.CASCADE,blank=True,null=True)