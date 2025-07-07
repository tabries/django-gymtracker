from rest_framework import serializers
from .models import User, Routine, Exercise, History


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ["id", "name", "user", "exercises"]
        read_only_fields = ["user", "exercises"]


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "routine", "name", "description"]


class HistorySerializer(serializers.ModelSerializer):
    exercise_name = serializers.ReadOnlyField(source="exercise.name")

    class Meta:
        model = History
        read_only_fields = ["user"]
        fields = [
            "id",
            "user",
            "exercise",
            "exercise_name",
            "date",
            "notes",
            "sets",
            "reps",
            "weightKg",
            "durationMin",
        ]
