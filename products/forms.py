from django import forms
from .models import Product

class RegisterProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'Name','Image','Price','MRP','Rating',
        ]
    def clean_name(self,*args, **kwargs):
        x = self.cleaned_data.get('Name')
        if(len(x)>50):
            raise forms.ValidationError("Name length exceeded")
        else:
            return x
    def clean_Rating(self,*args, **kwargs):
        x = self.cleaned_data.get('Rating')
        if(float(x)>5):
            raise forms.ValidationError("Rating is given out of 5")
        else:
            return x
