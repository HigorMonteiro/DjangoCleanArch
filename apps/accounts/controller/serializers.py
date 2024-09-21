from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    linkedin_url = serializers.URLField()
    name = serializers.CharField()
    email = serializers.EmailField()
