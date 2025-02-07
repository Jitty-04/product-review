from django.shortcuts import render
from django.views.generic import View
from product_review.forms import Product_form
from product_review.models import Product

class AddProduct(View):
    def get(self,request):
        form=Product_form
        return render(request,"addproduct.html",{'form':form})
    
    def post(self,request):
        form=Product_form(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            form=Product_form
        return render(request,'addproduct.html',{'form':form})
    

class ViewProudct(View):
    def get(self,request):
        data=Product.objects.all()
        return render(request,"view.html",{'data':data})
    
class DeleteProduct(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        return render(request,"confirmdelete.html",{"data":data})
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id).delete()
        return render(request,'delete.html',{"data":data})
class UpdateProduct(View):
    def get(sellf,request,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=Product_form(instance=data)
        return render(request,"update.html",{"form":form})
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=Product_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return render(request,'update.html',{"form":form})

    

        




   