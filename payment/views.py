from django.shortcuts import render
from payment.models import Payment
from user.models import User
from bike.models import Bike
from request.models import Request
import datetime
# Create your views here.


# Create your views here.
def post_payment(request,idd):
    ss = request.session["uid"]
    # obk = User.objects.get(u_id=ss)
    # ob2 = Bike.objects.all()
    obk = Request.objects.get(r_id=idd)
    context = {
        'nm': obk,
        # 'v': ob2
    }
    if request.method == 'POST':
        obj=Payment()
        obj.amount=request.POST.get('amount')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.u_id=ss
        obj.b_id=obk.b_id
        obj.save()
    return render(request,'payment/payment.html',context)

def view_payment(request):
    obj=Payment.objects.all()
    context= {
        'x':obj
    }
    return render(request, 'payment/view.html', context)
