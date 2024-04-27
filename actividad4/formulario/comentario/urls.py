from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comment/<int:texto_id>/', views.add_comment, name='add_comment'),
    path('view_comments/<int:texto_id>/', views.view_comments, name='view_comments'),
    path('add_comment_with_texto/<int:texto_id>/', views.add_comment_with_texto, name='add_comment_with_texto'),
]
