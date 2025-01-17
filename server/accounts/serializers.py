
from .models import Account

from rest_framework import serializers


class APIKeySerializer(serializers.Serializer):
    name = serializers.CharField(write_only=True)
    key = serializers.CharField(read_only=True)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('id','email','password','first_name','last_name','filiation','is_administrator')
        extra_kwargs={'password':{'write_only':True},'id':{'read_only':True},'is_administrator':{'read_only':True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

class EmailSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)