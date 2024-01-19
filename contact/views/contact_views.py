from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from contact.models import Treino

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

@login_required(login_url='contact:index')
def detalhes_treino(request, treino_id):
    treino = get_object_or_404(Treino, pk=treino_id, owner=request.user)
    site_title = f'{treino.nome}_{treino.categoria}'
    context = {
        'site_title': site_title,
        'treino': treino
    }
    return render(request, 'contact/detalhes_treino.html', context)