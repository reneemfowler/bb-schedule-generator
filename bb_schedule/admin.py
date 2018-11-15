from django.contrib import admin
from .models import Schedule, ScheduleItem


class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)
    search_fields = ('title',)

class ScheduleItemAdmin(admin.ModelAdmin):
    model = ScheduleItem
    list_display = ('time', 'title', 'notes', 'schedule')
    ordering = ('schedule',)
    search_fields = ('schedule', 'time', 'title',)

    
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(ScheduleItem, ScheduleItemAdmin)