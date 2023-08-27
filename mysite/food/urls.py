from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # index view
    path('', views.index, name='index'),
    # path('', views.IndexClassView.as_view(), name='index'),

    # hello view
    path('hello/', views.hello, name='hello'),

    # item view
    path('item/', views.item, name='item'),

    # detail view
    path('<int:item_id>/', views.detail, name='detail'),
    # path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),

    # create item view
    # path('add/', views.create_item, name='create_item'),
    path('add/', views.CreateItem.as_view(), name='create_item'),


    # update view
    path('update/<int:id>/', views.update_item, name='update_item'),

    # delete view
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]