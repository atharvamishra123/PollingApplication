"""EVCFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from polls.views import all_polls
from user.views import add_polls, user_registration, user_login, user_logout, show_profile
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^allpolls/(?P<id>[0-9]*)', all_polls, name="allpolls"),

    path('signup/', user_registration, name="sign_up"),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add/', add_polls, name="add"),
    path('profile/', show_profile, name="profile")

]
