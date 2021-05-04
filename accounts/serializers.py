from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'meta', 'district', 'state', 'dob', 'gender']


class SignupSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'profile', 'password']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        profile = Profile.objects.create(user=user, **profile_data)
        return {
            'firstName': profile.firstName,
            'lastName': profile.lastName, 
            'meta': profile.meta, 
            'district': profile.district, 
            'state': profile.state, 
            'dob': profile.dob, 
            'gender': profile.gender
        }


class LoginSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        username = data.get('username')
        password = data.get('password')

    def to_representation(self, instance):
        return {
            'id' : instance.user.id,
            'firstName': instance.firstName,
            'lastName': instance.lastName, 
            'meta': instance.meta, 
            'district': instance.district, 
            'state': instance.state, 
            'dob': instance.dob, 
            'gender': instance.gender
        }

class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'meta', 'district', 'state']