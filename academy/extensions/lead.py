
from modules.base.model_inheritance import ModelExtension
from django.db import models
from academy.models import Course
class PartnerExtension(ModelExtension):
    _inherit = 'crm.lead'
    courses=models.ManyToManyField(Course,blank=True,related_name='leads')
