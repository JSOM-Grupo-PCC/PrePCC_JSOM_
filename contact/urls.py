from django.urls import path
from contact import views
app_name = 'contact'

urlpatterns = [
    
    # user (CRUD)
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),

    # treino (CRUD)
    path('detalhes/<int:treino_id>/', views.detalhes_treino, name='detalhes_treino'),
    path('adicionar/', views.adicionar_treino, name='adicionar_treino'),
    path('atualizar/<int:treino_id>/', views.atualizar_treino, name='atualizar_treino'),
    path('excluir/<int:treino_id>/', views.excluir_treino, name='excluir_treino'),
    
    path('', views.index, name='index'),
]
