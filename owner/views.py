from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db.models import Sum, Max
from datetime import date
# Create your views here.
def owner_dashbord(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        m = Taneg.objects.values('mukadam_id','mukadam__name').annotate(top = Sum('taneg')).order_by('-top')[0:5]
        todays_taneg = Taneg.objects.filter(date__gte=date.today(),date__lte=date.today())
        tm = todays_taneg.values('mukadam_id','mukadam__name').annotate(top = Sum('taneg')).order_by('-top')[0:5]
        context={
            'total_mukadam':Mukadam.objects.all().count(),
            'total_karkhana':Karkhana.objects.all().count(),
            'm':m,
            'tm':tm,
            'mukadam':Mukadam.objects.all(),
            'karkhana':Karkhana.objects.all()
                }
        return render(request,'owner/owner_dashboard.html',context)
    else:
        return redirect('/login/')
    

def add_mukadam(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        if 'Add_Mukadam'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if Mukadam.objects.filter(mobile=mobile).exists():
                messages.warning(request,"Mobile Allready Exits")
                return redirect('/owner/add_mukadam/')
            else:
                Mukadam(
                    name=name,
                    mobile=mobile,
                    pin=pin,
                    status=1
                    ).save()
                messages.success(request,"Mukadam Add Succesfully")
                return redirect('/owner/add_mukadam/')
        if 'Active'in request.POST:
            mid =request.POST.get('id')
            m = Mukadam.objects.get(id=mid)
            m.status = 0
            m.save()
            return redirect('/owner/add_mukadam/')
        if 'Deactive'in request.POST:
            mid =request.POST.get('id')
            m = Mukadam.objects.get(id=mid)
            m.status = 1
            m.save()
            return redirect('/owner/add_mukadam/')
        context={
            'm':Mukadam.objects.all()
            }
        return render(request,'owner/add_mukadam.html',context)
    else:
        return redirect('/login/')
    


def taneg(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        if 'Add_Taneg'in request.POST:
            mukadam = request.POST.get('mukadam')
            karkhana = request.POST.get('karkhana')
            date = request.POST.get('date')
            taneg = request.POST.get('taneg')
            Taneg(
                mukadam_id=mukadam,
                karkhana_id=karkhana,
                added_by='admin',
                taneg=taneg,
                date=date
                ).save()
            messages.success(request,"Taneg Add Succesfully")
            return redirect('/owner/taneg/')

        context={
            'm':Mukadam.objects.all(),
            'k':Karkhana.objects.all(),
            't':Taneg.objects.all()
            }
        return render(request,'owner/taneg.html',context)
    else:
        return redirect('/login/')


def karkhana(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        if 'Add_Karkhana'in request.POST:
            name = request.POST.get('name')
            address = request.POST.get('address')
            #print('name = ',name,'add =',address)
            Karkhana(
                name=name,
                address=address
            ).save()
            return redirect('/owner/karkhana/')
        context={
            'k':Karkhana.objects.all()
        }
        return render(request,'owner/karkhana.html',context)
    else:
        return redirect('/login/')