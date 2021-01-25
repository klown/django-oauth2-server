from django.shortcuts import render

# new2
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# oauth2 (II)
from oauth2_provider.views.generic import ProtectedResourceView
#from django.http import HttpResponse
from django import http     # for oauth2 (II) and (III); covers two uses of HttpReponse

# oauth2 (III)
from django.contrib.auth.decorators import login_required
# from django.http.response import HttpResponse

# new2
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# oauth2 (II)
class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return http.HttpResponse('Hello, OAuth2!')

# oauth2 (III)
@login_required()
def secret_page(request, *args, **kwargs):
    return http.response.HttpResponse('Secret contents!', status=200)
