from django.core.management.base import BaseCommand
from django.conf import settings

from app.models import YearModel, MovieModel, StudioModel, ProducerModel

class Command(BaseCommand):

    help = "Imports Worst Picture/Movie dataset from Golden Raspberry Awards"

    def handle(self, *args, **options):
        imported_movies = 0
        self.stdout.write(self.style.NOTICE("Importing..."))
        dataset = settings.MOVIELIST_DATASET
        with open(dataset, 'r') as ds:

            next(ds) # Discard CSV header

            self.stdout.write(self.style.NOTICE(f"Processing..."))
            for line in ds:
                line = line.strip("\n").strip(",").split(",")

                year: int = int(line[0])
                movie: list[str] = [line[1]]
                winner: bool = False

                db_year = YearModel.objects.get_or_create(year=year)[0]
                db_movie: MovieModel

                # controls the starting index of "line" slicing for subsequent loops
                next_idx = 2

                # movie / studio
                for col in line[next_idx:]:

                    if col.startswith(' '):
                        movie.append(col.strip())
                        next_idx += 1
                    else:
                        db_movie = MovieModel.objects.get_or_create(year=db_year, title=" ".join(movie))[0]
                        imported_movies += 1
                        db_studio = StudioModel.objects.get_or_create(name=col)[0]
                        db_studio.movies.add(db_movie)
                        next_idx += 1
                        break

                # studio / producer
                for col in line[next_idx:]:

                    if col.startswith(' '):
                        db_studio = StudioModel.objects.get_or_create(name=col)[0]
                        db_studio.movies.add(db_movie)
                        next_idx += 1
                    else:
                        # TODO: this if/else can be brought to a function (DRY)
                        if " and" in col:
                            for prod in col.split(" and"):
                                prod = prod.strip()
                                if prod:
                                    db_producer = ProducerModel.objects.get_or_create(name=prod)[0]
                                    db_producer.movies.add(db_movie)
                        elif " and " in col:
                            for prod in col.split(" and "):
                                prod = prod.strip()
                                if prod:
                                    db_producer = ProducerModel.objects.get_or_create(name=prod)[0]
                                    db_producer.movies.add(db_movie)
                        else:
                            db_producer = ProducerModel.objects.get_or_create(name=col.strip())[0]
                            db_producer.movies.add(db_movie)
                        next_idx += 1
                        break

                # producer / winner
                for col in line[next_idx:]:

                    if col.startswith(' '):
                        # TODO: this if/else can be brought to a function (DRY)
                        if " and" in col:
                            for prod in col.split(" and"):
                                prod = prod.strip()
                                if prod:
                                    db_producer = ProducerModel.objects.get_or_create(name=prod)[0]
                                    db_producer.movies.add(db_movie)
                        elif " and " in col:
                            for prod in col.split(" and "):
                                prod = prod.strip()
                                if prod:
                                    db_producer = ProducerModel.objects.get_or_create(name=prod)[0]
                                    db_producer.movies.add(db_movie)
                        else:
                            db_producer = ProducerModel.objects.get_or_create(name=col.strip())[0]
                            db_producer.movies.add(db_movie)
                    else:
                        winner = True
                        break

                db_movie.winner = winner
                db_movie.save()

        self.stdout.write(self.style.SUCCESS(f"{imported_movies} movies imported!"))
