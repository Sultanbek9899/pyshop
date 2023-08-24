from django import forms


from src.apps.product.models import Product, Category




class CreateProductForm(forms.ModelForm):
    price = forms.DecimalField(max_digits=10,decimal_places=2, widget=forms.NumberInput(attrs={"type":"number"}))    

    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]