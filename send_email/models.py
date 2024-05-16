from django.db import models

# Create your models here.
class EmailModel(models.Model):
    email = models.EmailField(verbose_name="email")
    subject = models.CharField(max_length=50,verbose_name="subject")
    content = models.TextField(max_length=20 , verbose_name="content")

    def __str__(self):
        return f"{self.email} , {self.subject}"