from django.db import models


class MasterClass(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=30)
    order_time = models.DateTimeField(auto_now_add=True)


class GiftCertificate(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=30)
    order_time = models.DateTimeField(auto_now_add=True)
