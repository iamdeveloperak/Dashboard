from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.LoginViewUser.as_view(redirect_authenticated_user=True,redirect_field_name='index')),
    path('signup/', views.SignupViewUser.as_view()),
    path('logout/', views.logout_view, name="logout"),
]