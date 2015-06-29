from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from django.apps import apps

class UserSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model(settings.AUTH_USER_MODEL)
        fields = ['id', 'email', 'groups', 'is_staff']
