from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=True,
                            db_index=True)

    def __str__(self):
        return self.name
