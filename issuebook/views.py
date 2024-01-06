from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse
from issuebook.forms import issueform,issueformmodel
from reportlab.pdfgen import canvas

# Create your views here.
def issuebooknow(request,bookid):
    if request.method=="POST":
        f=issueformmodel(request.POST)
        if f.is_valid():
            f.save()
            data=f.cleaned_data
            c = canvas.Canvas(str(data.get("rollnumber"))+'_'+str(bookid)+".pdf")
            c.drawString(100, 750, "--------------------------YOUR ISSUE REPORT--------------------------")
            c.drawString(100, 700, "Your Roll Number: "+str(data.get("rollnumber")))
            c.drawString(100, 650, "Your Book ID: "+str(bookid))
            c.drawString(100, 600, "Number of Copies Issued: "+str(data.get("number_of_copies")))
            c.drawString(100, 550, "Reason For Issue: "+str(data.get("reason_for_issue")))
            c.drawString(100, 500, "Issuedate: "+str(data.get("date_of_issue")))
            c.drawString(100, 450, "Last date to Submit: "+str(data.get("date_of_submission")))
            c.drawString(100, 400, "--------------------------THANK YOU--------------------------")

            c.save()
            pdf_path = str(data.get("rollnumber"))+'_'+str(bookid)+".pdf"
            with open(pdf_path, 'r',encoding='utf-8',errors='ignore') as f:
                file_data = f.read()
            response = HttpResponse(file_data,content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename='+pdf_path+'.pdf'

            return response
        else:
            print(bookid)
            return render(request,"issuebooknow_template.html",{'form':f})
    else:
        form=issueformmodel()
        return render(request, "issuebooknow_template.html", {'form': form,'bid':str(bookid)})


