from django.db import models
from django.conf import settings
from products.models import Product


class DeliverySlot(models.Model):

    SLOT_CHOICES = [
        ("7:00-8:00 AM", "7:00-8:00 AM"),
        ("8:00-9:00 AM", "8:00-9:00 AM"),
        ("11:30-12:30 PM", "11:30-12:30 PM"),
        ("5:30-6:30 PM", "5:30-6:30 PM"),
        ("6:30-7:30 PM", "6:30-7:30 PM"),
    ]

    slot = models.CharField(
        max_length=30,
        choices=SLOT_CHOICES,
        unique=True
    )

    max_orders = models.PositiveIntegerField(default=20)

    booked_orders = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.slot


class Order(models.Model):

    STATUS = [
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Preparing", "Preparing"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    PAYMENT_CHOICES = [
        ("COD", "Cash On Delivery"),
        ("UPI", "UPI"),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_orders"
    )

    delivery_slot = models.ForeignKey(
        DeliverySlot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default="Pending"
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default="COD"
    )

    address = models.TextField()

    phone = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product.name
