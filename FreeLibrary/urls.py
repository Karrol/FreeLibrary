"""FreeLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from FreeLibrary import settings
from books import views as books_views
from account import views as account_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('', books_views.index, name='index'),
    path('account/', include('account.urls')),

    path('signup/', account_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html',redirect_field_name='next',redirect_authenticated_user=True),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
