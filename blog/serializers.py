from rest_framework import serializers
from .models import Posts, Coments

class Post_ser(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Posts
        fields= ['id', 'title', 'description', 'user', 'created_time']
