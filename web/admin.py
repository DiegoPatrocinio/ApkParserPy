from smartsoccer.models import *
from djcelery.models import *
from django.contrib.auth.models import *
from django.contrib.sites.models import Site

from django.contrib import admin
from hashids import Hashids
from django import forms

from django.forms.widgets import Widget, flatatt
from django.utils.html import format_html

class HideInput(Widget):
    def render(self, name, value, attrs=None):
        return format_html('-')

class LinkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['hash_link'].widget = HideInput()
        self.fields['picture'].widget = HideInput()


class LogLinkAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'link', 'ip', 'is_mobile', 'is_tablet', 'is_pc', 'is_bot',
                    'is_touch_capable', 'browser_family', 'browser_version', 'os', 'os_version', 'device']
    search_fields = ['os', 'browser_family', 'device']
    list_filter = ['os', 'browser_family', 'is_pc', 'is_bot', 'is_mobile', 'is_tablet']

class LogActivityAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'user', 'action', 'content', 'ip', 'referer', 'os', 'browser_family']
    search_fields = ['content', 'browser_family', 'os']
    list_filter = ['os', 'browser_family']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'user', 'hash_link_', 'link']
    form = LinkForm

    def save_model(self, request, obj, form, change):
        obj.save()
        h = Hashids(alphabet='abcdefghijklmnopqrstuvwxyz', min_length=6)
        obj.hash_link = h.encode(obj.id)
        obj.save()

class PortalUsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', 'remember_token', 'created_at',
    'updated_at', 'role_id', 'address', 'phone', 'status']


# Admin
#admin.site.register(PortalUsers, PortalUsersAdmin)
admin.site.register(PortalArticles)
admin.site.register(PortalUser)
admin.site.register(MedsosUsers)
admin.site.register(PortalHashTag)

admin.site.unregister(TaskState)
admin.site.unregister(WorkerState)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(PeriodicTask)
# admin.site.unregister(Site)
