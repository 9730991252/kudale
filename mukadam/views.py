from django.shortcuts import render,redirect
from owner.models import *
# Create your views here.
def mukadam_dashboard(request):
    if request.session.has_key('mukadam_mobile'):
        mukadam_mobile = request.session['mukadam_mobile']
        m = Mukadam.objects.filter(mobile=mukadam_mobile).first()
        if m:
            m = Mukadam.objects.get(mobile=mukadam_mobile)

        context={
            'm':m
        }
        return render(request, 'mukadam/mukadam_dashboard.html',context)
    else:
        return redirect('/login/')