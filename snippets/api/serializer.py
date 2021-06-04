from rest_framework import serializers

from snippets.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['title', 'time', 'todo']