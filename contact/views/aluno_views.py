from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from contact.models import Treino, UserProfile
from django.utils import timezone

@login_required(login_url='contact:login')
@user_passes_test(lambda u: not u.is_staff, login_url='contact:lista_alunos')
def index(request):
    user = request.user
    categorias = Treino.CATEGORIA_CHOICES
    treinos = Treino.objects.filter(owner=request.user)
    site_title = f'Treinos de {user}'
    context = {
        'site_title': site_title,
        'treinos': treinos,
        'categorias': categorias,
    }
    return render(
        request,
        'contact/index.html',
        context
    )

@login_required(login_url='contact:index')
def detalhes_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    site_title = f'{treino.nome}_{treino.categoria}'
    context = {
        'site_title': site_title,
        'treino': treino
    }
    return render(request, 'contact/detalhes_treino.html', context)

@login_required(login_url='contact:index')
def perfil_aluno(request, user_id):
    aluno = get_object_or_404(UserProfile, user__id=user_id)
    site_title = f"Perfil do aluno {aluno.user.username}"

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
    }

    return render(request, 'contact/perfil_aluno.html', context)

