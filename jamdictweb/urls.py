"""jamdictweb URL Configuration

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

from django.urls import path
from jamdictapp import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('api/version', views.version),
    path('api/parse/doc/', views.parse_doc, name='japi_parse_doc'),
    path('api/parse/doc/<str:text>/', views.parse_doc, name='japi_parse_doc'),
    path('api/jamdict/search/', views.jamdict_search, name='japi_lookup'),
    path('api/jamdict/search/<str:query>/', views.jamdict_search),
    path('api/jamdict/search/<slug:strict>/<str:query>/', views.jamdict_search),
]
