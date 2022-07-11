from django import forms
from .models import Order

class RegisterProduct(forms.ModelForm):
    desc = forms.CharField(required=False)
    class Meta:
        model = Order
        fields = [
            'netPrice','customer','paymentMode','Status','deliveryAgent',
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
