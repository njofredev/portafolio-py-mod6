from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Importa la vista de logout
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Agrega la URL y la vista de logout
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    # Agrega cualquier otra URL que necesites para tu aplicación
]
