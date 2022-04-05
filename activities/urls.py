from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

app_name = "activities"

router = DefaultRouter()
router.register("tags", views.TagViewSet)
router.register("activities", views.ActivityViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
