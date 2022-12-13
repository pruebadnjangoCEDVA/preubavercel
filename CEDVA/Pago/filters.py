import django_filters
from django_filters import *
from Cedva1.models import *
from django.forms import ModelForm

class buscaFilter(django_filters.FilterSet):
	end_date = DateFilter(field_name='inicioCurso', lookup_expr='lte')
	class Meta: 
		model=Alumno
		fields=['nombreA', 'apellidoPA']

class buscaFilterDos(django_filters.FilterSet):
	class Meta: 
		model=Pago
		fields=['fechaPago', 'mesPagado']