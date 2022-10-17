from django.shortcuts import render

# Create your views here.


# Create your views here.
def post_payment(request):
    return render(request,'payment/payment.html')

def view_payment(request):
        return render(request, 'payment/view.html')
