import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Vehicle(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False)
    vehicle_name = models.CharField(max_length=100,blank=False,null=False,default='')
    vehicle_type = models.CharField(max_length=100, blank=False,null=False,default='')
    vehicle_price = models.FloatField()
    vehicle_brand = models.CharField(max_length=60,blank=False,null=False,default='')
    vehicle_model = models.CharField(max_length=30, blank=False, null=False, default='')
    vehicle_status = models.CharField(max_length=30, blank=False, null=False, default='')
    inventory_admincontact = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehicle_name)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicle'

class VehicleAvailability(models.Model):

     id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False)
     vehicle_availability_status = models.CharField(max_length=100, blank=False, null=False, default='')
     vehicle_availability_comments = models.CharField(max_length=200, blank=False, null=False, default='')
     vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE,related_name='vehicleavails')

     def __str__(self):
        return str(self.vehicle_availability_status)

     class Meta:
        verbose_name = 'VehicleAvailability'
        verbose_name_plural = 'VehicleAvailability'

class PurchaseOrder(models.Model):

     id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False)
     purchaseorder_date = models.DateTimeField()
     totalnumberordered = models.IntegerField()
     purchaseorder_status = models.CharField(max_length=30, blank=False, null=False, default='')
     vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicles')
     supplier_contact = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
     vehicle_availability = models.ForeignKey(VehicleAvailability, on_delete=models.CASCADE,related_name='purchaseorders')

     def __str__(self):
        return str(self.purchaseorder_status)

     class Meta:
        verbose_name = 'PurchaseOrder'
        verbose_name_plural = 'PurchaseOrder'

class BillingOrder(models.Model):

     id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False)
     billingorder_price = models.FloatField()
     billingorder_status = models.CharField(max_length=30, blank=True, null=True)
     billingorder_date = models.DateTimeField()
     purchaseorder_details = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE,related_name='billingorders')

     def __str__(self):
       return str(self.billingorder_status)

     class Meta:
        verbose_name = 'BillingOrder'
        verbose_name_plural = 'BillingOrder'

