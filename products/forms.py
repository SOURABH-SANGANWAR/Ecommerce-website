from django import forms
from .models import Product,Colour,Varient,Product_Seller

class RegisterProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'Name','Image','Price','MRP','Rating','Varients','Colours','category'
        ]
    Name = forms.CharField()
    Varients = forms.CharField()
    Colours = forms.ModelMultipleChoiceField(
        queryset=Colour.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    def clean_Rating(self,*args, **kwargs):
        x = self.cleaned_data.get('Rating')
        if(float(x)>5):
            raise forms.ValidationError("Rating is given out of 5")
        else:
            return x
    def clean_Varients(self,*args, **kwargs):
        x =  Varient.objects.create(Name = self.cleaned_data.get('Varients'))
        x.save()
        return x

