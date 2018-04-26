from backoffice.models import *
from djcelery.models import *
from django.contrib.auth.models import *
from django.contrib.sites.models import Site

from django.contrib import admin


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Applications._meta.fields if field.name != "id"]

# Admin
admin.site.register(Applications, ApplicationsAdmin)

admin.site.unregister(TaskState)
admin.site.unregister(WorkerState)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(PeriodicTask)
admin.site.unregister(Site)
