from django.db import models


class Category(models.Model):
    """ Категории """

    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """ Актеры и режиссеры """
    name = models.CharField("Имя", max_length=150)
    age = models.PositiveSmallIntegerField("Описание")
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер и режиссер"
        verbose_name_plural = "Актеры и режиссеры"
