# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet, CategoryViewSet, InstallmentPlanViewSet, DiscountViewSet

# router = DefaultRouter()
# router.register(r'products', ProductViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'installment-plans', InstallmentPlanViewSet)
# router.register(r'discounts', DiscountViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]



from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name='product-detail'),
]

