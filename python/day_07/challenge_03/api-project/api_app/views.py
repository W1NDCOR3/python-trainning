from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db import connection

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        # Log the data being sent in the request for debugging
        print("Data received in PUT request:", request.data)
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if not serializer.is_valid():
            # Log the validation errors for debugging
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_update(serializer)
        return Response(serializer.data)
    
        # Add a custom action to delete all tasks
      # Custom action to delete all tasks and reset the primary key sequence
    
    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all(self, request):
        # Delete all tasks
        Task.objects.all().delete()

        # Reset the auto-incrementing ID sequence
        with connection.cursor() as cursor:
            # For SQLite
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='api_app_task';")

            # For PostgreSQL, use this instead:
            # cursor.execute("ALTER SEQUENCE api_app_task_id_seq RESTART WITH 1;")

        return Response({"message": "All tasks have been deleted and ID sequence reset."}, status=status.HTTP_204_NO_CONTENT)
