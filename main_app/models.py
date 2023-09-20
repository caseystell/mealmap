from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


MEALS = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
)


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(max_length=250)

    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})


class Calendar(models.Model):
    date = models.DateField('Date')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.date} ({self.id})'


class Meal(models.Model):
    date = models.DateField('Date')
    meal = models.CharField(
        max_length=9,
        choices=MEALS,
        default=[0][0]
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']