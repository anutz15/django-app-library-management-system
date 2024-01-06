from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest
from duebooks.forms import getrollnuoform,amountform
from django.db import connection
import razorpay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def showduebooks(request):
    if request.method=="POST":
        f=getrollnuoform(request.POST)
        if f.is_valid():
            data=f.cleaned_data
            rno=data.get("rollno")
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM issuebook_issuedbooks WHERE rollnumber=%s",[str(rno)])
                results=cursor.fetchall()
            a=[]
            b=[]
            c=[]
            d=[]
            e=[]
            print(results)
            if len(results) == 0:
                a.append("None")
                b.append("None")
                c.append("None")
                d.append("None")
                e.append("None")
            for i in results:
                a.append(i[0])
                b.append(i[2])
                c.append(i[3])
                d.append(i[4])
                e.append(i[6])
            context=zip(a,b,c,d,e)
            return render(request,"showduebooks_show.html",{'context':context})
        else:
            return HttpResponse("Invalid Form!")
    else:
        f=getrollnuoform()
        return render(request,"showduebooks_getrno.html",{'form':f})

def whichpay(request):
    if request.method=="POST":
        form=amountform(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            global amt
            amt=int(data.get("amt"))
            print(amt)
            bid=data.get("bookid")
            with connection.cursor() as cursor:
                cursor.execute("DELETE from issuebook_issuedbooks WHERE id = %s",[bid])
            return HttpResponseRedirect("payfees")
        else:
            return HttpResponse("Invalid!")
    else:
        form=amountform()
        return render(request,"howmuchtopay.html",{'form':form})





def payduefees(request):
    global razorpay_client
    razorpay_client= razorpay.Client(auth=('rzp_test_SDx8nsXtJsauaJ','GIyUnSB9EwOFCVO14GcQDPlg'))

    currency = 'INR'
    global amt
    amount=amt*100
    razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    callback_url = '/'

    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_SDx8nsXtJsauaJ'
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'payment.html', context=context)


@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                global amt
                amount = amt  
                try:


                    razorpay_client.payment.capture(payment_id, amount)

                    return render(request, 'paymentsuccess.html')
                except:

                    return render(request, 'paymentfail.html')
            else:
                return render(request, 'paymentfail.html')
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()