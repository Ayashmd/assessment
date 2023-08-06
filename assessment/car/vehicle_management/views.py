from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
import os
# Create your views here.

class superreg(generic.CreateView):
    form_class = superform
    template_name = 'superreg.html'
    success_url = reverse_lazy('logs')
    def post(self, request):
        cps = request.POST.get('confirm_password')
        a = self.form_class(request.POST)
        if a.is_valid():
            pa = a.cleaned_data['password']
            if pa == cps:
                a.save()
                return redirect('logs')
            else:
                return HttpResponse("password no match")
        return HttpResponse("failed")

class adminreg(generic.CreateView):
    form_class = adminform
    template_name = 'adminreg.html'
    success_url = reverse_lazy('loga')

    def post(self, request):
        cps = request.POST.get('confirm_password')
        a = self.form_class(request.POST)
        if a.is_valid():
            pa = a.cleaned_data['password']
            if pa == cps:
                a.save()
                return redirect('loga')
            else:
                return HttpResponse("password no match")
        return HttpResponse("failed")

class adminlog(generic.View):
    form_class = adminlogs
    template_name = 'adminlog.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            a = adminlogs(request.POST)
        if a.is_valid():
            us = a.cleaned_data['email']
            pn = a.cleaned_data['password']
            b = admins.objects.all()
            for i in b:
                if i.email == us and i.password == pn:
                    return redirect('disa')
            else:
                return HttpResponse("login failed")


class admindisplay(generic.ListView):
    model = vehiclemodel
    template_name = 'admindisplay.html'
    def get(self, request):
        a = self.model.objects.all()
        return render(request, self.template_name, {'a': a})

class adminedit(generic.UpdateView):
    model = vehiclemodel
    template_name = 'updateadmin.html'
    fields = ['Vehiclenumber', 'Vehicletype', 'vehiclemodel', 'vehicledesc']
    success_url = reverse_lazy('disa')


class adminview(generic.DetailView):
    model = vehiclemodel
    template_name = 'adminview.html'


def sucs(request):
    return render(request,'sucs.html')

class superlog(generic.View):
    form_class = logsform
    template_name = 'superlog.html'
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            a = logsform(request.POST)
        if a.is_valid():
            us = a.cleaned_data['email']
            pn = a.cleaned_data['password']
            b = superadmins.objects.all()
            for i in b:
                if i.email == us and i.password == pn:
                    return redirect('sup')
            else:
                return HttpResponse("login failed")

class addvehicle(generic.CreateView):
    form_class = add
    template_name = 'vehiclereg.html'
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=add(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sdis')
        return redirect(request,self.template_name,{'form':form})

class superdisplay(generic.ListView):
    model = vehiclemodel
    template_name = 'superdisplay.html'
    def get(self,request):
        a=self.model.objects.all()
        return render(request,self.template_name,{'a':a})

class editsuper(generic.UpdateView):
    model = vehiclemodel
    template_name = 'updatesuper.html'
    fields =['Vehiclenumber','Vehicletype','vehiclemodel','vehicledesc']
    success_url = reverse_lazy('sdis')


class deletesuper(generic.DeleteView):
     model = vehiclemodel
     template_name = 'delete.html'
     success_url = reverse_lazy('sdis')


class userreg(generic.CreateView):
    form_class = userregform
    template_name = 'userreg.html'
    success_url = reverse_lazy('logu')

    def post(self, request):
        cps = request.POST.get('confirm_password')
        a = self.form_class(request.POST)
        if a.is_valid():
            pa = a.cleaned_data['password']
            if pa == cps:
                a.save()
                return redirect('usl')
            else:
                return HttpResponse("password no match")
        return HttpResponse("failed")


class userlog(generic.View):
    form_class = userlogform
    template_name = 'userlog.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            a = userlogform(request.POST)
        if a.is_valid():
            us = a.cleaned_data['email']
            pn = a.cleaned_data['password']
            b = user.objects.all()
            for i in b:
                if i.email == us and i.password == pn:
                    return redirect('usd')
            else:
                return HttpResponse("login failed")

class userdisplay(generic.ListView):
    model = vehiclemodel
    template_name = 'userdisplay.html'

    def get(self, request):
        a = self.model.objects.all()
        return render(request, self.template_name, {'a': a})

class superview(generic.DetailView):
    model = vehiclemodel
    template_name = 'superview.html'



def index(request):
    return render(request,'index.html')

def super(request):
    return render(request,'superadmin.html')