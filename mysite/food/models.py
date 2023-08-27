from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    # def __str__(self):
    #     return str((self.item_name, self.item_desc, str(self.item_price)))

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    prod_code = models.IntegerField(default=1)
    for_user = models.CharField(max_length=200, default='alex')
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=300, default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse tempora officiis, libero, eum nobis magnam fugiat totam voluptatibus veritatis error facilis fuga impedit quos pariatur at eligendi. Vero, veniam doloribus!')
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")

    # replaced with 'success_url = reverse_lazy('food:index')' in class based 'Createitem' view  
    # def get_absolute_url(self):
    #     # return reverse("food:details", kwargs={"pk": self.pk})
    #     return reverse("food:index")
    

class History(models.Model):
    
    def __str__(self):
        return str((self.prod_ref, self.user_name, self.item_name, self.op_type))

    user_name = models.CharField(max_length=200)
    prod_ref = models.IntegerField(default=100)
    item_name = models.CharField(max_length=200)
    op_type = models.CharField(max_length=100)

    
