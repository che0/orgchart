from django.contrib import admin
from treeadmin.admin import TreeAdmin
from orgchart import models

class PhoneNumberAdmin(admin.TabularInline):
    model = models.PhoneNumber

class TitleAdmin(admin.TabularInline):
    model = models.Title

class PersonAdmin(TreeAdmin):
    list_display = ('photo_html', 'indented_short_title', 'title', 'email', 'skype', 'phone')
    inlines = [TitleAdmin, PhoneNumberAdmin]
    
    class Media:
        css = {
            "all": ("orgchart/admin_styles.css",)
        }

admin.site.register(models.Person, PersonAdmin)
