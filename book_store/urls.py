"""
URL configuration for book_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from core.views import home_view
# from core.views import login_view
from core.views import register_view
from user_auth.views import login_view
from core.api.views import BookListAPIView
from core.api.dashain import dashainAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",home_view),
    path("login/",login_view),
    path("register/",register_view),
    path("api/books/",BookListAPIView.as_view()),
    path("api/dashain/",dashainAPIView.as_view())
]
