from django.db import models

# Create your models here.


class Contact(models.Model):
    """
    Contact Model
    """

    class Meta:
        verbose_name_plural = 'Messages'

    
    first_name = models.CharField(max_length=50, null=False, blank=False)
    second_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    message = models.TextField(max_length=1000, null=False, blank=False)
    contact_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.email)