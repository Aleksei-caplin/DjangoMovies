from django.db import models
from datetime import date

from django.urls import reverse


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
    age = models.PositiveSmallIntegerField("Возраст")
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актер и режиссер"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    """ Жанры """
    name = models.CharField("Название жанра", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """ Фильмы """
    title = models.CharField("Название фильма", max_length=160)
    tagline = models.CharField("Слоган", max_length=100, default="")
    description = models.TextField("Описание")
    poster = models.ImageField("Аватар", upload_to="movie/")
    year = models.PositiveSmallIntegerField("Дата выхода", default="2021")
    country = models.CharField("Страна", max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name="Режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="film_actors")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    world_premier = models.DateField("Премьера в мире", default=date.today())
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="Указать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="Указать сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мировом прокате", default=0, help_text="Указать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_reviews(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    """ Кадры из фильма """
    title = models.CharField("Заголовок", max_length=160)
    description = models.TextField("Описание")
    image = models.ImageField("Картинка", upload_to="movie_shots")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    """ Звезда рейтинга """
    value = models.PositiveIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезда рейтинга"
        ordering = ["-value"]

class Rating(models.Model):
    """ Рейтинг """
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name="Звезда", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """ Отзывы """
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



