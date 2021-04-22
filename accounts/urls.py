from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name='home'),
    path('register/',views.registerView,name='register_url'),
    path('login/',LoginView.as_view(),name="login_url"),
    path('dashboard/',views.dashboardView, name='dashboard'),
    path('logout/',LogoutView.as_view(next_page="home"),name='logout'),
]
