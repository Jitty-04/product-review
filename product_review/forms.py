from django import forms
from product_review.models import Review

class Review_form(forms.ModelForm):
    class Meta:
        model=Review
        fields=["reviewer_name","rating","comment"]