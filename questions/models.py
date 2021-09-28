from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Question(models.Model):
    class Order(models.TextChoices):
        desc    = "desc", "Descending"
        asc     = "asc", "Ascending"
    class Sort(models.TextChoices):
        activity    = "activity", "Activity"
        creation    = "creation", "Creation"
        votes       = "votes", "Votes"
        relevance   = "relevance", "Relevance"

    q           = models.CharField(max_length=500)
    accepted    = models.BooleanField(null=True,blank=True)
    answers     = models.IntegerField(null=True,blank=True)
    body        = models.CharField(max_length=500,null=True,blank=True)
    closed      = models.BooleanField(null=True)
    migrated    = models.BooleanField(null=True)
    notice      = models.BooleanField(null=True)
    tagged      = models.CharField(max_length=500,null=True,blank=True)
    nottagged   = models.CharField(max_length=500,null=True,blank=True)
    title       = models.CharField(max_length=500,null=True,blank=True)
    user        = models.BigIntegerField(null=True,blank=True)
    title       = models.CharField(max_length=500,null=True,blank=True)
    url         = models.URLField(max_length=500,null=True,blank=True)
    views       = models.BigIntegerField(null=True,blank=True)
    wiki        = models.BooleanField(null=True)
    page        = models.IntegerField(default=1,validators=[MinValueValidator(1)])
    pagesize    = models.IntegerField(default=25,validators=[MinValueValidator(1)])
    fromdate    = models.DateField(null=True,blank=True)
    todate      = models.DateField(null=True,blank=True)
    order       = models.CharField(max_length = 300, choices=Order.choices, default=Order.desc)
    min         = models.DateField(null=True,blank=True)
    max         = models.DateField(null=True,blank=True)
    sort        = models.CharField(max_length = 300, choices=Sort.choices, default=Sort.activity)


class Search(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.JSONField()