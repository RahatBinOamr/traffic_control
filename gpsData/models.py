from django.db import models
class TrafficData(models.Model):
    # Define choices for road_name
    ROAD_NAME_CHOICES = [
        ('Bahaddarhat', 'Bahaddarhat'),
        ('GEC Circle', 'GEC Circle'),
        ('New Market', 'New Market'),
        ('2 no Gate', '2 no Gate'),
        ('Oxygen Mor', 'Oxygen Mor'),
        ('Muradpur Mor', 'Muradpur Mor'),
        ('Agrabad Commercial Area', 'Agrabad Commercial Area'),
        ('EPZ', 'EPZ'),
        ('Chattogram Port', 'Chattogram Port'),
        ('Lalkhan Bazar', 'Lalkhan Bazar'),
        ('Wasa Mor', 'Wasa Mor'),
    ]

    # GPS Data
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    timestamp = models.DateTimeField()

    # Traffic Data
    traffic_speed = models.FloatField(help_text="Speed in km/h")
    traffic_density = models.IntegerField(null=True, blank=True)
    traffic_condition = models.CharField(
        max_length=50,
        choices=[
            ('traffic-heavy', 'Heavy'),
            ('traffic-moderate', 'Moderate'),
            ('traffic-free', 'Free-flowing'),
        ]
    )

    # Road & Location Info
    road_name = models.CharField(max_length=100, choices=ROAD_NAME_CHOICES)
    road_type = models.CharField(
        max_length=50,
        choices=[
            ('highway', 'Highway'),
            ('main_road', 'Main Road'),
            ('small_road', 'Small Road'),
        ]
    )
    distance_between_points = models.FloatField(help_text="Distance in meters")

    # Time-Based Info
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
            ('Sunday', 'Sunday'),
        ]
    )
    hour_of_day = models.TimeField()

    month_collected = models.CharField(
        max_length=10,
        choices=[
            ('October', 'October'),
            ('November', 'November'),
            ('December', 'December'),
            ('January', 'January'),
            ('February', 'February'),
            ('March', 'March'),
        ]
    )

    def __str__(self):
        return f"{self.road_name} - {self.timestamp}"
