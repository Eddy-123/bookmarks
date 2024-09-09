from rest_framework import generics
from django.conf import settings
from django.contrib.auth import get_user_model
from account.api.serializers import ProfileSerializer
from ..models import Profile


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
