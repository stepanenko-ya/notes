from django.urls import path, include
from .views import NoteViewSet
from rest_framework import routers


class CustomRouter(routers.DefaultRouter):
    def get_method_map(self, viewset, method_map):
        return {http_method: method_map[http_method] for http_method in method_map.keys() if http_method in ['get', 'post', 'patch', 'put', 'delete']}


router = CustomRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
