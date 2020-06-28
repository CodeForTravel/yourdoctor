from django import forms

from . import models




class ReviewForm(forms.Form):
    
    comment = forms.CharField(label='Write a Review',
        max_length=300,required=False,
        widget=forms.Textarea(attrs={'placeholder':'Write your opinion!'}))

    # def deploy(self,rat_value):
    #     comment = self.cleaned_data.get('comment')
    #     print(comment)
    #     print(rat_value)