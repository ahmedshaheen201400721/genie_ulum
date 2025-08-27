from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
# Models for academy module
from modules.base.models import BaseModel,Partner
class Course(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True,blank=True)
    instructor = models.ForeignKey(Partner, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
