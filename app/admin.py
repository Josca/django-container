from django.contrib import admin
from .models import Sample

# Admin classes to show tables columns in admin web interface.


class SampleAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'value')


admin.site.register(Sample, SampleAdmin)
