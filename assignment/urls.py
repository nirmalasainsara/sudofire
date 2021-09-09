from django.urls import path
from . import apiviews

app_name = "assignment"

urlpatterns = [
    path(
        "",
        apiviews.Product_view.as_view(),
        name="product_view",
    ),
]
