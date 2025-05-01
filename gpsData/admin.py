import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import TrafficData
import random
from datetime import datetime, time
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
    ordering = ('-timestamp','road_name', 'road_type', 'timestamp',
        'traffic_speed', 'traffic_condition',
        'latitude', 'longitude', 'month_collected')
    actions = [export_as_csv]
    def get_changeform_initial_data(self, request):
        traffic_conditions = ['traffic-heavy', 'traffic-moderate', 'traffic-free']
        road_names = [
            'Bahaddarhat', 'GEC Circle', 'New Market', '2 no Gate', 'Oxygen Mor',
            'Muradpur Mor', 'Agrabad Commercial Area', 'EPZ',
            'Chattogram Port', 'Lalkhan Bazar', 'Wasa Mor'
        ]
        road_types = ['highway', 'main_road', 'small_road']
        months = ['October', 'November', 'December', 'January', 'February', 'March']
        
        # Fixed hour_of_day options
        fixed_hours = [
            time(6, 0),   # 6:00 AM
            time(12, 0),  # 12:00 PM
            time(16, 0),  # 4:00 PM
            time(18, 0),  # 6:00 PM
            time(0, 0),   # 12:00 AM
        ]

        # Randomize traffic condition
        condition = random.choice(traffic_conditions)

        if condition == 'traffic-heavy':
            speed = random.uniform(0, 20)
            density = random.randint(100, 1500)
            distance = random.uniform(5, 10)
        elif condition == 'traffic-moderate':
            speed = random.uniform(30, 50)
            density = random.randint(30, 80)
            distance = random.uniform(15, 30)
        else:
            speed = random.uniform(60, 100)
            density = random.randint(10, 20)
            distance = random.uniform(50, 100)

        now = datetime.now()
        selected_hour = random.choice(fixed_hours)
        day_of_week = now.strftime('%A')
        month = random.choice(months)

        return {
            'latitude': round(random.uniform(22.0, 23.0), 7),
            'longitude': round(random.uniform(91.0, 92.0), 7),
            'timestamp': now,
            'traffic_speed': round(speed, 2),
            'traffic_density': density,
            'traffic_condition': condition,
            'road_name': random.choice(road_names),
            'road_type': random.choice(road_types),
            'distance_between_points': round(distance, 2),
            'day_of_week': day_of_week,
            'hour_of_day': selected_hour,
            'month_collected': month,
        }