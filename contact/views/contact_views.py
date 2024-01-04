from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contact.models import Treino
from contact.forms import TreinoForm


@login_required(login_url='contact:login')
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

@login_required(login_url='contact:login')
def detalhes_treino(request, treino_id):
    treino = get_object_or_404(Treino, pk=treino_id, owner=request.user)
    site_title = f'{treino.nome}_{treino.categoria}'
    context = {
        'site_title': site_title,
        'treino': treino
    }
    return render(request, 'contact/detalhes_treino.html', context)

@login_required(login_url='contact:login')
def adicionar_treino(request):
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.owner = request.user
            treino.save()
            return redirect('contact:index')
    else:
        form = TreinoForm()
    site_title = "Adicionando novo treino"
    context = {
        'site_title': site_title,
        'form': form
    }
    return render(request, 'contact/adicionar_treino.html', context)

@login_required(login_url='contact:login')
def atualizar_treino(request, treino_id):
    treino = get_object_or_404(Treino, pk=treino_id, owner=request.user)
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('contact:index')
    else:
        form = TreinoForm(instance=treino)
    
    site_title = f'Editando {treino.nome}'
    context = {
        'site_title': site_title,
        'treino': treino,
        'form': form,
    }
    return render(request, 'contact/atualizar_treino.html', context,)

@login_required(login_url='contact:login')
def excluir_treino(request, treino_id):
    treino = get_object_or_404(Treino, pk=treino_id, owner=request.user)
    treino.delete()
    return redirect('contact:index')