from rest_framework import routers
from rest_framework.routers import DefaultRouter

from snippets.api.viewsets import TodoViewSet

router = DefaultRouter()
router.register('todo', TodoViewSet)


