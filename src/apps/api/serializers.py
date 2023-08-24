from rest_framework import serializers
from src.apps.account.models import User

class UserUpdateSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = [
            "id","first_name","last_name" , 
            "email", "address", "mobile",
            "is_staff", "is_superuser"
            ]
        read_only_fields = ("id", "email", "is_staff", "is_superuser")



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'address', 'mobile']



def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError('This field must be an even number.')


class TestSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    quantity = serializers.IntegerField(validators=[even_number])
    text = serializers.CharField()
    to_email = serializers.EmailField()
