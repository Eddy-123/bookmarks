from django.urls import path
from .views import ProfileListCreateView


urlpatterns = [
    path("profiles/", ProfileListCreateView.as_view(), name="profile-list-create")
]
