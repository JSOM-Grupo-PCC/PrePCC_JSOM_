from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import UserProfile, Treino
from django.utils import timezone
from django.contrib.auth.models import User
from contact.forms import TreinoForm

@user_passes_test(lambda u: u.is_staff, login_url='contact:index')
def adicionar_treino_admin(request, user_id):
    aluno = get_object_or_404(User, id=user_id)  # Obtendo diretamente o usuário
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.owner = aluno  # Associando o treino ao usuário do perfil do aluno
            treino.save()
            return redirect('contact:perfil_aluno', user_id=user_id)
    else:
        form = TreinoForm()
    
    site_title = f"Adicionando novo treino para {aluno.username}"
    context = {
        'site_title': site_title,
        'form': form
    }
    return render(request, 'contact/adicionar_treino.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='contact:index')
def atualizar_treino_admin(request, treino_id):
    treino = get_object_or_404(Treino, pk=treino_id)
    
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('contact:index')
    else:
        form = TreinoForm(instance=treino)
    
    site_title = f'Editando treino {treino.nome}'
    context = {
        'site_title': site_title,
        'treino': treino,
        'form': form,
    }
    return render(request, 'contact/atualizar_treino.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='contact:index')
def excluir_treino_admin(request, treino_id):
    treino = get_object_or_404(Treino, pk=treino_id)
    treino.delete()
    return redirect('contact:index')

@user_passes_test(lambda u: u.is_staff, login_url='contact:index')
def lista_alunos(request):
    site_title = "Lista de Alunos"
    users = UserProfile.objects.select_related('user').prefetch_related('user__treino_set')

    context = {
        'users': users,
        'site_title': site_title,
    }

    return render(request, 'contact/lista_alunos.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='contact:index')
def perfil_aluno_admin(request, user_id):
    aluno = get_object_or_404(UserProfile, user__id=user_id)
    site_title = f"Perfil do aluno {aluno.user.username}"
    categorias = Treino.CATEGORIA_CHOICES

    # Calcular idade a partir da data de nascimento
    if aluno.data_nascimento:
        hoje = timezone.now().date()
        idade = hoje.year - aluno.data_nascimento.year - ((hoje.month, hoje.day) < (aluno.data_nascimento.month, aluno.data_nascimento.day))
    else:
        idade = None

    treinos = Treino.objects.filter(owner=aluno.user)

    context = {
        'aluno': aluno,
        'idade': idade,
        'site_title': site_title,
        'treinos': treinos, 
        'categorias': categorias,
    }

    return render(request, 'contact/perfil_aluno.html', context)

