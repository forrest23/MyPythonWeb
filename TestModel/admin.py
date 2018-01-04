# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
 
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email','age'),
        }],
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])