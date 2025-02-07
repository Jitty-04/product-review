from django import forms
from product_review.models import Product

class Product_form(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

# class Review_form(forms.ModelForm):
#     class Meta:
#         model=Review
#         fields=["reviewer_name","rating","comment"]