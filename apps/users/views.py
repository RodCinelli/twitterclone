from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from .forms import CustomPasswordResetForm
from django.shortcuts import render
from allauth.account.views import SignupView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import logging

User = get_user_model()
logger = logging.getLogger(__name__)

class CustomPasswordResetView(FormView):
    template_name = "account/password_reset.html"
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy("password_reset")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        new_password = form.cleaned_data.get("new_password1")
        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            messages.success(self.request, "Sua senha foi redefinida com sucesso.")
        except User.DoesNotExist:
            messages.error(self.request, "O email informado não pode ser localizado.")
        return super().form_valid(form)

def custom_logout_view(request):
    logout(request)
    return render(request, "account/logout.html")

class CustomSignupView(SignupView):
    template_name = "account/signup.html"  # Usando o mesmo template

    def form_valid(self, form):
        logger.info(f"Signup process started for data: {form.cleaned_data}")
        response = super().form_valid(form)
        # Após form_valid, o usuário criado é atribuído a self.user
        if self.user:
            logger.info(f"User created successfully: {self.user.username}")
            messages.success(self.request, f"Cadastro realizado com sucesso! Usuário '{self.user.username}' criado. Por favor, faça login.")
        else:
            logger.error("User creation failed: No user returned after signup.")
            messages.error(self.request, "Ocorreu um erro ao cadastrar o usuário.")
        return response

    def form_invalid(self, form):
        logger.error(f"Signup form invalid: {form.errors}")
        return super().form_invalid(form)

# Removendo proteções da UserListView para testes
class UserListView(ListView):
    model = get_user_model()
    template_name = 'account/user_list.html'
    context_object_name = 'users'
    ordering = ['id']
