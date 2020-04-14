from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'langapp'
urlpatterns = [
    path('', auth_views.LoginView.as_view(),
         name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(success_url='/langapp/password_change_done'), name='change-password'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(), name='forgot_password'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='change_password'),
    # path('password_reset_emai/', auth_views.PasswordResetView.as_view(), name='password_reset_confirm'),
    path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('home', views.index, name='home'),
    path('blog', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('contact', views.contact, name='contact'),
    path('course', views.course, name='course'),
    path('courses', views.courses, name='courses'),
    path('instructors', views.instructors, name='instructors'),
    path('regular', views.regular, name='regular'),
]