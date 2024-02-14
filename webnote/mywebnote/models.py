from django.db import models


# Create your models here.

# class Users(models.Model):  # создало таблицу mywebnote_users
#     nickname = models.CharField(max_length=50, help_text="Введите ник:")
#     password = models.TextField(blank=True, null=True, help_text="Введите пароль:")

class FeedbackDB(models.Model):
    nickname = models.CharField(max_length=50, help_text="ник")
    text = models.TextField(help_text="отзыв")
    # из директории, где runserver
    #> python manage.py makemigrations
    #> python manage.py migrate
    # создало таблицу mywebnote_feedbackdb

