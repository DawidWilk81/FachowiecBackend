from django.urls import path, include
from rest_framework import routers
from .views import RegisterUserViewSet, RegisterWorkerViewSet,\
    GetWorkerProfileViewSet, GetProfileViewSet, KategorieViewSet, AnnouncementTownsViewSet,\
    OgloszeniaViewSet, UpdateWorkerImageViewSet, ShowOgloszeniaViewSet, OstatnieOgloszeniaViewSet,\
    OgloszeniaUnloggedViewSet, OgloszeniaUzytkownikaViewSet, UpdateWorkerBioViewSet,\
    FachowiecViewSet, GetWorkerViewSet, CommentFachowiecViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

router = routers.DefaultRouter()
router.register('users', RegisterUserViewSet)
router.register('workers', RegisterWorkerViewSet)
router.register('profile', GetProfileViewSet)
router.register('workerProfile', GetWorkerProfileViewSet)
router.register('workerGet', GetWorkerViewSet)
router.register('categoryList', KategorieViewSet)
router.register('comments', CommentFachowiecViewSet)
router.register('announcements', OgloszeniaViewSet)
router.register('announcementsShow', OgloszeniaUnloggedViewSet)
router.register('allAnnouncements', ShowOgloszeniaViewSet)
router.register('lastAnnouncements', OstatnieOgloszeniaViewSet)
router.register('town', AnnouncementTownsViewSet)
router.register('updateAvatar', UpdateWorkerImageViewSet)
router.register('updateBio', UpdateWorkerBioViewSet)
router.register('fachowiec', FachowiecViewSet)
router.register('userPosts', OgloszeniaUzytkownikaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
