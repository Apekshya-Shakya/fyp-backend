from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('event', EventDetail)
router.register('member', MemberDetail)
router.register('introduction', IntroductionDetail)
router.register('messagefrompresidentandgeneralsecretary',MessagefromPresidentandGeneralSecretaryDetail)
router.register('activities', ActivitiesDetail)
router.register('news', NewsDetail)
router.register('imagemedia', ImageMediaDetail)
router.register('videomedia', VideoMediaDetail)
router.register('contactus', ContactUsDetail)


urlpatterns = [
    path('', include(router.urls)),
]
