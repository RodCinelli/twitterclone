from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import CustomPasswordResetForm

User = get_user_model()

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
            # To avoid exposing whether the email exists
            messages.success(self.request, "Caso o e-mail esteja cadastrado, sua senha foi redefinida com sucesso.")
        return super().form_valid(form)
