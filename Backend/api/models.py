from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField(null = True)

    def __str__(self):
        return self.title


class Library(models.Model):
    STATUS_CHOICES = [
        ('played', 'Played'),
        ('playing', 'Playing'),
        ('want', 'Want to play')
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} review on {self.game.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank = True)

    def __str__(self):
        return self.user.username
