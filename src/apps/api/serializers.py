from rest_framework import serializers
from src.apps.account.models import User

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "address", "mobile"]

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'address', 'mobile']

