from django.shortcuts import render , redirect 
from django.contrib import messages 
from owner.models import *
from django.db.models import Sum
from datetime import date
# Create your views here.
def index(request):
    m = Taneg.objects.values('mukadam_id','mukadam__name').annotate(top = Sum('taneg')).order_by('-top')[0:5]
    todays_taneg = Taneg.objects.filter(date__gte=date.today(),date__lte=date.today())
    tm = todays_taneg.values('mukadam_id','mukadam__name').annotate(top = Sum('taneg')).order_by('-top')[0:5]
    context={
        'm':m,
        'tm':tm,
        'mukadam':Mukadam.objects.filter(status=1)
        }
    return render(request, 'home/index.html',context)
 
def login(request):
    if request.session.has_key('owner_mobile'):
        return redirect('/owner/owner_dashboard/')
    if 'Login' in request.POST:
        num = request.POST.get('number')
        pin = request.POST.get('pin')
        owner_login={'mobile':'123','pin':'123'}
        if owner_login["mobile"]==num and owner_login["pin"]==pin:
            request.session['owner_mobile'] = request.POST.get('number')
            return redirect('/owner/owner_dashboard/')
        else:
            messages.warning(request,"please insert correct information or call more suport 9921856831")
    return render(request, 'home/login.html' )

def logout (request):
    del request.session['owner_mobile']
    return redirect('/')

def mukadam_logout(request):
    del request.session['mukadam_mobile']
    return redirect('/')

def vehicle_logout(request):
    del request.session['vehicle_mobile']
    return redirect('/')