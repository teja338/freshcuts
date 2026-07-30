
from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = (
            "phone",
            "address",
            "delivery_slot",
            "payment_method",
        )

        widgets = {

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Mobile Number"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter Delivery Address"
                }
            ),

            "delivery_slot": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "payment_method": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }
