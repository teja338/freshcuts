from decimal import Decimal
from products.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get("cart")

        if self.cart is None:
            self.cart = self.session["cart"] = {}

    def add(self, product, quantity=1):

        product_id = str(product.id)

        if product_id not in self.cart:

            self.cart[product_id] = {
                "quantity": quantity,
                "price": str(product.price),
            }

        else:

            self.cart[product_id]["quantity"] += quantity

        self.save()

    def increase(self, product):

        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]["quantity"] += 1
            self.save()

    def decrease(self, product):

        product_id = str(product.id)

        if product_id in self.cart:

            if self.cart[product_id]["quantity"] > 1:
                self.cart[product_id]["quantity"] -= 1
            else:
                del self.cart[product_id]

            self.save()

    def remove(self, product):

        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True

    def __iter__(self):

        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():

            item["price"] = Decimal(item["price"])

            item["subtotal"] = (
                item["price"] *
                item["quantity"]
            )

            yield item

    def get_total_price(self):

        return sum(
            item["subtotal"]
            for item in self
        )

    def total_quantity(self):

        return sum(
            item["quantity"]
            for item in self.cart.values()
        )

    def __len__(self):
        return self.total_quantity()
