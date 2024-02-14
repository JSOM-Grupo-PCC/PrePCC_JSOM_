from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from jsom_sga.models import UserProfile, Treino
from django.utils import timezone
from django.contrib.auth.models import User
from jsom_sga.forms import TreinoForm, RegisterUpdateForm

@user_passes_test(lambda u: u.is_staff, login_url='USER:login')
def admin_aluno_update(request, user_id):
    aluno = get_object_or_404(User, id=user_id)  # Obtendo diretamente o usuário
    user_profile = aluno.userprofile  # Acesso ao UserProfile associado
    site_title = f"Atualizando dados do aluno {aluno.username}"

    form = RegisterUpdateForm(instance=aluno, initial={
        'peso': user_profile.peso,
        'altura': user_profile.altura,
        'data_nascimento': user_profile.data_nascimento,
    })

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=aluno)

        if form.is_valid():
            form.save()
            # Atualize também o UserProfile
            user_profile.peso = form.cleaned_data['peso']
            user_profile.altura = form.cleaned_data['altura']
            user_profile.data_nascimento = form.cleaned_data['data_nascimento']
            user_profile.save()

            return redirect('JSOM_SGA:perfil_aluno_admin', user_id=user_id)

    return render(
        request,
        'USER/aluno_update.html',
        {
            'form': form,
            'site_title': site_title,
        }
    )

@user_passes_test(lambda u: u.is_staff, login_url='JSOM_SGA:index')
def adicionar_treino_admin(request, user_id):
    aluno = get_object_or_404(User, id=user_id)  # Obtendo diretamente o usuário
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.owner = aluno  # Associando o treino ao usuário do perfil do aluno
            treino.save()
            return redirect('JSOM_SGA:perfil_aluno_admin', user_id=user_id)
    else:
        form = TreinoForm()
    
    site_title = f"Adicionando novo treino para {aluno.username}"
    context = {
        'site_title': site_title,
        'form': form
    }
    return render(request, 'CRUD_treino/adicionar_treino.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='JSOM_SGA:index')
def atualizar_treino_admin(request, treino_id, user_id):
    treino = get_object_or_404(Treino, pk=treino_id)
    
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('JSOM_SGA:perfil_aluno_admin', user_id=user_id)
    else:   
        form = TreinoForm(instance=treino)
    
    site_title = f'Editando treino {treino.nome}'
    context = {
        'site_title': site_title,
        'treino': treino,
        'form': form,
    }
    return render(request, 'CRUD_treino/atualizar_treino.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='JSOM_SGA:index')
def excluir_treino_admin(request, treino_id, user_id):
    treino = get_object_or_404(Treino, pk=treino_id)
    treino.delete()
    return redirect('JSOM_SGA:perfil_aluno_admin', user_id=user_id)

@user_passes_test(lambda u: u.is_staff, login_url='JSOM_SGA:index')
def lista_alunos(request):
    site_title = "Lista de Alunos"
    lista_alunos = "active bg-gradient-primary_jsom"
    users = UserProfile.objects.select_related('user').prefetch_related('user__treino_set')

    context = {
        'users': users,
        'site_title': site_title,
        'lista_alunos': lista_alunos,
    }

    return render(request, 'JSOM_SGA/lista_alunos.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='JSOM_SGA:index')
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

    return render(request, 'USER/perfil_aluno.html', context)

