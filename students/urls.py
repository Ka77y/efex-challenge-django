from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import StudentsViewSet, StudentsByIdViewSet

router = DefaultRouter()
router.register(r'', StudentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("/<int:pk>", StudentsByIdViewSet.as_view())
]
