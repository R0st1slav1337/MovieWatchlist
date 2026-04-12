from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Game(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    genre = models.CharField(max_length=100, blank=True)
    release_date = models.DateField(null = True, blank=True)
    image = models.URLField(blank=True)

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

    # User can only add game to one status list
    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    # Only one review per game from user
    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} review on {self.game.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank = True)
    avatar = models.URLField(blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
