
from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('pwa.urls')),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='twitter/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('editar', views.editar, name='editar'),
    path('follow/<str:username>/', views.follow, name='follow'),
	path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
	path('hijos/', views.hijos, name='hijos'),
	path('consultas/', views.consultas, name='consultas'),
    path('consulta/<int:id>/', views.consulta, name='consulta'),
	path('vacunacion/', views.vacunacion, name='vacunacion'),
	path('interes/', views.interes, name='interes'),
	path('brotes/', views.brotes, name='brotes'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)