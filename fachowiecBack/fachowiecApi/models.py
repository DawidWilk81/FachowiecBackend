from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
kategorie = (
    ('Murarz', 'Murarz'),
    ('Glazurnik', 'Glazurnik'),
    ('Elektryk', 'Elektryk'),
    ('Slusarz', 'Slusarz'),
    ('Informatyk', 'Informatyk'),
    ('Pomoc domowa', 'Pomoc domowa'),
    ('Malarz', 'Malarz'),

)


def upload_avatar(instance, filname):
    return '/'.join(['avatars', str(instance.user), filname])


def upload_announcement_image(instance, filname):
    return '/'.join(['announcements', str(instance.user), filname])


class Fachowiec(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fachowiec')
    bio = models.TextField(max_length=366, default='Jestem najlepszy w swojej dziedzinie')
    image = models.ImageField(upload_to=upload_avatar, blank=True, default='default.jpg')
    is_worker = models.BooleanField(default=True)

    def no_of_ratings(self):
        rating = Rating.objects.filter(user=self)
        return len(rating)

    def avg_rating(self):
        sum = 0

        ratings = Rating.objects.filter(user=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.user.username


class Rating(models.Model):
    title = models.CharField(max_length=128, default='Najlepszy fachowiec')
    # skomentowany uzytkownik
    user = models.ForeignKey(Fachowiec, on_delete=models.CASCADE, related_name='userCommented')
    stars = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    commentValue = models.TextField(max_length=254, default='Polecam')
    # komentujacy uzytkownik
    commentedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentedBy')
    commentedByusername = models.CharField(max_length=64, default='Anonymous', blank=True, null=True)

    def __str__(self):
        return self.commentedByusername


# Modele ogloszenia
class Kategorie(models.Model):
    nazwa = models.CharField(max_length=64)

    def __str__(self):
        return self.nazwa


class Ogloszenie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userAnnouncement')
    title = models.CharField(max_length=254)
    desc = models.TextField(default='brak')
    category = models.TextField(max_length=124, default='brak')
    phone = models.IntegerField()
    town = models.TextField(max_length=64)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to=upload_announcement_image, blank=True, default='default.jpg')

    def __str__(self):
        return self.title


class Miejscowosci(models.Model):
    town = models.CharField(max_length=254)

    def __str__(self):
        return self.town