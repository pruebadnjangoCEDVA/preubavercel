from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import admin
from django.urls import reverse_lazy
from Cedva1.models import *
from datetime import datetime
from django.views.generic.base import TemplateView
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin

class totalGrafiphs(LoginRequiredMixin,TemplateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    template_name="graficaTotal.html"

    def todo_get(self,**kwargs):
        data = [] 
        year =self.kwargs.get('date')

        total1=Pago.objects.filter(fechaPago__year=year,fechaPago__month='1').count()
        
        total2=Pago.objects.filter(fechaPago__year=year,fechaPago__month='2').count()

        total3=Pago.objects.filter(fechaPago__year=year,fechaPago__month='3').count()

        total4=Pago.objects.filter(fechaPago__year=year,fechaPago__month='4').count()

        total5=Pago.objects.filter(fechaPago__year=year,fechaPago__month='5').count()        
        
        total6=Pago.objects.filter(fechaPago__year=year,fechaPago__month='6').count()

        total7=Pago.objects.filter(fechaPago__year=year,fechaPago__month='7').count()

        total8=Pago.objects.filter(fechaPago__year=year,fechaPago__month='8').count()

        total9=Pago.objects.filter(fechaPago__year=year,fechaPago__month='9').count()

        total10=Pago.objects.filter(fechaPago__year=year,fechaPago__month='10').count()

        total11=Pago.objects.filter(fechaPago__year=year,fechaPago__month='11').count()

        total12=Pago.objects.filter(fechaPago__year=year,fechaPago__month='12').count() 

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]

        return data


    def todo_los_pagos(self,**kwargs):
        data = [] 
        anio = self.kwargs.get('date')
        year= anio
        total1=Pago.objects.filter(fechaPago__year=year,fechaPago__month='1').aggregate(R=Coalesce(Sum('monto'),0)).get('R')
        
        total2=Pago.objects.filter(fechaPago__year=year,fechaPago__month='2').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total3=Pago.objects.filter(fechaPago__year=year,fechaPago__month='3').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total4=Pago.objects.filter(fechaPago__year=year,fechaPago__month='4').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total5=Pago.objects.filter(fechaPago__year=year,fechaPago__month='5').aggregate(R=Coalesce(Sum('monto'),0)).get('R')
        
        total6=Pago.objects.filter(fechaPago__year=year,fechaPago__month='6').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total7=Pago.objects.filter(fechaPago__year=year,fechaPago__month='7').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total8=Pago.objects.filter(fechaPago__year=year,fechaPago__month='8').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total9=Pago.objects.filter(fechaPago__year=year,fechaPago__month='9').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total10=Pago.objects.filter(fechaPago__year=year,fechaPago__month='10').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total11=Pago.objects.filter(fechaPago__year=year,fechaPago__month='11').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total12=Pago.objects.filter(fechaPago__year=year,fechaPago__month='12').aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]
        print(data)
        return data

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = self.todo_get()
        context['todo_pagos'] = self.todo_los_pagos()
        return context


class grafico(LoginRequiredMixin,TemplateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    template_name= "grafico.html"
    
    def get_report_year_month(self,*args, **kwargs):
        data = [] 
        anio = self.kwargs.get('date')
        year= anio
       # print(request.GET)  

        total1=Pago.objects.filter(fechaPago__year=year,mesPagado='Enero',PagoRegistrado="Mensual").count()
        
        total2=Pago.objects.filter(fechaPago__year=year,mesPagado='Febrero',PagoRegistrado="Mensual").count()

        total3=Pago.objects.filter(fechaPago__year=year,mesPagado='Marzo',PagoRegistrado="Mensual").count()

        total4=Pago.objects.filter(fechaPago__year=year,mesPagado='Abril',PagoRegistrado="Mensual").count()

        total5=Pago.objects.filter(fechaPago__year=year,mesPagado='Mayo',PagoRegistrado="Mensual").count()        
        
        total6=Pago.objects.filter(fechaPago__year=year,mesPagado='Junio',PagoRegistrado="Mensual").count()

        total7=Pago.objects.filter(fechaPago__year=year,mesPagado='Julio',PagoRegistrado="Mensual").count()

        total8=Pago.objects.filter(fechaPago__year=year,mesPagado='Agosto',PagoRegistrado="Mensual").count()

        total9=Pago.objects.filter(fechaPago__year=year,mesPagado='Septiembre',PagoRegistrado="Mensual").count()

        total10=Pago.objects.filter(fechaPago__year=year,mesPagado='Octubre',PagoRegistrado="Mensual").count()

        total11=Pago.objects.filter(fechaPago__year=year,mesPagado='Noviembre',PagoRegistrado="Mensual").count()

        total12=Pago.objects.filter(fechaPago__year=year,mesPagado='Diciembre',PagoRegistrado="Mensual").count() 

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]

        return data

    def get_report_Con_Convenio(self):
        
        year=datetime.now().year 
        totalc=Alumno.objects.filter(convenio='SI',inicioCurso__year=year,activo_por_pagos=True).count()
       
       
        return totalc

    def get_report_Sin_Convenio(self):
        year=datetime.now().year 
        totala=Alumno.objects.filter(convenio='NO',inicioCurso__year=year,activo_por_pagos=True).count()
        return totala

    def get_año(self):
        year=datetime.now().year 
        return year 
    def get_añoAnterior(self):
        year=(datetime.now().year)-1 
        return year 
    def get_añoSig(self):
        year=(datetime.now().year)+1 
        return year 

    def get_alumnos_activos(self):
        alumnos=Alumno.objects.filter(activo_por_pagos=True)
        print(alumnos)
        return alumnos

    def get_tipo_de_pagos(self,*args, **kwargs):
        data = [] 
        anio = self.kwargs.get('date')
        year= anio
       
        total1=Pago.objects.filter(fechaPago__year=year,mesPagado='Enero',PagoRegistrado="Mensual", tipoPago="Efectivo").count()
        
        total2=Pago.objects.filter(fechaPago__year=year,mesPagado='Febrero',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total3=Pago.objects.filter(fechaPago__year=year,mesPagado='Marzo',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total4=Pago.objects.filter(fechaPago__year=year,mesPagado='Abril',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total5=Pago.objects.filter(fechaPago__year=year,mesPagado='Mayo',PagoRegistrado="Mensual",tipoPago="Efectivo").count()        
        
        total6=Pago.objects.filter(fechaPago__year=year,mesPagado='Junio',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total7=Pago.objects.filter(fechaPago__year=year,mesPagado='Julio',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total8=Pago.objects.filter(fechaPago__year=year,mesPagado='Agosto',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total9=Pago.objects.filter(fechaPago__year=year,mesPagado='Septiembre',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total10=Pago.objects.filter(fechaPago__year=year,mesPagado='Octubre',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total11=Pago.objects.filter(fechaPago__year=year,mesPagado='Noviembre',PagoRegistrado="Mensual",tipoPago="Efectivo").count()

        total12=Pago.objects.filter(fechaPago__year=year,mesPagado='Diciembre',PagoRegistrado="Mensual",tipoPago="Efectivo").count() 

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]
        return data

    def get_tipo_de_pagos_Tranferencia(self,*args, **kwargs):
        data = [] 
        anio = self.kwargs.get('date')
        year= anio
       
        total1=Pago.objects.filter(fechaPago__year=year,mesPagado='Enero',PagoRegistrado="Mensual", tipoPago="Transferencia").count()
        
        total2=Pago.objects.filter(fechaPago__year=year,mesPagado='Febrero',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total3=Pago.objects.filter(fechaPago__year=year,mesPagado='Marzo',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total4=Pago.objects.filter(fechaPago__year=year,mesPagado='Abril',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total5=Pago.objects.filter(fechaPago__year=year,mesPagado='Mayo',PagoRegistrado="Mensual",tipoPago="Transferencia").count()        
        
        total6=Pago.objects.filter(fechaPago__year=year,mesPagado='Junio',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total7=Pago.objects.filter(fechaPago__year=year,mesPagado='Julio',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total8=Pago.objects.filter(fechaPago__year=year,mesPagado='Agosto',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total9=Pago.objects.filter(fechaPago__year=year,mesPagado='Septiembre',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total10=Pago.objects.filter(fechaPago__year=year,mesPagado='Octubre',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total11=Pago.objects.filter(fechaPago__year=year,mesPagado='Noviembre',PagoRegistrado="Mensual",tipoPago="Transferencia").count()

        total12=Pago.objects.filter(fechaPago__year=year,mesPagado='Diciembre',PagoRegistrado="Mensual",tipoPago="Transferencia").count() 

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]
        return data

    def get_tipo_de_pagos_total(self,*args, **kwargs):
        data = [] 
        anio = self.kwargs.get('date')
        year= anio 
       
        total1=Pago.objects.filter(fechaPago__year=year,mesPagado='Enero',PagoRegistrado="Mensual",tipoPago="Depósito").count()
        
        total2=Pago.objects.filter(fechaPago__year=year,mesPagado='Febrero',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total3=Pago.objects.filter(fechaPago__year=year,mesPagado='Marzo',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total4=Pago.objects.filter(fechaPago__year=year,mesPagado='Abril',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total5=Pago.objects.filter(fechaPago__year=year,mesPagado='Mayo',PagoRegistrado="Mensual",tipoPago="Depósito").count()        
        
        total6=Pago.objects.filter(fechaPago__year=year,mesPagado='Junio',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total7=Pago.objects.filter(fechaPago__year=year,mesPagado='Julio',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total8=Pago.objects.filter(fechaPago__year=year,mesPagado='Agosto',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total9=Pago.objects.filter(fechaPago__year=year,mesPagado='Septiembre',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total10=Pago.objects.filter(fechaPago__year=year,mesPagado='Octubre',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total11=Pago.objects.filter(fechaPago__year=year,mesPagado='Noviembre',PagoRegistrado="Mensual",tipoPago="Depósito").count()

        total12=Pago.objects.filter(fechaPago__year=year,mesPagado='Diciembre',PagoRegistrado="Mensual",tipoPago="Depósito").count() 

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]

        return data


    def get_tipo_de_pagos_total_Mer(self,*args, **kwargs):
        data = [] 
        anio = self.kwargs.get('date')
        year= anio 
       
        total1=Pago.objects.filter(fechaPago__year=year,mesPagado='Enero',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()
        
        total2=Pago.objects.filter(fechaPago__year=year,mesPagado='Febrero',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total3=Pago.objects.filter(fechaPago__year=year,mesPagado='Marzo',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total4=Pago.objects.filter(fechaPago__year=year,mesPagado='Abril',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total5=Pago.objects.filter(fechaPago__year=year,mesPagado='Mayo',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()        
        
        total6=Pago.objects.filter(fechaPago__year=year,mesPagado='Junio',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total7=Pago.objects.filter(fechaPago__year=year,mesPagado='Julio',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total8=Pago.objects.filter(fechaPago__year=year,mesPagado='Agosto',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total9=Pago.objects.filter(fechaPago__year=year,mesPagado='Septiembre',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total10=Pago.objects.filter(fechaPago__year=year,mesPagado='Octubre',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total11=Pago.objects.filter(fechaPago__year=year,mesPagado='Noviembre',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count()

        total12=Pago.objects.filter(fechaPago__year=year,mesPagado='Diciembre',PagoRegistrado="Mensual",tipoPago="Mercado Libre").count() 

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]

        return data
    
    def get_tipo_de_pagos_totales(self,*args, **kwargs):
        data = [] 
        anio = self.kwargs.get('date')
        year= anio
        total1=Pago.objects.filter(fechaPago__year=year,mesPagado='Enero',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')
        
        total2=Pago.objects.filter(fechaPago__year=year,mesPagado='Febrero',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total3=Pago.objects.filter(fechaPago__year=year,mesPagado='Marzo',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total4=Pago.objects.filter(fechaPago__year=year,mesPagado='Abril',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total5=Pago.objects.filter(fechaPago__year=year,mesPagado='Mayo',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')
        
        total6=Pago.objects.filter(fechaPago__year=year,mesPagado='Junio',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total7=Pago.objects.filter(fechaPago__year=year,mesPagado='Julio',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total8=Pago.objects.filter(fechaPago__year=year,mesPagado='Agosto',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total9=Pago.objects.filter(fechaPago__year=year,mesPagado='Septiembre',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total10=Pago.objects.filter(fechaPago__year=year,mesPagado='Octubre',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total11=Pago.objects.filter(fechaPago__year=year,mesPagado='Noviembre',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        total12=Pago.objects.filter(fechaPago__year=year,mesPagado='Diciembre',PagoRegistrado="Mensual").aggregate(R=Coalesce(Sum('monto'),0)).get('R')

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]
        print(data)
        return data

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['buscaraño'] = self.get_año()
        context['buscarañoSig'] = self.get_añoSig()
        context['buscarañoan'] = self.get_añoAnterior()
        context['reportConConvenio'] = self.get_report_Con_Convenio()
        context['reportSinConvenio'] = self.get_report_Sin_Convenio()
        context['report_year_month'] = self.get_report_year_month()
        context['report_alumnos_activos'] = self.get_alumnos_activos()
        context['report_tipo_de_pagos'] = self.get_tipo_de_pagos()
        context['report_tipo_de_pagos_trans'] = self.get_tipo_de_pagos_Tranferencia()
        context['report_tipo_de_pagos_total'] = self.get_tipo_de_pagos_total()
        context['report_tipo_de_pagos_totales'] = self.get_tipo_de_pagos_totales()
        context['report_tipo_de_pagos_totales_Mer'] = self.get_tipo_de_pagos_total_Mer()
        return context
