
from django.urls import path
from blog.views import delete_reply,reply,PostListView,postDetailView,PostCreateView,PostUpdateView,postDeleteView,UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', postDetailView, name='post-detail'),
    path('post/<int:pk>/delete/', postDeleteView, name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/reply/<int:pk>/<int:v>/', reply, name='reply'),
    path('post/reply/delete/<int:pk>/<int:v>/', delete_reply, name='delete-reply'),

]
