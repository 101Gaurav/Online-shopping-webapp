from django.urls import path, include
from . import views

urlpatterns = [
    path("signup", views.signup),
    path("signin", views.signin),
    path("logout", views.logout),
    path("save", views.save),
    path("profile",views.profile),

]
