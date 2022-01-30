from django.shortcuts import render,redirect
from .models import AddDonation,Category,DonatedMember,Transaction
import razorpay
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
client = razorpay.Client(auth=("rzp_test_Q4uje180fau9as", "jtfzK7K8BPs4j8X1acgL45l0"))
today = datetime.now().date()
current_time = datetime.now().time()

def donate(request):
    data = AddDonation.objects.all().values()
    cat = Category.objects.all().values()
    context = dict()
    context['data'] = data
    context['cat'] = cat
    return render(request, 'donate.html', context)

def donatenow(request,id):
    id = id
    data = AddDonation.objects.filter(id=id).values()
    data2 = AddDonation.objects.all().values()
    context = dict()
    context['data'] = data
    context['data2'] = data2

    return render(request, 'donation.html', context)

def add_donation(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        amount_paid = request.POST['amount']
        seva_name = request.POST['seva_name']
        obj = DonatedMember(name=name,phone=phone,email=email,amount_paid=amount_paid,seva_name=seva_name)
        obj.save()

        data = DonatedMember.objects.filter(id=obj.id).values()
        context = dict()
        context['seva_name'] = data[0]['seva_name']
        context['name'] = data[0]['name']
        context['phone'] = data[0]['phone']
        context['email'] = data[0]['email']
        context['order_id'] = data[0]['id']
        context['amount_paid'] = (data[0]['amount_paid'])*100

        context['data'] = data
        return render(request,'confirm_pay.html',context)

@csrf_exempt
def charged(request):
    if request.method == 'POST':
        payment_id = request.POST['razorpay_payment_id']
        payment_amount = request.POST['amount_paid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        id = request.POST['id']

        payment_currency = "INR"
        resp = client.payment.capture(payment_id, payment_amount, {"currency": payment_currency})
        print(resp)
        pay_id = resp['id']
        pay_amount = resp['amount']
        pay_method = resp['method']
        pay_refund = resp['amount_refunded']
        pay_bank = resp['bank']
        pay_fee = resp['fee']
        pay_tax = resp['tax']

        pay_amount = int(pay_amount)




        DonatedMember.objects.filter(id=id).update(razorpay_id=pay_id, flag=1)

        obj = Transaction( name=name,  txn_id=pay_id,
                          phone=phone,transaction_type=pay_method,
                          paid_amount=payment_amount, Date=today, Time=current_time)
        obj.save()

        return redirect('donate')


    return redirect('donate')