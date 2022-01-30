from django.contrib import admin
from .models import *
# Register your models here.


class DonateAdmin(admin.ModelAdmin):

    list_display = ['title']
    list_filter = ['title',]

admin.site.register(Category,DonateAdmin)

class AddDonateAdmin(admin.ModelAdmin):

    list_display = ['name_of_donation']
    list_filter = ['name_of_donation',]

admin.site.register(AddDonation,AddDonateAdmin)

class DonatedMemberAdmin(admin.ModelAdmin):

    list_display = ['name','phone','seva_name','amount_paid','transaction_date']
    list_filter = ['seva_name','flag']

admin.site.register(DonatedMember,DonatedMemberAdmin)

class TransactionAdmin(admin.ModelAdmin):

    list_display = ['name','phone']
    list_filter = ['name',]

admin.site.register(Transaction, TransactionAdmin)