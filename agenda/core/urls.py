from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='agenda/')),
    path('agenda/', views.listar_eventos, name='listar_eventos'),
    path('logout/', views.logout_user, name='logout_page'),
    path('login', views.login_user, name='login_user'),
    path('agenda/evento/', views.evento, name='evento'),
    path('agenda/evento/delete/<int:id>', views.delete_evento, name='delete_evento'),
    path('agenda/evento/submit', views.submit_evento, name='submit_evento'),
    path('cadastrar/usuario', views.cadastrar_usuario, name='novo_usuario'),
    path('vencidos', views.vencidos, name='vencidos'),

]