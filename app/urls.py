from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import MinMaxYearIntervalsApiView
from app.viewsets import YearsViewSet, MoviesViewSet, StudiosViewSet, ProducersViewSet

router = DefaultRouter()
router.register(r"years", YearsViewSet, basename="year")
router.register(r"movies", MoviesViewSet, basename="movie")
router.register(r"studios", StudiosViewSet, basename="studio")
router.register(r"producers", ProducersViewSet, basename="producer")

urlpatterns = [
    path("", include(router.urls)),
    path("intervals/", MinMaxYearIntervalsApiView.as_view(), name="intervals")
]