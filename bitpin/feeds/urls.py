from django.urls import path
from .views import FeedView, UserRateView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', FeedView, basename='list-feeds')
router.register(r'rate', UserRateView, basename='rate-feed')

urlpatterns = router.urls
