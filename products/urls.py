from django.urls import path

from .views import CreateStripeCheckoutSessionView
from .views import CancelView, SuccessView

app_name = "products"

urlpatterns = [
    path(
        "create-checkout-session/<int:pk>/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
]