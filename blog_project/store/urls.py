from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('cart/add_order/<int:pk>/',views.createOrder,name='create_order'),
    path('store/',views.ProductListView.as_view(),name='store'),
    path('store/new_item',views.ProductCreateView.as_view(),name='store_new_item'),
    path('store/item/<int:pk>/',views.ProductDetailView.as_view(),name='store_item'),
    path('store/update_item/<int:pk>/',views.ProductUpdateView.as_view(),name='store_item_update'),
    path('checkOut/',views.checkOut,name='checkOut'),
    path('cart/update_quantity/',views.updateQuantity,name='update_quantity'),
]
