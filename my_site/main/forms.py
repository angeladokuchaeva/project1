from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from main.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
