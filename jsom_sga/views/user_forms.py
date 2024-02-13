from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from jsom_sga.forms import RegisterForm, RegisterUpdateForm, AlunoUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from jsom_sga.models import UserProfile

@user_passes_test(lambda u: u.is_staff, login_url='JSOM_SGA:login')
def register(request):
    form = RegisterForm()
    register = "active bg-gradient-primary_jsom"

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Agora que o usuário está salvo, é criado um UserProfile associado com valores padrão
            user_profile = UserProfile(user=user, peso=None, altura=None, data_nascimento=None)
            user_profile.save()         

            return redirect('JSOM_SGA:login')

    return render(
        request,
        'JSOM_SGA/register.html',
        {
            'form': form,
            'site_title': "Cadastrando novo Aluno",
            'register': register,
        }
    )

@user_passes_test(lambda u: u.is_staff, login_url='JSOM_SGA:login')
def user_update(request):
    user = request.user
    user_profile = user.userprofile  # Acesso ao UserProfile associado
    user_update = "active bg-gradient-primary_jsom"

    form = RegisterUpdateForm(instance=user, initial={
        'peso': user_profile.peso,
        'altura': user_profile.altura,
        'data_nascimento': user_profile.data_nascimento,
    })

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=user)

        if form.is_valid():
            form.save()
            # Atualize também o UserProfile
            user_profile.peso = form.cleaned_data['peso']
            user_profile.altura = form.cleaned_data['altura']
            user_profile.data_nascimento = form.cleaned_data['data_nascimento']
            user_profile.save()

            return redirect('JSOM_SGA:login')

    return render(
        request,
        'JSOM_SGA/user_update.html',
        {
            'form': form,
            'site_title': "Update Admin",
            'user_update': user_update,
        }
    )

@user_passes_test(lambda u: not u.is_staff, login_url='JSOM_SGA:login')
def aluno_update(request):
    user = request.user
    user_profile = user.userprofile  # Acesso ao UserProfile associado

    form = AlunoUpdateForm(instance=user, initial={
        'peso': user_profile.peso,
        'altura': user_profile.altura,
        'data_nascimento': user_profile.data_nascimento,
    })

    if request.method == 'POST':
        form = AlunoUpdateForm(data=request.POST, instance=user)

        if form.is_valid():
            form.save()
            # Atualize também o UserProfile
            user_profile.peso = form.cleaned_data['peso']
            user_profile.altura = form.cleaned_data['altura']
            user_profile.data_nascimento = form.cleaned_data['data_nascimento']
            user_profile.save()

            return redirect('JSOM_SGA:perfil_aluno', user_id=user.id)

    return render(
        request,
        'JSOM_SGA/aluno_update.html',
        {
            'form': form,
            'site_title': "Atualizando dados do Aluno"
        }
    )

class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control mb-2 text-white'})
        self.fields['password'].widget.attrs.update({'class': 'form-control mb-2 text-white'})

def login_view(request):
    form = BootstrapAuthenticationForm(request)

    if request.method == 'POST':
        form = BootstrapAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('JSOM_SGA:index')
    
    return render(
        request,
        'JSOM_SGA/login.html',
        {
            'form': form,
            'site_title': "Login User",
        }
    )

@login_required(login_url='JSOM_SGA:login')
def logout_view(request):
    auth.logout(request)
    return redirect('JSOM_SGA:login')