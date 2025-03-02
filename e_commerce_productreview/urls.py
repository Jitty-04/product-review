"""
URL configuration for e_commerce_productreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product_review.views import AddProduct,ViewProudct,DeleteProduct,UpdateProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('addreview/<int:pk>',AddReview.as_view())
    path('addproduct/',AddProduct.as_view()),
    path('viewproduct/',ViewProudct.as_view()),
    path('deleteproduct/<int:pk>',DeleteProduct.as_view()),
    path('updateproduct/<int:pk>',UpdateProduct.as_view()),
    
]
