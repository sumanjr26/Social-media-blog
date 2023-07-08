from rest_framework import serializers

from app.models import *
class socialmediams(serializers.ModelSerializer):
    class Meta:
        model=SocialMedia
        fields="__all__"