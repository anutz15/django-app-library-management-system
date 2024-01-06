from django.db import models
import datetime
# Create your models here.

class issuedbooks(models.Model):
    bookid=models.IntegerField()
    rollnumber=models.CharField(max_length=100)
    number_of_copies=models.IntegerField()
    reason_for_issue=models.TextField()
    date_of_issue=models.DateField(default=datetime.date.today())
    date_of_submission=models.DateField(default=datetime.date.today())