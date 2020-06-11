from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from . import forms
# Create your views here.

class DegreeFormView(LoginRequiredMixin,View):
    login_url = 'users:login'
    
    template_name = 'degrees/degree_form.html'

    def get(self,request):
        form = forms.DegreeForm()
        variables = { 'form':form, }
        return render(request,self.template_name,variables)

    def post(self, request):
        form = forms.DegreeForm(request.POST or None)
        if form.is_valid():
            form.deploy(request)
            return redirect('users:user_profile')
        variables = { 'form': form, }
        return render(request, self.template_name, variables)
