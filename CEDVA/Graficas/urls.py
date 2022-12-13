from django.urls import path
from Graficas import views

urlpatterns = [
    path('<int:date>/grafico',views.grafico.as_view(),name="grafico"),
    path('<int:date>/grafico2',views.totalGrafiphs.as_view(),name="grafico2"),   
]