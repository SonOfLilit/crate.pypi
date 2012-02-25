from django.contrib import admin

from pypi.models import PyPIMirrorPage
from pypi.models import ChangeLog, Log


class PyPIMirrorPageAdmin(admin.ModelAdmin):
    list_display = ["package", "type"]
    list_filter = ["type"]
    search_fields = ["package__name", "content"]
    raw_id_fields = ["package"]


class ChangeLogAdmin(admin.ModelAdmin):
    list_display = ["package", "version", "timestamp", "action", "handled"]
    list_filter = ["timestamp", "handled"]
    search_fields = ["package", "action"]


class LogAdmin(admin.ModelAdmin):
    list_display = ["type", "created", "message"]
    list_filter = ["type", "created"]


admin.site.register(PyPIMirrorPage, PyPIMirrorPageAdmin)
admin.site.register(ChangeLog, ChangeLogAdmin)
admin.site.register(Log, LogAdmin)
