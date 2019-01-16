from django.urls import path
from . import views as user_view
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='webstarsapp/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='webstarsapp/logout.html'), name='logout'),
    path('signup/', user_view.signup, name='signup'),
    path('profile/', user_view.profile, name='profile'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)