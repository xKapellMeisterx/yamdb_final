from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User

EMPTY_VALUE = '-пусто-'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'bio', 'role')
    search_fields = ('username',)
    list_filter = ('role',)
    empty_value_display = EMPTY_VALUE


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'year', 'description')
    search_fields = ('name',)
    list_filter = ('year', 'category', 'genre')
    empty_value_display = EMPTY_VALUE


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'score', 'pub_date', 'title')
    search_fields = ('text',)
    list_filter = ('author', 'score')
    empty_value_display = EMPTY_VALUE


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'pub_date', 'review')
    search_fields = ('text',)
    list_filter = ('review', 'author')
    empty_value_display = EMPTY_VALUE
