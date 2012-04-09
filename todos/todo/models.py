#coding=utf-8
from django.db import models

class Todo(models.Model):
    content = models.CharField(max_length=128)
    done = models.CharField(max_length=1,default='N')    #Y表示完成N表示未完成
    order = models.IntegerField(blank=True)