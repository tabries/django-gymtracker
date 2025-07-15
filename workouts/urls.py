from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoutineViewSet, ExerciseViewSet, HistoryViewSet, WeightViewSet

router = DefaultRouter()
router.register(r'routines', RoutineViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'weight', WeightViewSet)

urlpatterns = [
    path('', include(router.urls)),
]