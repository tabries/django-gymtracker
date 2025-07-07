from django.contrib.auth.models import User
from django.db import models

class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    routine = models.ForeignKey(Routine, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True)
    sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    weightKg = models.FloatField(blank=True, null=True)
    durationMin = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} on {self.date}"