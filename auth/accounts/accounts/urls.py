# new2
from django.urls import path

from .views import SignUpView, secret_page


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('secret', secret_page, name='secret'),
]