from django import forms

from . import models 
from users.models import CustomUser




class ReviewForm(forms.Form):
    
    comment = forms.CharField(label='Comment',
        max_length=300,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Write your openion!'}))
    rating = forms.IntegerField(label='Rating',required=False,max_value=5,min_value=1)

    def clean(self):
        comment = self.cleaned_data.get('comment')
        rating = self.cleaned_data.get('rating')
        
        
        if not comment and not rating:
            raise forms.ValidationError('Please write your valuable openion!')

    def deploy(self):
        comment = self.cleaned_data.get('comment')
        rating = self.cleaned_data.get('rating')
        print(comment)
        print(rating)