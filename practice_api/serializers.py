from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Article, Post

class ArticleSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=100)
	author = serializers.CharField(max_length=100)
	email = serializers.CharField(max_length=100)
	date = serializers.DateTimeField()

	def create(self, validated_data):
		return Article.objects.create(validated_data)
	
	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.author = validated_data.get('author', instance.author)
		instance.email = validated_data.get('email', instance.email)
		instance.date = validated_data.get('date', instance.date)
		instance.save()
		return instance

class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'