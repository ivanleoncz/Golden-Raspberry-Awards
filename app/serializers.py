from rest_framework.serializers import ModelSerializer

from app.models import YearModel, MovieModel, StudioModel, ProducerModel

class YearSerializer(ModelSerializer):
    class Meta:
        model = YearModel
        fields = ["id", "year"]

class MovieSerializer(ModelSerializer):

    class Meta:
        model = MovieModel
        fields = ["id", "title", "winner", "year"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["year"] = YearSerializer(instance.year).data
        return rep

class StudioSerializer(ModelSerializer):
    class Meta:
        model = StudioModel
        fields = ["id", "name"]

class ProducerSerializer(ModelSerializer):
    class Meta:
        model = ProducerModel
        fields = ["id", "name"]
