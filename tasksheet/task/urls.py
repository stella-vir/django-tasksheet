from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>/', views.detail, name='detail'),
    path('<int:room_id>/rate/', views.rate, name='rate'),
    path('<int:room_id>/results/', views.results, name='results'),

]
