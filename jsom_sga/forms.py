from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Treino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'categoria', 'descricao', 'imagem']


    nome = forms.CharField(
        min_length=2,
        required=True,
        help_text='*',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        ),
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    categoria = forms.ChoiceField(
        required=True,
        help_text='*',
        widget=forms.Select(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        ),
        choices=Treino.CATEGORIA_CHOICES  # Acesse as opções diretamente da instância do modelo
    )

    descricao = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        ),
    )

    imagem = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2',
                'accept': 'image/*',
            }
        ),
    )

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'peso', 'altura', 'data_nascimento', 
            'email', 'username', 'password1', 'password2',
        ]


    first_name = forms.CharField(
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    last_name = forms.CharField( 
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    peso = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    altura = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    data_nascimento = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2',
                'type': 'date', 
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    password1 = forms.CharField(
        label="Senha",  
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-4'
            }
        )
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='*',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        ),
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='*', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    peso = forms.FloatField(
        required=True,
        help_text='*',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    altura = forms.FloatField(
        required=True,
        help_text='*',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    data_nascimento = forms.DateField(
        required=True,
        help_text='*',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2',
                'type': 'date',  # Adicionado para suporte a data
            }
        )
    )
    username = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='*', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )
    email = forms.CharField(
        required=True,
        help_text='*', 
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        )
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'form-control border-1 border-jsom shadow-big mb-2'
            }
        ),
        required=False,
    )

    password2 = forms.CharField(
        label="Confirme a Senha",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'form-control border-1 border-jsom shadow-big mb-4'
            }
        ),
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'peso', 'altura', 'data_nascimento',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1