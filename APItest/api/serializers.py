from rest_framework import serializers

from .models import Post, Group, Comment


class GroupCustomField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        try:
            if isinstance(data, int):
                data = Group.objects.get(pk=data)
            if isinstance(data, str):
                data = Group.objects.get(title=data)
        except ValueError:
            raise serializers.ValidationError('Такой группы не существует')
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'post', 'author')
        read_only_fields = ('id', 'post', 'author')


class PostSerializer(serializers.ModelSerializer):
    group = GroupCustomField(required=False)

    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'group', 'author', 'comments')
        read_only_fields = ('id', 'author', 'comments')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title')
        read_only_fields = ('id',)
