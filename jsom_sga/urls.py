from django.urls import path
from jsom_sga import views

app_name = 'JSOM_SGA'

urlpatterns = [
    
    # user 
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),

    # Aluno
    path('aluno/update/', views.aluno_update, name='aluno_update'),

    path('aluno/perfil/<int:user_id>/', views.perfil_aluno, name='perfil_aluno'),

    # treino (CRUD)
    path('detalhes/<int:treino_id>/', views.detalhes_treino, name='detalhes_treino'),
    # treino_admin (CRUD)
    path('admin/adicionar/<int:user_id>/', views.adicionar_treino_admin, name='adicionar_treino_admin'),
    path('admin/atualizar/<int:user_id>/<int:treino_id>/', views.atualizar_treino_admin, name='atualizar_treino_admin'),
    path('admin/excluir/<int:user_id>/<int:treino_id>/', views.excluir_treino_admin, name='excluir_treino_admin'),
    path('admin/aluno/update/<int:user_id>/', views.admin_aluno_update, name='admin_aluno_update'),
    
    # admin
    path('admin/lista_alunos/', views.lista_alunos, name='lista_alunos'),
    path('admin/perfil_aluno_admin/<int:user_id>/', views.perfil_aluno_admin, name='perfil_aluno_admin'),

    # index
    path('', views.index, name='index'),
]
