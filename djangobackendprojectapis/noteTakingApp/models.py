from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):

    STATUS_CHOICES = (
        ("Active", 'active'),
        ("In-Active", 'inactive'),
        )
    
    id           = models.AutoField(primary_key=True,db_index=True)                                                 #db_index=True creates index on the field  
    status       = models.CharField(choices=STATUS_CHOICES,default="Active",max_length=100)
    created_at   = models.DateTimeField(auto_now_add=True)                                                          # auto_now_add saves current time only at the time of record creation
    updated_at   = models.DateTimeField(auto_now=True)                                                              # auto_now saves current time whenever record is saved

    class Meta:
        abstract = True

class Note(BaseModel):

    title = models.CharField(verbose_name="Title", max_length=100)
    description = models.CharField(verbose_name="Description", max_length=500)
    html_text = models.CharField(verbose_name="Raw HTML", max_length=500,null=True)
    user =  models.IntegerField(null=False,blank=False,db_index=True)

    class Meta:
        unique_together = [["title","user"]]                                                                        #make two field unique together
        