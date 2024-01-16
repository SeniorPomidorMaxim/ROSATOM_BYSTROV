from django.urls import path
from .import views


urlpatterns = [
    path('question', views.AddQuestions.as_view(), name='question'),
    path('', views.IndexView.as_view(), name='home'),
    path('list', views.list, name='list'),
    path('get_companies/', views.GetCompanies.as_view(), name='get_companies'),
]

