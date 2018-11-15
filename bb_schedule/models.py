from django.db import models


class Schedule(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    

class ScheduleItem(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE,)
    time = models.TimeField()
    title = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.title