from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('resume/create/', views.resume_create, name='resume_create'),
    path('resume/<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('resume/<int:pk>/delete/', views.resume_delete, name='resume_delete'),
    path('resume/<int:pk>/', views.resume_detail, name='resume_detail'),
    path('resume/<int:pk>/pdf/', views.resume_pdf, name='resume_pdf'),
]
