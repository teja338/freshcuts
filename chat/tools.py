from django.db.models import Q
from products.models import Product


# -----------------------------------------
# Product Search Tool
# -----------------------------------------

def search_products(query):

    products = Product.objects.filter(

        Q(name__icontains=query) |
        Q(description__icontains=query)

    )[:10]

    if not products.exists():

        return None

    result = ""

    for product in products:

        result += f"""
Product Name : {product.name}
Price : ₹{product.price}
Description : {product.description}

----------------------------------
"""

    return result


# -----------------------------------------
# Recipe Tool
# -----------------------------------------

def recipe_tool(food):

    return f"""
Recipe Request

Main Ingredient : {food}

Generate:

1. Ingredients

2. Preparation Steps

3. Cooking Time

4. Protein

5. Calories
"""


# -----------------------------------------
# Offers Tool
# -----------------------------------------

def offers_tool():

    return """
Current FreshCuts Offers

• Free Delivery above ₹999

• Weekend Chicken Discount

• Buy 2 Get 1 Egg Pack
"""


# -----------------------------------------
# Delivery Tool
# -----------------------------------------

def delivery_tool(location):

    return f"""
Check delivery availability for

{location}
"""


# -----------------------------------------
# Order Tool
# -----------------------------------------

def order_tool(order_id):

    return f"""
Track Order

Order ID

{order_id}
"""


TOOLS = {

    "search_products": search_products,

    "recipe_tool": recipe_tool,

    "offers_tool": offers_tool,

    "delivery_tool": delivery_tool,

    "order_tool": order_tool,

}
