from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails, PostAPIView, PostDetails

urlpatterns = [
	path('article/', ArticleAPIView.as_view()),
	path('article/<int:id>/', ArticleDetails.as_view()),
	path('post/', PostAPIView.as_view()),
	path('post/<int:id>/', PostDetails.as_view()),
]