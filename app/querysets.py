
from app.models import ProducerModel

def get_queryset_producers_movie_winners_and_years():
    return ProducerModel.objects.prefetch_related('movies').prefetch_related('movies__year')

def get_movie_winners_by_producer(producer: ProducerModel):
    return producer.movies.filter(winner=True)

def get_min_max_intervals_of_worst_movie_winners(min_list_display: int = 2,
                                                 max_list_display: int = 2) -> dict:
    """
    Obtains list of producers of 2+ worst movies, with minimal and maximum winning intervals,
    only displaying the tail of minimal intervals and the head of maximum intervals.

    min_list_display and max_list_display, control how much of data is displayed on tail and head.

    Example of expected dataset:

    {
        'min': [
            {
                'producer': 'Joel Silver',
                'interval': 1,
                'previousWin': 1990,
                'followingWin': 1991},
            {
                'producer': 'Bo Derek',
                'interval': 6,
                'previousWin': 1984,
                'followingWin': 1990
            }
        ],
        'max': [
            {
                'producer': 'Matthew Vaughn',
                'interval': 13,
                'previousWin': 2002,
                'followingWin': 2015
            },
            {
                'producer': 'Bo Derek',
                'interval': 26,
                'previousWin': 1984,
                'followingWin': 2010
            }
        ]
    }
    """
    min_list = []
    max_list = []

    for producer in get_queryset_producers_movie_winners_and_years().order_by('movies__year'):

        winners = get_movie_winners_by_producer(producer).values_list("year__year", flat=True)
        winners_count = winners.count()

        if winners_count == 2:
            # max and min cases are treated the same, since there are only two winners

            winner_years = list(winners)
            case = {
                "producer": producer.name,
                "interval": winner_years[-1] - winner_years[0],
                "previousWin": winner_years[0],
                "followingWin": winner_years[-1]
            }

            if case not in max_list:
                max_list.append(case)

            if case not in min_list:
                min_list.append(case)

        elif winners_count > 2:
            winner_years = list(winners)
            case = {
                "producer": producer.name,
                "interval": winner_years[-1] - winner_years[0],
                "previousWin": winner_years[0],
                "followingWin": winner_years[-1]
            }
            if case not in max_list:
                max_list.append(case)

            # for comparisons with lesser intervals, being updated when a lesser one is detected
            last_min_interval = case["interval"]

            # find min
            idx_a, idx_b = 0, 1
            while idx_b < winners_count:

                min_case = {
                    "producer": producer.name,
                    "interval": None,
                    "previousWin": None,
                    "followingWin": None
                }

                interval = winner_years[idx_b] - winner_years[idx_a]
                if interval <= last_min_interval:
                    last_min_interval = interval
                    min_case["interval"] = interval
                    min_case["previousWin"] = winner_years[idx_a]
                    min_case["followingWin"] = winner_years[idx_b]

                    if min_case not in min_list:
                        min_list.append(min_case)

                idx_a += 1
                idx_b += 1

    min_list.sort(key=lambda winner: winner["interval"])
    max_list.sort(key=lambda winner: winner["interval"])

    return {
        "min": min_list[:min_list_display],
        "max": max_list[len(max_list) - max_list_display:]
    }
