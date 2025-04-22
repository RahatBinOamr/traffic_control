import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import TrafficData

def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="traffic_data.csv"'
    writer = csv.writer(response)
    fields = [field.name for field in modeladmin.model._meta.fields]
    writer.writerow(fields)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])
    return response

export_as_csv.short_description = "Export Selected as CSV"

@admin.register(TrafficData)
class TrafficDataAdmin(admin.ModelAdmin):
    list_display = (
        'road_name', 'road_type', 'timestamp',
        'traffic_speed', 'traffic_condition',
        'latitude', 'longitude', 'month_collected'
    )
    list_filter = ('road_type', 'traffic_condition', 'month_collected', 'day_of_week')
    search_fields = ('road_name', 'traffic_condition', 'timestamp')
    ordering = ('-timestamp',)
    actions = [export_as_csv]
