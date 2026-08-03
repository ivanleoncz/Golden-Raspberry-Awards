from django.contrib import admin

from .models import YearModel, MovieModel, StudioModel, ProducerModel

admin.site.register(YearModel)
admin.site.register(MovieModel)
admin.site.register(StudioModel)
admin.site.register(ProducerModel)
