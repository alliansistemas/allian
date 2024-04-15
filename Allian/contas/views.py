from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import generic

class Registro(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'
