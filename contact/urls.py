from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    
    # user 
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
    path('aluno/perfil/<int:user_id>/', views.perfil_aluno, name='perfil_aluno'),

    # treino (CRUD)
    path('detalhes/<int:treino_id>/', views.detalhes_treino, name='detalhes_treino'),
    # treino_admin (CRUD)
    path('admin/adicionar/<int:user_id>/', views.adicionar_treino_admin, name='adicionar_treino_admin'), # Só admin pode adcionar treinos para os alunos 
    path('admin/atualizar/<int:treino_id>/', views.atualizar_treino_admin, name='atualizar_treino_admin'),# Só admin pode atulaizar treinos para os alunos
    path('admin/excluir/<int:treino_id>/', views.excluir_treino_admin, name='excluir_treino_admin'),# Só admin pode excluir treinos dos alunos
    
    # admin
    path('admin/lista_alunos/', views.lista_alunos, name='lista_alunos'),
    path('admin/perfil_aluno_admin/<int:user_id>/', views.perfil_aluno_admin, name='perfil_aluno_admin'),

    # index
    path('', views.index, name='index'),
]
