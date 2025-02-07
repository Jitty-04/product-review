from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()

# class Review(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     reviewer_name=models.CharField(max_length=100)
#     rating=models.PositiveIntegerField()
#     comment=models.TextField()
#     review_date=models.DateField(auto_now=True)   