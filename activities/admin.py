from django.contrib import admin

from .models import Activity, Tag

admin.site.register(Activity)
admin.site.register(Tag)
admin.site.site_header = "Activities API administration"
admin.site.site_title = "Activities API"
