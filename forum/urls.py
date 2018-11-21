"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from forum.views import User, Question, Topic, Answer, Comment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', User.register),
    path('login/', User.login),
    path('question/', Question.add),
    path('topic/', Topic.add),
    path('topics/', Topic.topics),
    path('answer/', Answer.add),
    path('comment/', Comment.add),
    path('questions/', Question.questions)
]
