from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    # customer rating-feedback view
    path('crf/<int:pc>/', views.CusRatFeed, name='CusRatFeed'),

    # orders
    path('orders/<int:id>/<int:pdcd>/<str:user>/', views.Orders, name='orders'),

    #updating orders
    path('upd_orders/<int:id>/<int:upd_order_id>', views.update_orders, name='upd_orders'),
     
    # updating customers ratings and feedbacks
    path('crf/<int:details_id>/<int:crf_id>/', views.update_crf, name = 'upd_crf'),

    # deleting customers ratings and feedbacks
    path('delete_crf/<int:details_id>/<int:crf_id>/', views.delete_crf, name = 'del_crf'),
    
]