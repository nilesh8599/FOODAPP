from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from food.models import Item, History
from django.template import loader
from django.contrib import messages
from food.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from users.models import CusRatingFeedback, CusOrders

# Create your views here.

# function based index view
# ------------------------------------------------------------
def index(request):
    if request.user.is_superuser:
        item_list = Item.objects.all()

    elif request.user.is_authenticated and request.user.profile.user_type=='Restaurant':
        item_list = Item.objects.filter(for_user=request.user.username)

    elif request.user.is_authenticated and request.user.profile.user_type=='Customer':
        item_list = Item.objects.all()
        
    else:
        item_list = Item.objects.all()

    context = {
        'item_list':item_list,
    }
    
    return render(request, 'food/index.html', context)


# class based index view
# ------------------------------------------------------------
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


# function based hello view
# ------------------------------------------------------------
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")


# function based hello view
# ------------------------------------------------------------
def item(request):
    return HttpResponse("This is an item view")


# function based detail view with render
# ------------------------------------------------------------
def detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    hist = History.objects.filter(
        prod_ref = item.prod_code
    )

    if request.user.profile.user_type == 'Restaurant' or request.user.profile.user_type == 'Admin':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code = item.prod_code
        )
    
    elif request.user.profile.user_type == 'Customer':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code = item.prod_code,
            user = request.user.username
        )

    crf = CusRatingFeedback.objects.filter(
        prod_code = item.prod_code
    )

    context = {
        'item':item,
        'hist':hist,
        'crf':crf,
        "oco":Obj_CusOrd
    }
    # return HttpResponse("This is detail view: %s" % item_id)
    return render(request,'food/detail.html', context)

# class based detail view
# ------------------------------------------------------------
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
      
    # by default: context_object_name = 'object' or 'item' which is model_name(all lowercase)
    # or can have any user defined variable name as below
    # context_object_name = 'item_obj'
    # passes the object of the model

# function based create view
# ------------------------------------------------------------
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form':form})


# class based create view
# ------------------------------------------------------------
class CreateItem(CreateView):
    model = Item                                                                    # model
    fields = ['prod_code', 'item_name', 'item_desc', 'item_price', 'item_image']    # form structure
    template_name = 'food/item-form.html'                                           # renders item-form page
    success_url = reverse_lazy('food:index')                                        # redirects to index page 

    def form_valid(self, form):
       form.instance.user_name = self.request.user
       messages.success(
           self.request, 
           f'{self.request.user} Your item {self.request.POST.get("item_name")} has been successfully added.'
        )

       obj_History = History(
           user_name = self.request.user.username,
           prod_ref = form.instance.prod_code,
           item_name = self.request.POST.get('item_name'),
           op_type = 'Created'
       )

       obj_History.save()

       return super().form_valid(form)

# function based update view
# ------------------------------------------------------------
def update_item(request, id):
    item = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        messages.success(
            request, 
            f'Your item {item.item_name} has been successfully updated'
        )
        form.save()

        obj_History = History(
            user_name = request.user.username,
            prod_ref = item.prod_code,
            item_name = request.POST.get('item_name'),
            op_type = 'Updated'
        )

        obj_History.save()

        return redirect('food:index')

    return render(request, 'food/item-form.html',{'form':form, 'item':item})


# function based delete view
# ------------------------------------------------------------
def delete_item(request, id):
    item = Item.objects.get(pk = id)

    if request.method == 'POST':
        messages.success(
            request, 
            f'Your item {item.item_name} has been deleted'
        )

        obj_History = History(
            user_name = request.user.username,
            prod_ref = item.prod_code,
            item_name = item.item_name,
            op_type = 'Deleted'
        )

        obj_History.save()

        item.delete()

        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item':item})