from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Article, Post

class ArticleSerializer(ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'

class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		#fields = ['id', 'author', 'content']
		fields = '__all__'