from django.contrib.auth.forms import UserCreationForm

from main.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
