from django.db import models

class Routine(models.Model):
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
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True)
    sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    weightKg = models.FloatField(blank=True, null=True)
    durationMin = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.exercise.name} on {self.date}"
    
class Weight(models.Model):
    date = models.DateField()
    notes = models.TextField(blank=True)
    weightKg = models.FloatField()

    def __str__(self):
        return f"{self.weightKg} on {self.date}"