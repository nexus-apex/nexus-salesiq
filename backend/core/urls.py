from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('visitors/', views.visitor_list, name='visitor_list'),
    path('visitors/create/', views.visitor_create, name='visitor_create'),
    path('visitors/<int:pk>/edit/', views.visitor_edit, name='visitor_edit'),
    path('visitors/<int:pk>/delete/', views.visitor_delete, name='visitor_delete'),
    path('conversations/', views.conversation_list, name='conversation_list'),
    path('conversations/create/', views.conversation_create, name='conversation_create'),
    path('conversations/<int:pk>/edit/', views.conversation_edit, name='conversation_edit'),
    path('conversations/<int:pk>/delete/', views.conversation_delete, name='conversation_delete'),
    path('cannedresponses/', views.cannedresponse_list, name='cannedresponse_list'),
    path('cannedresponses/create/', views.cannedresponse_create, name='cannedresponse_create'),
    path('cannedresponses/<int:pk>/edit/', views.cannedresponse_edit, name='cannedresponse_edit'),
    path('cannedresponses/<int:pk>/delete/', views.cannedresponse_delete, name='cannedresponse_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
