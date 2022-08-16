from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import \
    UserSerializer, FachowiecRegisterSerializer,\
    KategorieSerializer, OgloszenieSerializer, FachowiecProfileSerializer,\
    MiejscowosciSerializer, MiastaSerializer, OgloszenieFilterSerializer, FachowiecUpdateBioProfileSerializer,\
    FachowiecUpdateImageProfileSerializer,RatingSerializer,FachowiecRatingSerializer, OgloszeniaUzytkownikaSerializer
from rest_framework import permissions
from .models import Fachowiec, Kategorie, Rating, Ogloszenie, Miejscowosci
from django.http import HttpResponse


# values
class AnnouncementTownsViewSet(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.values('town').distinct()
    serializer_class = MiastaSerializer


class UpdateWorkerImageViewSet(viewsets.ModelViewSet):
    queryset = Fachowiec.objects.all()
    serializer_class = FachowiecUpdateImageProfileSerializer

    def put(self):
        image = self.request.data['image']
        id = self.request.data['id']
        Fachowiec.objects.filter(id=id).update(image=image)


class UpdateWorkerBioViewSet(viewsets.ModelViewSet):
    queryset = Fachowiec.objects.all()
    serializer_class = FachowiecUpdateBioProfileSerializer

    def put(self):
        bio = self.request.data['bio']
        id = self.request.data['id']
        Fachowiec.objects.filter(id=id).update(bio=bio)


# Ogolny user Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class RegisterWorkerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = FachowiecRegisterSerializer
    permission_classes = [permissions.AllowAny]


class CommentFachowiecViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = FachowiecRatingSerializer

    def get_queryset(self):
        username = self.request.GET.get('username')
        print(username)
        user = User.objects.get(username=username)
        worker = user.fachowiec
        return Rating.objects.filter(user=worker.id)


# pobierz pracownika
class GetWorkerViewSet(viewsets.ModelViewSet):
    queryset = Fachowiec.objects.all()
    serializer_class = FachowiecProfileSerializer

    def get_queryset(self):
        username = self.request.GET.get('username')
        user = User.objects.get(username=username)
        return Fachowiec.objects.filter(user=user.id)


# Zaloguj uzytkownika
class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GetWorkerProfileViewSet(viewsets.ModelViewSet):
    queryset = Fachowiec.objects.all()
    serializer_class = FachowiecProfileSerializer

    @action(detail=True, methods=['POST'])
    def rate_worker(self, request, pk=None):
        if 'stars' in request.data:
            title = request.data['title']
            commentValue = request.data['commentValue']
            stars = request.data['stars']
            workerId = request.data['workerId']
            worker = Fachowiec.objects.get(id=workerId)
            user = request.user
            try:
                rating = Rating.objects.get(commentedBy=user.id, user=worker.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Już oceniałes', 'result': serializer.data}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            except:
                rating = Rating.objects.create(title=title, user=worker, stars=stars,
                                      commentValue=commentValue, commentedBy=user, commentedByusername=self.request.user)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Oceniono', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'Brak gwiazdek'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)




class GetProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = FachowiecRegisterSerializer


class KategorieViewSet(viewsets.ModelViewSet):
    queryset = Kategorie.objects.all()
    serializer_class = KategorieSerializer


class OgloszeniaUnloggedViewSet(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszenieSerializer


class OgloszeniaViewSet(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszenieSerializer

    def update(self, request, pk):
        print(self.request.user)
        ann_id = self.request.data['annId']
        title = self.request.data['title']
        category = self.request.data['category']
        phone = self.request.data['phone']
        town = self.request.data['town']
        desc = self.request.data['desc']
        Ogloszenie.objects.filter(id=ann_id).update(user=self.request.user, title=title, category=category,
                                                    phone=phone, town=town, desc=desc)

        return HttpResponse({'message': 'Zaktualizowano ogloszenie'}, status=200)


class ShowOgloszeniaViewSet(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszenieFilterSerializer

    def get_queryset(self):
        category = self.request.GET.get('category')
        town = self.request.GET.get('town')
        print('town', town, 'category: ', category)

        if type(town) == str and category != 'undefined' and category is not None:
            print('1town', type(town), town, 'category: ', type(category), category)
            return Ogloszenie.objects.filter(category=category, town=town)
        elif type(town) == str and category == 'undefined' or category is None:
            print('2town', town, 'category: ', category)
            return Ogloszenie.objects.filter(town=town)
        elif type(town) != str and category != 'undefined' and category is not None:
            print('3town', town, 'category: ', category)
            return Ogloszenie.objects.filter(category=category)



class OgloszeniaUzytkownikaViewSet(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszeniaUzytkownikaSerializer

    def get_queryset(self):
        return Ogloszenie.objects.filter(user_id=self.request.user.id)


class OgloszeniaUzytkownikaUpdateViewSet(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszeniaUzytkownikaSerializer


class OstatnieOgloszeniaViewSet(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.all().order_by('-id')[:2]
    serializer_class = OgloszenieSerializer


# worker update

class FachowiecViewSet(viewsets.ModelViewSet):
    queryset = Fachowiec.objects.all()
    serializer_class = FachowiecProfileSerializer


class MiejscowosciViewSet(viewsets.ModelViewSet):
    queryset = Miejscowosci.objects.all()
    serializer_class = MiejscowosciSerializer
