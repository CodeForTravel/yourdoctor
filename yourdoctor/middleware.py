import re
from carts.models import CartItem
from django.shortcuts import redirect


class ReviewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self,request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            items = CartItem.objects.filter(
                user = request.user,
                appointment_complete = True,
                is_reviewed = False
                )
            # if items:
                # print(items)
                # return redirect("reviews:review_form")
        else:
            print("User is not authenticated!")