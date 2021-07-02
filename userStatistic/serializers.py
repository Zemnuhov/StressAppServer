from rest_framework import serializers

from .models import User, Statistic


class UsersSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    login = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance



class StatisticSerializers(serializers.Serializer):
    dateTime = serializers.IntegerField()
    tonicAvg = serializers.IntegerField()
    peaksCount = serializers.IntegerField()
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Statistic.objects.create(**validated_data)
