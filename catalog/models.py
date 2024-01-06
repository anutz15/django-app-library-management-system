from django.db import models
from django.core.validators import MaxValueValidator

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)

    def upload_path(self, filename):
        try:
            name, abc, ext = filename.split(".")
        except:
            name, ext = filename.split(".")

        if self.pk:
            return f"ebooks/{self.pk}-{self.title}.{ext}"
        elif Book.objects.last():
            return f"ebooks/{Book.objects.last().pk+1}-{self.title}.{ext}"
        else:
            return f"ebooks/1-{self.title}.{ext}"
    ebook = models.FileField(upload_to=upload_path, null=True, blank=True)

    number_of_copies=models.PositiveIntegerField(default=0)
    number_of_copies_available=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.ebook.delete()
        super().delete(*args, **kwargs)

