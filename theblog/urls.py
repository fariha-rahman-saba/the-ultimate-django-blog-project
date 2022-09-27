from django.urls import path
from .views import HomeView, ArticleDetail,AddPost,UpdatePostView, Delete, AddCategory,CategoryView,CategoryListView, LikeView

urlpatterns = [
    
    path('',HomeView.as_view(), name = "home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name = 'article-detail'),
    path('add-post', AddPost.as_view(), name = 'add-post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/remove',Delete.as_view(),name='delete_post'),
    path('add-category', AddCategory.as_view(), name = 'add-category'),
    path('category/<str:cats>', CategoryView, name = 'category'),
    path('category-list/', CategoryListView, name = 'category-list'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    
]
