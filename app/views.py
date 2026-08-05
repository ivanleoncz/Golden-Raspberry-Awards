from rest_framework.response import Response
from rest_framework.views import APIView

from app.querysets import get_min_max_intervals_of_worst_movie_winners

class MinMaxYearIntervalsApiView(APIView):

    def get(self, request):
        result = get_min_max_intervals_of_worst_movie_winners()
        return Response(result)
