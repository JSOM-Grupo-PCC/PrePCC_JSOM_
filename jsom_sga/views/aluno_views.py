from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from jsom_sga.models import Treino, UserProfile
from django.utils import timezone

@login_required(login_url='USER:login')
@user_passes_test(lambda u: not u.is_staff, login_url='JSOM_SGA:lista_alunos')
def index(request):
    user = request.user
    categorias = Treino.CATEGORIA_CHOICES
    treinos = Treino.objects.filter(owner=request.user)
    site_title = f'Treinos de {user}'
    lista_treinos = "active bg-gradient-primary_jsom"
    
    context = {
        'site_title': site_title,
        'treinos': treinos,
        'categorias': categorias,
        'lista_treinos': lista_treinos,
    }
    
    return render(
        request,
        'JSOM_SGA/index.html',
        context
    )

@login_required(login_url='JSOM_SGA:index')
def detalhes_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    site_title = f'{treino.nome}_{treino.categoria}'
    context = {
        'site_title': site_title,
        'treino': treino
    }
    return render(request, 'CRUD_treino/detalhes_treino.html', context)

@login_required(login_url='JSOM_SGA:index')
def perfil_aluno(request, user_id):
    aluno = get_object_or_404(UserProfile, user__id=user_id)
    site_title = f"Perfil do aluno {aluno.user.username}"
    perfil_aluno= "active bg-gradient-primary_jsom"

    # Calcular idade a partir da data de nascimento
    if aluno.data_nascimento:
        hoje = timezone.now().date()
        idade = hoje.year - aluno.data_nascimento.year - ((hoje.month, hoje.day) < (aluno.data_nascimento.month, aluno.data_nascimento.day))
    else:
        idade = None

    context = {
        'aluno': aluno,
        'idade': idade,
        'site_title': site_title,
        'perfil_aluno': perfil_aluno,
    }

    return render(request, 'USER/perfil_aluno.html', context)

