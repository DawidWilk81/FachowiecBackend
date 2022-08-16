
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Fachowiec, Kategorie, Ogloszenie, Miejscowosci, Rating
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view


# pobierz uzytkownika
class FachowiecProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fachowiec
        fields = ["id", "bio", "image", "is_worker", "no_of_ratings", "avg_rating"]


# skomentuj fachowca
class FachowiecRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class FachowiecUpdateBioProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fachowiec
        fields = ["id", "bio"]


class FachowiecUpdateImageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fachowiec
        fields = ["id", "image"]


# zdefiniuj profil uzytkownika
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# zdefiniuj profil uzytkownika

class FachowiecRegisterSerializer(serializers.ModelSerializer):
    fachowiec = FachowiecProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'fachowiec']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        worker = validated_data.pop('fachowiec')
        user = User.objects.create_user(**validated_data)
        user.worker = Fachowiec.objects.create(user=user, **worker)
        user.save()

        return user

    def get_queryset(self):
        user_id = self.request.user
        return User.objects.filter(pk=user_id)


class KategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategorie
        fields = ['id', 'nazwa']


class MiastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ogloszenie
        fields = ['town', 'category']


class OgloszenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ogloszenie
        fields = ['id', 'title', 'category', 'phone', 'town', 'desc', 'user', 'image']

    @api_view(["POST"])
    def post(self):
        title = self.request.data['title']
        category = self.request.data['category']
        phone = self.request.data['phone']
        town = self.request.data['town']
        desc = self.request.data['desc']
        image = self.request.data['image']

        return Ogloszenie.objects.create(user_id=self.request.user, title=title, category=category, phone=phone, town=town,
                                         desc=desc, image=image)


class OgloszeniaUzytkownikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ogloszenie
        fields = '__all__'


class OgloszenieFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ogloszenie
        fields = ['id', 'title', 'category', 'phone', 'town', 'desc', 'user', 'image']


class MiejscowosciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miejscowosci
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
