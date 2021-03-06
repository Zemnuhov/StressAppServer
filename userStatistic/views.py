from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import User, Statistic
from .serializers import UsersSerializer, StatisticSerializers

from django.shortcuts import get_object_or_404

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

class StatisticViewSet(viewsets.ModelViewSet):
    serializer_class = StatisticSerializers
    queryset = Statistic.objects.all()

class AuthorizationView(ListModelMixin, GenericAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        data = request.data
        try:
            authorization = get_object_or_404(User.objects.all(),
                                              login=data['login'],
                                              password=data['pass'])
            serializers = UsersSerializer(authorization)
            print(Response({'auth_user:': serializers.data}))
            return Response(serializers.data)
        except:
            return Response({False})

