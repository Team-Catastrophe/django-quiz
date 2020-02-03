from django.conf.urls import url
from django.urls import path, include
from .views import PostListView,PostDetailView


urlpatterns = [         
            path('list/', PostListView, name='list'),
            path('detail/<int:pk>/', PostDetailView, name='detail'),
]