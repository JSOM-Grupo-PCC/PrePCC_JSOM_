from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.decorators import login_required
from contact.models import UserProfile

@login_required(login_url='contact:login')
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Agora que o usuário está salvo, crie o UserProfile associado
            user_profile = UserProfile(user=user)
            user_profile.peso = form.cleaned_data['peso']
            user_profile.altura = form.cleaned_data['altura']
            user_profile.data_nascimento = form.cleaned_data['data_nascimento']
            user_profile.save()

            messages.success(request, 'Usuário registrado com sucesso')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'site_title': "Register User",
        }
    )

@login_required(login_url='contact:login')
def user_update(request):
    user = request.user
    user_profile = user.userprofile  # Acesso ao UserProfile associado

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

            messages.success(request, 'Perfil atualizado com sucesso')
            return redirect('contact:login')

    return render(
        request,
        'contact/user_update.html',
        {
            'form': form,
            'site_title': "Update User"
        }
    )


class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control border-1 border-warning shadow-big mb-2'})
        self.fields['password'].widget.attrs.update({'class': 'form-control border-1 border-warning shadow-big mb-4'})

def login_view(request):
    form = BootstrapAuthenticationForm(request)

    if request.method == 'POST':
        form = BootstrapAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, f'Usuario {user.username} logado com sucesso!')
            return redirect('contact:index')
        messages.error(request, 'Login inválido')
    
    return render(
        request,
        'contact/login.html',
        {
            'form': form,
            'site_title': "Login User",
        }
    )

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')