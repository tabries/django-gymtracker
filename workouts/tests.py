from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Routine, Exercise, History

class UserTests(APITestCase):
    def create_user(self, username='testuser', password='testpass'):
        return User.objects.create_user(username=username, password=password)

    def test_user_creation(self):
        response = self.client.post(reverse('user-list'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

class RoutineTests(APITestCase):
    def setUp(self):
        self.user = self.create_user()

    def create_routine(self, name='Test Routine'):
        return Routine.objects.create(name=name, user=self.user)

    def test_routine_creation(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('routine-list'), {'name': 'Test Routine'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Routine.objects.count(), 1)
        self.assertEqual(Routine.objects.get().name, 'Test Routine')

class ExerciseTests(APITestCase):
    def setUp(self):
        self.user = self.create_user()
        self.routine = self.create_routine()

    def create_exercise(self, name='Test Exercise'):
        return Exercise.objects.create(name=name, routine=self.routine)

    def test_exercise_creation(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('exercise-list'), {'name': 'Test Exercise', 'routine': self.routine.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Exercise.objects.count(), 1)
        self.assertEqual(Exercise.objects.get().name, 'Test Exercise')

class HistoryTests(APITestCase):
    def setUp(self):
        self.user = self.create_user()
        self.exercise = self.create_exercise()

    def create_history(self, sets=3, reps=10):
        return History.objects.create(sets=sets, reps=reps, exercise=self.exercise)

    def test_history_creation(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('history-list'), {'sets': 3, 'reps': 10, 'exercise': self.exercise.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(History.objects.count(), 1)
        self.assertEqual(History.objects.get().sets, 3)