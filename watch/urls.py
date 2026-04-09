from django.urls import path
from .views import *

urlpatterns = [
    path("category/<int:pk>/", CategoryProducts.as_view(), name="categories_products"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("deatil/<int:pk>/", ProductDetailView.as_view(), name="detail-legacy"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete"),
    path("my_products/", MyProducts.as_view(), name="myProducts"),
    path("products/", ProductsListView.as_view(), name="product-list"),
    path("category/<int:pk>", CategoryProducts.as_view(), name="categories_products_legacy"),
    path("create", ProductCreateView.as_view(), name="create-legacy"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="update-legacy"),
    path("detail/<int:pk>", ProductDetailView.as_view(), name="detail-legacy-2"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="delete-legacy"),
    path("my_products", MyProducts.as_view(), name="myProducts-legacy"),
    path("products", ProductsListView.as_view(), name="product-list-legacy"),
]
