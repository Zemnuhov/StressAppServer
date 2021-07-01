from rest_framework import serializers

from .models import User, Statistic


class UsersSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()


class StatisticSerializers(serializers.Serializer):
    dateTime = serializers.IntegerField()
    tonicAvg = serializers.IntegerField()
    peaksCount = serializers.IntegerField()
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
