from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    
    # user (CRUD)
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
    
    path('', views.index, name='index'),
]
