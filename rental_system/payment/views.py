from django.shortcuts import render
from payment.models import Payment
from user.models import User
from bike.models import Bike
import datetime
# Create your views here.


# Create your views here.
def post_payment(request):
    ob1 = User.objects.all()
    ob2 = Bike.objects.all()
    context = {
        'u': ob1,
        'v': ob2
    }


    if request.method == 'POST':
        obj=Payment()
        obj.amount=request.POST.get('amount')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.u_id=request.POST.get('ee')
        obj.b_id=request.POST.get('ef')

        obj.save()
    return render(request,'payment/payment.html',context)

def view_payment(request):
    obj=Payment.objects.all()
    context= {
        'x':obj
    }
    return render(request, 'payment/view.html', context)
