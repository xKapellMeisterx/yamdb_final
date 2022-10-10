from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import Truncator


MAX_LENGTH_SHORT = 50
MAX_LENGTH_MED = 150
MAX_LENGTH_LONG = 254
MAX_LEN_TEXT = 3


class User(AbstractUser):
    ROLES_CHOICES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]

    username = models.CharField(
        'Username', max_length=MAX_LENGTH_MED, unique=True
    )
    email = models.EmailField(
        'Email',
        max_length=MAX_LENGTH_LONG,
        help_text='Specify your email.',
        unique=True,
    )
    role = models.CharField(
        'Roles', choices=ROLES_CHOICES, default='user', max_length=14
    )
    bio = models.TextField(
        'Biography', blank=True, null=True, help_text='Short bio here.'
    )
    access_code = models.CharField(
        max_length=8, default=None, blank=True, null=True
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin'


class Category(models.Model):
    name = models.CharField('Category', max_length=MAX_LENGTH_SHORT)
    slug = models.SlugField('Slug', max_length=MAX_LENGTH_SHORT)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Genre', max_length=MAX_LENGTH_SHORT)
    slug = models.SlugField('Slug', max_length=MAX_LENGTH_SHORT)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Title', max_length=MAX_LENGTH_MED)
    year = models.PositiveSmallIntegerField('Year of release')
    description = models.CharField(
        'Description', blank=True, max_length=MAX_LENGTH_LONG
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='titles_category',
    )
    genre = models.ManyToManyField(Genre, blank=True)

    class Meta:
        ordering = ('year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='reviews',
    )
    text = models.TextField('Review', help_text='Write your review here.')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews_authors'
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Оценка'
    )
    pub_date = models.DateTimeField('Date of publishing', auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique_review'
            )
        ]

    def __str__(self):
        return Truncator(self.text).words(MAX_LEN_TEXT)


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField('Comment', help_text='Write your comment here.')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments_authors'
    )
    pub_date = models.DateTimeField('Date of publishing', auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return Truncator(self.text).words(MAX_LEN_TEXT)
