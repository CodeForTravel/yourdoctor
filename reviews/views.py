from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import forms


class ReviewFormView(LoginRequiredMixin,View):
    login_url = 'users:login'
    template_name = 'reviews/user_review_form.html'
    
    def get(self,request):
        form = forms.ReviewForm()
        args = {'form':form }
        return render(request,self.template_name, args)

    def post(self,request):
        form = forms.ReviewForm(request.POST or None)
        data_rating = request.POST.get('data_rating')
        print(data_rating)
        if form.is_valid():
            form.deploy()
        args = {
            'form':form,
        }
        return render(request,self.template_name,args)