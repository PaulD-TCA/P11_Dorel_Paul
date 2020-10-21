"""purbeurre_plateforme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('search_and_sub/', include('search_and_sub.urls')),
    path('user/', include('user.urls')),
    path('basics_screens/', include('basics_screens.urls')),
    path('', include('search_and_sub.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns = [
#     path('purbeurre_plateforme.search_and_sub/', include('purbeurre_plateforme.search_and_sub.urls')),
#     path('purbeurre_plateforme.user/', include('purbeurre_plateforme.user.urls')),
#     path('purbeurre_plateforme.basics_screens/', include('purbeurre_plateforme.basics_screens.urls')),
#     path('', include('purbeurre_plateforme.search_and_sub.urls')),
#     path('admin/', admin.site.urls),
# ]
