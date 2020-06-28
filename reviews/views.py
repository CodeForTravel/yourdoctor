from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from carts.models import CartItem
from reviews.models import Review
from . import forms


class ReviewFormView(LoginRequiredMixin,View):
    login_url = 'users:login'
    template_name = 'reviews/user_review_form.html'
    
    def get(self,request):
        form = forms.ReviewForm()
        args = {'form':form }
        return render(request,self.template_name, args)


def saverating(request):
    if request.method == 'POST':
        rating = request.POST['rat_value']
        comment = request.POST['comment']
        cartitem = CartItem.objects.filter(
                                            user = request.user,
                                            is_reviewed =False,
                                            appointment_complete=True
                                            ).last()

        # print(cartitem.appointment_type)
        # print(request.user)
        # print(cartitem.doctor)
        review = Review(
            user = request.user,
            doctor = cartitem.doctor,
            comment = comment,
            rating = rating,
            cart = cartitem
        )
        review.save()
        cartitem.is_reviewed = True
        cartitem.save()
        return redirect('users:user_profile')
        