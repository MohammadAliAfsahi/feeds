from .models import Feed, UserRate
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = ['title', 'total_rate', 'number_of_rate']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        rsp = {
            'title': ret['title'],
            'Number of Rates': ret['number_of_rate']
        }
        try:
            user_rate = UserRate.objects.get(user=self.context['request'].user, feed=instance)
            rsp['your_rate'] = user_rate.rate
        except ObjectDoesNotExist:
            pass
        if ret['total_rate'] is None:
            rsp['rating'] = None
        else:
            rsp['rating'] = float("{:.2f}".format(ret['total_rate'] / ret['number_of_rate']))
        return rsp


class UserRateSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        try:
            return self.Meta.model.objects.create(**validated_data)
        except IntegrityError:
            instance = UserRate.objects.get(user=validated_data['user'], feed=validated_data['feed'])
            self.update(instance=instance, validated_data=validated_data)
        return instance

    class Meta:
        model = UserRate
        # If we use all fields, all users will be shown in browsable API
        # and each can rate to feed with identity of other users
        fields = ['feed', 'rate']
