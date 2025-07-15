from rest_framework import serializers
from .models import Routine, Exercise, History, Weight


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ["id", "name", "exercises"]
        read_only_fields = ["exercises"]


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "routine", "name", "description"]


class HistorySerializer(serializers.ModelSerializer):
    exercise_name = serializers.ReadOnlyField(source="exercise.name")

    class Meta:
        model = History
        fields = [
            "id",
            "exercise",
            "exercise_name",
            "date",
            "notes",
            "sets",
            "reps",
            "weightKg",
            "durationMin",
        ]

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ["id", "date", "notes", "weightKg"]