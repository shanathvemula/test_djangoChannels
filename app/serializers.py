from rest_framework import serializers
from app.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_author(self, obj):
        return obj.author.username


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
