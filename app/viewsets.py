
from rest_framework.viewsets import ModelViewSet

from app.models import YearModel, MovieModel, StudioModel, ProducerModel
from app.serializers import YearSerializer, MovieSerializer, StudioSerializer, ProducerSerializer

class YearsViewSet(ModelViewSet):
    queryset = YearModel.objects.all()
    serializer_class = YearSerializer

class MoviesViewSet(ModelViewSet):
    queryset = MovieModel.objects.select_related("year")
    serializer_class = MovieSerializer

class StudiosViewSet(ModelViewSet):
    queryset = StudioModel.objects.all()
    serializer_class = StudioSerializer

class ProducersViewSet(ModelViewSet):
    queryset = ProducerModel.objects.all()
    serializer_class = ProducerSerializer
