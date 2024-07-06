from django.shortcuts import render , redirect 
from django.contrib import messages 
from owner.models import *
from django.db.models import Sum
from datetime import date
# Create your views here.
def index(request):
    Taneg.objects.all().delete()
    #Mukadam.objects.all().delete()
    #Karkhana.objects.all().delete()
    m = Taneg.objects.values('mukadam_id','mukadam__name').annotate(top = Sum('taneg')).order_by('-top')[0:5]
    todays_taneg = Taneg.objects.filter(date__gte=date.today(),date__lte=date.today())
    tm = todays_taneg.values('mukadam_id','mukadam__name').annotate(top = Sum('taneg')).order_by('-top')[0:5]
    context={
        'm':m,
        'tm':tm,
        }
    return render(request, 'home/index.html',context)
 
def login(request):
    if request.session.has_key('owner_mobile'):
        return redirect('/owner/owner_dashbord/')
    if 'Login' in request.POST:
        num = request.POST.get('number')
        pin = request.POST.get('pin')
        owner_login={'mobile':'9921856831','pin':'1252'}
        if owner_login["mobile"]==num and owner_login["pin"]==pin:
            request.session['owner_mobile'] = request.POST.get('number')
            return redirect('/owner/owner_dashbord/')
        else:
            messages.warning(request,"please insert correct information or call more suport 9921856831")
    return render(request, 'home/login.html' )

def logout (request):
    del request.session['owner_mobile']
    return redirect('/')