from django.contrib import admin

# Register your models here.
from vehiclemsapp.models import Vehicle, VehicleAvailability, PurchaseOrder, BillingOrder

class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = ('id', 'vehicle_name','vehicle_type','vehicle_price','vehicle_brand','vehicle_model','vehicle_status')
    list_filter = ('id', 'vehicle_name','vehicle_type','vehicle_price','vehicle_brand','vehicle_model','vehicle_status')
    ordering = ['vehicle_name']

class VehicleAvailabilityAdmin(admin.ModelAdmin):
    model = VehicleAvailability
    list_display = ('id','vehicle_availability_status','vehicle_availability_comments','vehicle_name')
    list_filter = ('id','vehicle_availability_status','vehicle_availability_comments','vehicle_name')
    ordering = ['vehicle_name']


class PurchaseOrderAdmin(admin.ModelAdmin):
    model = PurchaseOrder
    list_display = ('id','purchaseorder_date','totalnumberordered','purchaseorder_status','vehicle_name','vehicle_availability')
    list_filter = ('id','purchaseorder_date','totalnumberordered','purchaseorder_status','vehicle_name','vehicle_availability')
    ordering = ['vehicle_name']


class BillingOrderAdmin(admin.ModelAdmin):
    model = BillingOrder
    list_display = ('id','billingorder_price','billingorder_status','billingorder_date','purchaseorder_details')
    list_filter = ('id','billingorder_price','billingorder_status','billingorder_date','purchaseorder_details')
    ordering = ['billingorder_price']


admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(VehicleAvailability,VehicleAvailabilityAdmin)
admin.site.register(PurchaseOrder,PurchaseOrderAdmin)
admin.site.register(BillingOrder,BillingOrderAdmin)
