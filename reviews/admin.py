from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


class UserAdmin(admin.ModelAdmin):

    list_display = (
        "role", "bio", "email", "username", 'first_name', 'last_name')
    empty_value_display = "-пусто-"


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug')
    empty_value_display = "-пусто-"


class GenreAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug')
    empty_value_display = "-пусто-"


class TitleAdmin(admin.ModelAdmin):

    list_display = ('name', 'year', 'category')
    empty_value_display = "-пусто-"


class ReviewAdmin(admin.ModelAdmin):

    list_display = ("text", "author", "title", "score", "pub_date")
    empty_value_display = "-пусто-"


class CommentAdmin(admin.ModelAdmin):

    list_display = ("text", "author", "review", "pub_date",)
    empty_value_display = "-пусто-"


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
