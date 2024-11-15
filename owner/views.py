from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db.models import Sum, Max
from datetime import date
from django.core.paginator import Paginator
import time
# Create your views here.
def owner_dashboard(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        m = Taneg.objects.values('mukadam_id','mukadam__name').annotate(top = Sum('taneg')).order_by('-top')[0:5]
        todays_taneg = Taneg.objects.filter(date__gte=date.today(),date__lte=date.today())
        tm = todays_taneg.values('mukadam_id','mukadam__name').annotate(top = Sum('taneg')).order_by('-top')[0:5]
        context={
            'total_mukadam':Mukadam.objects.all().count(),
            'total_karkhana':Karkhana.objects.all().count(),
            'total_vehicle':Vehicle.objects.all().count(),
            'm':m,
            'tm':tm,
            'mukadam':Taneg.objects.values('mukadam_id','mukadam__name').annotate(mukadam = Sum('taneg')).order_by('-mukadam'),
            'karkhana':Karkhana.objects.all(),
            'vehicle':Vehicle.objects.all(),
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
            vehicle = request.POST.get('vehicle')
            karkhana = request.POST.get('karkhana')
            date = request.POST.get('date')
            taneg = request.POST.get('taneg')
            Taneg(
                mukadam_id=mukadam,
                vehicle_id=vehicle,
                karkhana_id=karkhana,
                added_by='admin',
                taneg=taneg,
                date=date
                ).save()
            messages.success(request,"Taneg Add Succesfully")
            time.sleep(1)
            return redirect('/owner/taneg/')
        if 'T_delete'in request.POST:
            tid = request.POST.get('tid')
            print(tid)
            Taneg.objects.get(id=tid).delete()
            return redirect('/owner/taneg/')
        t = Taneg.objects.all().order_by('-date')
        paginator = Paginator(t,20) 
        page_number = request.GET.get('page')
        t = paginator.get_page(page_number)
        context={
            'm':Mukadam.objects.filter(status=1),
            'v':Vehicle.objects.filter(status=1),
            'k':Karkhana.objects.all(),
            't':t,
            'delete_pin':'1253'
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
    


def vehicle(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        if 'Add_vehicle'in request.POST:
            owner_name = request.POST.get('owner_name')
            vehicle_number = request.POST.get('vehicle_number')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            print(vehicle_number)
            if Vehicle.objects.filter(vehicle_number=vehicle_number).exists():
                messages.warning(request,"Vehicle Number Allready Exits")
                return redirect('/owner/vehicle/')
            elif Vehicle.objects.filter(mobile=mobile).exists():
                messages.warning(request,"Mobile Allready Exits")
                return redirect('/owner/vehicle/')
            else:
                Vehicle(
                    owner_name=owner_name,
                    vehicle_number=vehicle_number,
                    mobile = mobile,
                    pin = pin,
                    status=1
                    ).save()
                messages.success(request,"Vehicle Added Succesfully")
                return redirect('/owner/vehicle/')
        if 'Active'in request.POST:
            vid =request.POST.get('id')
            v = Vehicle.objects.get(id=vid)
            v.status = 0
            v.save()
            return redirect('/owner/vehicle/')
        if 'Deactive'in request.POST:
            vid =request.POST.get('id')
            v = Vehicle.objects.get(id=vid)
            v.status = 1
            v.save()
            return redirect('/owner/vehicle/')
        context={
            'v':Vehicle.objects.all()
            }
        return render(request,'owner/vehicle.html',context)
    else:
        return redirect('/login/')
    



def report(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        from_date = ''
        to_date = ''
        result = ''
        total = ''
        if 'Search'in request.POST:
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')
            mid = request.POST.get('mukadam')
            vid = request.POST.get('vehicle')
            kid = request.POST.get('karkhana')
            if mid == '' and vid == '' and kid == '':
                messages.warning(request,"Please select Mukadam or Vehicle anyone")
            if mid == '0':
                result = Taneg.objects.filter(date__gte=from_date,date__lte=to_date).order_by('-taneg')
                total = result.aggregate(Sum('taneg'))
                total = total['taneg__sum']
            elif mid:
                result = Taneg.objects.filter(date__gte=from_date,date__lte=to_date,mukadam_id=mid).order_by('-date')
                total = result.aggregate(Sum('taneg'))
                total = total['taneg__sum']
            elif vid == '0':
                result = Taneg.objects.filter(date__gte=from_date,date__lte=to_date).order_by('-date')
                total = result.aggregate(Sum('taneg'))
                total = total['taneg__sum']
            elif vid:
                result = Taneg.objects.filter(date__gte=from_date,date__lte=to_date,vehicle_id=vid).order_by('-date')
                total = result.aggregate(Sum('taneg'))
                total = total['taneg__sum']
            elif kid == '0':
                result = Taneg.objects.filter(date__gte=from_date,date__lte=to_date).order_by('-date')
                total = result.aggregate(Sum('taneg'))
                total = total['taneg__sum']
            elif kid:
                result = Taneg.objects.filter(date__gte=from_date,date__lte=to_date,karkhana_id=kid).order_by('-date')
                total = result.aggregate(Sum('taneg'))
                total = total['taneg__sum']
        context={
            'm':Mukadam.objects.all(),
            'v':Vehicle.objects.all(),
            'k':Karkhana.objects.all(),
            'from_date':from_date,
            'to_date':to_date,
            'result':result,
            'total':total,
                }
        return render(request,'owner/report.html',context)
    else:
        return redirect('/login/')