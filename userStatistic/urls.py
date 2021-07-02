from rest_framework.routers import DefaultRouter
from  rest_framework.urls import path

from .views import UserViewSet, StatisticViewSet, AuthorizationView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'statistic', StatisticViewSet, basename='statistic')

urlpatterns=[
    path('authorization/', AuthorizationView.as_view())
]

urlpatterns += router.urls
