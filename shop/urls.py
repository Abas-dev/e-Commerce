from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='homePage'),
    path('about/',views.AboutUsPageView.as_view(),name='aboutPage'),
    path('products/',views.ProductPageView.as_view(),name='product'),
    path('products/<int:id>/',views.SingleProductPageView.as_view(),name='singleProduct')
]
