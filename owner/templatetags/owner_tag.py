from django import template
from owner.models import *
from django.db.models import Avg, Sum, Min, Max
from math import *
from datetime import date
register = template.Library()

@register.simple_tag
def todays_taneg():
    t = Taneg.objects.filter(date__gte=date.today(),date__lte=date.today()).aggregate(Sum('taneg'))
    todays_taneg = t['taneg__sum']
    return todays_taneg

@register.simple_tag
def total_taneg():
    t = Taneg.objects.filter().aggregate(Sum('taneg'))
    total_taneg = t['taneg__sum']
    return total_taneg

@register.simple_tag
def mukadam_taneg(id):
    t = Taneg.objects.filter(mukadam_id=id).aggregate(Sum('taneg'))
    todays_taneg = t['taneg__sum']
    return todays_taneg

@register.simple_tag
def vehicle_taneg(id):
    t = Taneg.objects.filter(vehicle_id=id).aggregate(Sum('taneg'))
    todays_taneg = t['taneg__sum']
    return todays_taneg

@register.simple_tag
def karkhana_taneg(id):
    t = Taneg.objects.filter(karkhana_id=id).aggregate(Sum('taneg'))
    todays_taneg = t['taneg__sum']
    return todays_taneg