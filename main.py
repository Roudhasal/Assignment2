from ebook import EBook
from catalog import Catalog
from customer import Customer
from cart import ShoppingCart
from order import Order
from discount_pricing import DiscountPricing
from invoice import Invoice

# Create e-books
ebook1 = EBook("Programming Fund", "Abdulla Ali", "2023-01-15", "Programming", 20.0)
ebook2 = EBook("Machine Learning", "Sajad Ali", "2022-07-10", "ML", 15.0)

# Update e-book rating
ebook1.set_rating(4.5)
ebook2.set_rating(4.0)

# Create a catalog and add e-books
catalog = Catalog()
catalog.add_ebook(ebook1)
catalog.add_ebook(ebook2)
catalog.show_catalog()

# Create a customer
customer = Customer("Shaikha", "shaikha@example.com", True)

# Create a shopping cart and add e-books
cart = ShoppingCart()
cart.set_owner(customer.get_name())
cart.add_item(ebook1)
cart.add_item(ebook2)
cart.view_cart()

# Calculate total and apply discounts
base_price = cart.get_total_price()
pricing = DiscountPricing(base_price, customer.is_loyalty_member(), len(cart._ShoppingCart__items))
discounted_price = pricing.apply_discounts()

# Create an order and generate invoice
order = Order(customer, cart)
print(order.get_order_details())

invoice = Invoice(discounted_price)
print(invoice.generate_invoice())
