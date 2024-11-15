from django.shortcuts import render,redirect
from owner.models import *
# Create your views here.
def vehicle_dashboard(request):
    if request.session.has_key('vehicle_mobile'):
        vehicle_mobile = request.session['vehicle_mobile']
        v = Vehicle.objects.filter(mobile=vehicle_mobile).first()
        if v:
            v = Vehicle.objects.get(mobile=vehicle_mobile)
        context={
            'v':v
        }
        return render(request, 'vehicle/vehicle_dashboard.html',context)
    else:
        return redirect('/login/')