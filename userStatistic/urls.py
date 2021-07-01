from rest_framework.routers import DefaultRouter

from .views import UserViewSet, StatisticViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'statistic', StatisticViewSet, basename='statistic')

urlpatterns = router.urls