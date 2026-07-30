from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):

    CHICKEN = "Chicken"
    MUTTON = "Mutton"
    FISH = "Fish"
    EGGS = "Eggs"

    PRODUCT_TYPES = [
        (CHICKEN, "Chicken"),
        (MUTTON, "Mutton"),
        (FISH, "Fish"),
        (EGGS, "Eggs"),
    ]

    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPES
    )

    description = models.TextField()

    # Selling Price
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Original Price (for discounts)
    original_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    # Stock Available
    stock = models.PositiveIntegerField(default=0)

    # Product Image
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    # Product Weight
    weight = models.CharField(
        max_length=50,
        default="500 g"
    )

    # Product Rating
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.5
    )

    # Number of Reviews
    reviews = models.PositiveIntegerField(default=0)

    # Discount Percentage
    discount_percentage = models.PositiveIntegerField(default=0)

    # Featured Product
    is_featured = models.BooleanField(default=False)

    # Product Status
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        """
        Returns the discounted price based on original_price
        and discount_percentage.
        """
        if self.original_price and self.discount_percentage > 0:
            discount = (
                self.original_price * self.discount_percentage
            ) / 100
            return self.original_price - discount
        return self.price

    @property
    def in_stock(self):
        return self.stock > 0
