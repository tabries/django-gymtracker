from datetime import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Routine, Exercise, History
from .serializers import UserSerializer, RoutineSerializer, ExerciseSerializer, HistorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    # permission_classes = [IsAuthenticated]

    #GET /api/routines/1/
    def get_queryset(self):
        return Routine.objects.filter()
    
    #GET api/routines/1/exercises/
    @action(detail=True, methods=['get'])
    def exercises(self, request, pk=None):
        routine = self.get_object()
        exercises = routine.exercises.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    #POST /api/routines/
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        routine_id = self.request.query_params.get('routine_id')
        if routine_id:
            return Exercise.objects.filter(routine_id=routine_id)
        return Exercise.objects.all()

    def perform_create(self, serializer):
        # routine_id comes from the request data, not the URL
        serializer.save()

    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        exercise = self.get_object()
        history_qs = exercise.history_set.all()
        serializer = HistorySerializer(history_qs, many=True)
        return Response(serializer.data)
    
    
class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def perform_create(self, serializer):
        # exercise_id comes from the request data, not the URL
        serializer.save()

    @action(detail=False, methods=['get'], url_path='by_date')
    def by_date(self, request):
        date = request.query_params.get('date')
        if not date:
            return Response({'error': 'date query parameter is required.'}, status=400)
        queryset = self.get_queryset().filter(date=date)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='by_month')
    def by_month(self, request):
        date_str = request.query_params.get('date')
        if not date_str:
            return Response({'error': 'date query parameter is required.'}, status=400)
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        queryset = self.get_queryset().filter(
            date__year=date_obj.year,
            date__month=date_obj.month
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)