from django.contrib import admin

from .models import YearModel, MovieModel, StudioModel, ProducerModel


class MovieInLine(admin.TabularInline):
    model = MovieModel
    extra = 1

@admin.register(YearModel)
class YearAdmin(admin.ModelAdmin):
    inlines = [MovieInLine, ]
    list_display = ('year', 'get_movies')
    ordering = ('year', )

    def get_movies(self, obj):
        return ", ".join([movie.title for movie in obj.movies.all()])

    get_movies.short_description = "movies"

@admin.register(MovieModel)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'winner', 'get_studios', 'get_producers')
    search_fields = ('title', )
    ordering = ('title', )

    def get_studios(self, obj):
        return ', '.join([studio.name for studio in obj.studios.all()])

    def get_producers(self, obj):
        return ', '.join([producer.name for producer in obj.producers.all()])

    get_studios.short_description = "Studios"
    get_producers.short_description = "Producers"

@admin.register(StudioModel)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_movies')
    search_fields = ('name', )
    ordering = ('name', )
    def get_movies(self, obj):
        return ", ".join([movie.title for movie in obj.movies.all()])

    get_movies.short_description = "Movies"

@admin.register(ProducerModel)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_movies')
    search_fields = ('name', )
    ordering = ('name', )
    def get_movies(self, obj):
        return ", ".join([movie.title for movie in obj.movies.all()])

    get_movies.short_description = "Movies"
