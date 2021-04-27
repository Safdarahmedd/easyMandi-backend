from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    harvest = models.CharField(max_length=50)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_set')
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='buyer_set')
    amount = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    date = models.DateTimeField()
    description = models.CharField(max_length=250, blank=True, null=True)
    Quantity = models.DecimalField(decimal_places=3, max_digits=8,  blank=True, null=True)

    def __str__(self):
        return self.seller.username + "'s " + self.harvest