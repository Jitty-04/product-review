from django.shortcuts import render
from django.views.generic import View
from product_review.forms import Review_form
from product_review.models import Review,Product

class AddReview(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=Review_form(instance=data)
        return render(request,"reviewadd.html",{"form":form})
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=Review_form(request.POST,instance=data)
        if form.is_valid():
            form=Review.objects.create(**form.cleaned_data)
            
        return render(request,'reviewadd.html',{'form':form})