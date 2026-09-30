from rest_framework import serializers


class UserSerializer(serializers.Serializer):
        username=serializers.CharField()
        email=serializers.EmailField()
        password=serializers.CharField()

class TurfSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    location=serializers.CharField()
    phone_no=serializers.IntegerField()
    fee=serializers.IntegerField()

    def validate(self,validated_data):
        fee=validated_data.get("fee")
        if fee<250:
            raise serializers.ValidationError("invalid fee.fee should be>250")
        return validated_data

