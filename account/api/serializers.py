from rest_framework import serializers
from django.conf import settings
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user"]
