from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')
    class Meta:
        model = Blog
        fields = ('username','name','desc','img','created_at','slug')

    def get_username_from_author(self,blog):
        username = blog.author.username
        return username