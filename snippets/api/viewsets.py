from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializer import TodoSerializer
from snippets.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    '''Extras; to customize use these functions'''
    # getting the latest entry at the top; the one to be executed last
    @action(methods=['get'], detail=False)
    def latest(self,request):
        latest = self.get_queryset().order_by('time').last() # getting the last created; the get_queryset is a method in the ModelViewSet class
        serializer = self.get_serializer_class()(latest)
        return Response(serializer.data)