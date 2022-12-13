from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import admin
from django.urls import reverse_lazy
from Cedva1.models import *
from AlumnosAdmin.forms import FormularioAlumno 
from Pago.forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import *
from datetime import *
from .filters import *

@staff_member_required(login_url="/loginuser/")  
def pagos(request):
    return render(request, "pagos.html")  

class registroPagos(LoginRequiredMixin,CreateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model = Pago
    template_name = 'RegistroPago.html'
    second_model = Alumno
    form_class = FormularioPago
    success_url = reverse_lazy('registroPagos')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(registroPagos, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago = form.save(commit=False)
            registropago.PagoRegistrado = "Mensual"
            registropago.alumno_id = self.kwargs.get('pk')
            registropago.save() 
            messages.success(request, 'Agregado con éxito.')
            return render(request,'RegistroPago.html', {'registropago' : registropago})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 


class diferentepago(LoginRequiredMixin,CreateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    success_url = reverse_lazy('diferentepago')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(diferentepago, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago1 = form.save(commit=False)
            registropago1.PagoRegistrado = "modelo_educativo"
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            messages.success(request, 'Agregado con éxito.')
            return render(request,'RegistroPago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 

class diferentepago1(LoginRequiredMixin,CreateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    success_url = reverse_lazy('diferentepago1')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(diferentepago1, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago1 = form.save(commit=False)
            registropago1.PagoRegistrado = "reincripcion"
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'RegistroPago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 

class diferentepago2(LoginRequiredMixin,CreateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    #second_form_class = FormularioAlumno
    success_url = reverse_lazy('diferentepago2')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        context=super(diferentepago2, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        id_alumno = kwargs['pk']
        form=self.form_class(request.POST)
        if form.is_valid():
            registropago1 = form.save(commit=False)
            Alumno.objects.filter(id=id_alumno).update(certificado=True)
            registropago1.PagoRegistrado = "certificado"
            registropago1.Findepagos = True
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'RegistroPago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 

class anual(LoginRequiredMixin,CreateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    success_url = reverse_lazy('anual')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(anual, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago1 = form.save(commit=False)
            registropago1.PagoRegistrado = "anual"
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'RegistroPago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 

class Manual(LoginRequiredMixin,CreateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    success_url = reverse_lazy('Manual')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(Manual, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago1 = form.save(commit=False)
            registropago1.PagoRegistrado = "Manual"
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'RegistroPago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form))             

@staff_member_required(login_url="/loginuser/")
def alumnoConPagosPendientes(request):
    mes = request.POST.get('mes')
    year=datetime.now().year  
    inicioAlumno=Alumno.objects.all()
    totalc=Pago.objects.filter(fechaPago__year=year, mesPagado=mes,PagoRegistrado="Mensual").exclude(Estado_pago=True)
    return render(request,'pagosPendientes.html',{'alumno':totalc})     

@staff_member_required(login_url="/loginuser/")
def alumnoConPagosnoRealizo(request):
    mes = request.POST.get('mes')
    year = request.POST.get('anio')
    year1=request.POST.get('ano1')
    inicioAlumno=Alumno.objects.filter(~Exists(Pago.objects.filter(alumno_id=OuterRef('id'),fechaPago__year=year1, mesPagado=mes))).filter(inicioCurso__year=year).exclude(certificado=True).exclude(activo_por_pagos=False)
    myfilter = buscaFilter(request.GET, queryset=inicioAlumno)
    inicioAlumno=myfilter.qs
    pago = Pago.objects.all()
    myfilterdos = buscaFilterDos(request.GET, queryset=pago)
    pago = myfilterdos.qs
    
    return render(request,'pagonoRealizadoEnero.html',{'inicioAlumno':inicioAlumno, 'myfilter':myfilter, 'myfilterdos':myfilterdos, 'pago':pago}) 
        

@staff_member_required(login_url="/loginuser/") 
def pagoalumno(request):
    return render(request, "pagosAlumno.html") 
   

@staff_member_required(login_url="/loginuser/")
def pagados_por_mes(request):
    year=datetime.now().year 
    month=request.POST.get('mes')
    day=datetime.now().day
    inicioAlumno=Alumno.objects.filter(certificado=False)
    totalc=Pago.objects.filter(Findepagos=False, mesPagado=month,PagoRegistrado="Mensual").exclude(Estado_pago=False)
    return render(request,'pagosrealizados.html',{'alumno':totalc,'inicioAlumno':inicioAlumno}) 

@staff_member_required(login_url="/loginuser/")    
def AlumnoPagoListView(request,pk): 
    pago=Pago.objects.filter(alumno_id=pk,PagoRegistrado="Mensual")
    Modelo=Pago.objects.filter(alumno_id=pk,PagoRegistrado="modelo_educativo")
    reincripcion=Pago.objects.filter(alumno_id=pk,PagoRegistrado="reincripcion")
    certificado=Pago.objects.filter(alumno_id=pk,PagoRegistrado="certificado")
    anual=Pago.objects.filter(alumno_id=pk,PagoRegistrado="anual")
    Manual=Pago.objects.filter(alumno_id=pk,PagoRegistrado="Manual")
    total = Pago.objects.filter(alumno_id=pk).count()
    alumno = Alumno.objects.filter(id=pk).only('nombreA', 'apellidoPA', 'apellidoMA','especialidad')
    return render(request,'pagosAlumno.html',{'pago':pago,'anual':anual,'Manual':Manual ,'total':total, 'alumno':alumno, 'Modelo':Modelo, 'reincripcion':reincripcion,'certificado':certificado})      

#@staff_member_required(login_url="/loginuser/")
class Actualizarpago(LoginRequiredMixin,UpdateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model=Pago
    template_name='actualizaPago.html'
    form_class = FormularioPago

    def get_success_url(self):
        return reverse_lazy('pagoalumno',kwargs={'pk':self.object.alumno_id})
#@staff_member_required(login_url="/loginuser/")
class ActualizarpagoOTRO(LoginRequiredMixin,UpdateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model=Pago
    template_name='actualizaPago.html'
    form_class = FormularioACTUALIZAROTROS

    def get_success_url(self):
        return reverse_lazy('pagoalumno',kwargs={'pk':self.object.alumno_id})
#@staff_member_required(login_url="/loginuser/")
class ActualizarpagoOTRO1(LoginRequiredMixin,UpdateView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model=Pago
    template_name='actualizaPago1.html'
    form_class = FormularioACTUALIZAROTROS

    def get_success_url(self):
        return reverse_lazy('pendientes')        

@staff_member_required(login_url="/loginuser/")
def AlumnoPListView(request):
    model =Alumno.objects.filter(activo_por_pagos=True,certificado=False)
    return render(request,'pagos.html',{'listas':model})      
          

#@staff_member_required(login_url="/loginuser/")
class eliminarPago(LoginRequiredMixin,DeleteView):
    login_url = '/loginuser/'
    redirect_field_name = 'loginuser'
    model = Pago
    template_name = 'PagoElimina.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Pago'] = 'Pago'
        context['list_url'] = reverse_lazy('pagoalumno', kwargs={'pk':self.object.alumno_id})
        return context
    
    def get_success_url(self):
        return reverse_lazy('pagoalumno',kwargs={'pk':self.object.alumno_id})