from django.conf.urls import url
from . import views #同じディレクトリにあるviews.pyを呼び出し
from django.urls import path

app_name = 'app'

urlpatterns = [path('', views.Homeview.as_view(), name='index'),]