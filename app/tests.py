from io import StringIO

from app.models import YearModel, MovieModel, ProducerModel

from django.conf import settings
from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class TestDataIngestionAndApi(APITestCase):

    out = StringIO()
    err = StringIO()

    @classmethod
    def setUp(cls):
        call_command(command_name="import_worst_movies_dataset",
                     verbosity=0, stdout=cls.out, stderr=cls.err)

    def test_import_worst_movies_dataset_success(self):
        with open(settings.MOVIELIST_DATASET, "r") as f:
            number_of_lines = len(f.readlines()) - 1 # header doesn't count, expecting 206 lines (movies)
        self.assertIn(f"{number_of_lines} movies imported!",  self.out.getvalue())

    def test_intervals_endpoint(self):

        url = reverse("intervals")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="endpoint 'intervals' is not available")
        self.assertIn("min", response.data, msg="json response does not contain an object 'min'")
        self.assertEqual(len(response.data["min"]), 1, msg="'min' object does not contain a list of two elements")
        self.assertIn("max", response.data, msg="json response does not contain an object 'max'")
        self.assertEqual(len(response.data["max"]), 1, msg="'max' object does not contain a list of two elements")

        expected_response = {
            'min': [
                {
                    'producer': 'Joel Silver',
                    'interval': 1,
                    'previousWin': 1990,
                    'followingWin': 1991
                }
            ],
            'max': [
                {
                    'producer': 'Matthew Vaughn',
                    'interval': 13,
                    'previousWin': 2002,
                    'followingWin': 2015
                }
            ]
        }
        self.assertEqual(response.data, expected_response)

    def test_intervals_endpoint_after_db_modification_new_max_interval(self):

        year_2019 = YearModel.objects.get(year=2019)
        new_movie = MovieModel.objects.create(title="I made this up", year=year_2019, winner=True)
        producer_bo_derek = ProducerModel.objects.get(name="Bo Derek")
        producer_bo_derek.movies.add(new_movie)

        url = reverse("intervals")
        response = self.client.get(url)
        expected_response = {
            'min': [
                {
                    'producer': 'Joel Silver',
                    'interval': 1,
                    'previousWin': 1990,
                    'followingWin': 1991
                }
            ],
            'max': [
                {
                    'producer': 'Bo Derek',
                    'interval': 35,  # <---------------------------- new movie winner from 2019
                    'previousWin': 1984,
                    'followingWin': 2019
                }
            ]
        }

        self.assertEqual(response.data, expected_response)


    def test_intervals_endpoint_after_db_modification_new_min_interval(self):

        year_1992 = YearModel.objects.get(year=1992)
        new_movie = MovieModel.objects.create(title="I made this other up", year=year_1992, winner=True)
        producer_bo_derek = ProducerModel.objects.get(name="Joel Silver")
        producer_bo_derek.movies.add(new_movie)

        url = reverse("intervals")
        response = self.client.get(url)
        expected_response = {
            'min': [
                {
                    'producer': 'Joel Silver',
                    'interval': 1,
                    'previousWin': 1990,
                    'followingWin': 1991
                }
            ],
            'max': [
                {
                    'producer': 'Matthew Vaughn',
                    'interval': 13,
                    'previousWin': 2002,
                    'followingWin': 2015
                }
            ]
        }

        self.assertEqual(response.data, expected_response)