from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ['username', 'password1', 'password2']
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        # self.fields['email'].label = 'Email Address'
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None
