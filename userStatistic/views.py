from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import User, Statistic
from .serializers import UsersSerializer, StatisticSerializers

from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

class StatisticViewSet(viewsets.ModelViewSet):
    serializer_class = StatisticSerializers
    queryset = Statistic.objects.all()