from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login/',views.LoginPage.as_view(),name='login'),
    path('register/',views.RegisterPage.as_view(),name='register'),
    path('logout/',views.LogoutView.as_view(),name='logout')

]
