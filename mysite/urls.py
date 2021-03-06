"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from users import views as user_views
from visualization import views as visualization_views
from linkchecker import views as linkchecker_views

urlpatterns = [
    path('', include('analysis.urls')),
    path('admin/', admin.site.urls),
    path('login/', user_views.login, name='firebase-login'),
    path('logout/', user_views.logout, name='firebase-logout'),
    path('visualization/', visualization_views.visualization, name='visualization'),
    path('linkchecker/', linkchecker_views.linkchecker, name='link-checker'),
]