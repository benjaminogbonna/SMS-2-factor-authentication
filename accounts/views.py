from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from verify.forms import CodeForm
from verify.models import CustomUser
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy

from .utils import send_sms

# Create your views here.


# @login_required()
def index(request):
    context = {}
    return render(request, 'accounts/main.html', {})


@login_required()
def home(request):
    context = {}
    return render(request, 'accounts/user.html', {})


def auth_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('accounts:verify')

    return render(request, 'accounts/auth.html', {'form': form})


def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f'{user.username}: {user.code}'
        if not request.POST:
            # send sms
            # send_sms(code_user, user.phone_num)
            print(code_user)
        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('accounts:home')
            else:
                return redirect('accounts:login')
    return render(request, 'accounts/verify.html', {'form': form})


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/signup.html'
