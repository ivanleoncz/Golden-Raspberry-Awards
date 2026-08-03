from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class YearModel(models.Model):
    year = models.PositiveSmallIntegerField(blank=False, null=False, unique=True, validators=[MinValueValidator(1980),
                                                                                              MaxValueValidator(2026)])

    def __str__(self):
        return f"{self.year}"

    class Meta:
        verbose_name_plural = "Years"

class MovieModel(models.Model):
    year = models.ForeignKey(YearModel, blank=False, null=False, related_name="movies", on_delete=models.DO_NOTHING)
    title = models.CharField(blank=False, null=False, max_length=128)
    winner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, from {self.year}"

    class Meta:
        verbose_name_plural = "Movies"

class StudioModel(models.Model):
    movies = models.ManyToManyField(MovieModel, related_name="studios")
    name = models.CharField(blank=False, null=False, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Studios"

class ProducerModel(models.Model):
    movies = models.ManyToManyField(MovieModel, related_name="producers")
    name = models.CharField(blank=False, null=False, unique=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Producers"