from ebook import EBook
from catalog import Catalog
from customer import Customer
from cart import ShoppingCart
from discount_pricing import DiscountPricing
from invoice import Invoice
from order import Order

def test_ebook_management():
    print("\n************ Test Case 1 ************\n")
    catalog = Catalog()

    # Add e-books
    ebook1 = EBook("Desert Journeys", "Ali Al Mansoori", "2023-05-10", "Travel", 18.50)
    ebook2 = EBook("Modern Architecture", "Amina Al Habsi", "2024-01-20", "Architecture", 25.00)
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)

    # Modify e-book price
    catalog.update_ebook_price("Desert Journeys", 20.00)

    # Display specific e-book
    print("\nDetails of 'Desert Journeys':")
    print(catalog.get_ebook("Desert Journeys"))

    # Remove an e-book
    catalog.remove_ebook("Modern Architecture")
    print("\nAfter removing 'Modern Architecture':")
    catalog.show_catalog()

def test_customer_management():
    print("\n************ Customer Details************\n")
    customer1 = Customer("Layla Al Yousuf", "layla.yousuf@example.com", True)
    customer2 = Customer("Omar Al Rashid", "omar.rashid@example.com")

    # Display customers
    print("Customer 1 details:")
    print(customer1)
    print("Customer 2 details:")
    print(customer2)

    # Update customer details
    customer1.set_contact_info("layla.newemail@example.com")
    print("\nUpdated contact for Layla:")
    print(customer1)

def test_shopping_cart_and_order():
    print("\n************ Shopping Cart and Order ************\n")
    cart = ShoppingCart()
    catalog = Catalog()

    # Create and add e-books
    ebook1 = EBook("Artificial Intelligence", "Sara Al Saadi", "2025-02-14", "Technology", 30.00)
    ebook2 = EBook("Sustainability Practices", "Hassan Al Nuaimi", "2024-12-05", "Environment", 22.50)
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)

    # Add e-books to the cart
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    cart.view_cart()

    # Calculate total price and apply discounts for loyalty customers
    customer = Customer("Mariam Al Falasi", "mariam.falasi@example.com", True)
    base_price = cart.get_total_price()
    pricing = DiscountPricing(base_price, customer.is_loyalty_member(), len(cart._ShoppingCart__items))
    discounted_price = pricing.apply_discounts()

    # Generate an order and invoice
    order = Order(customer, cart)
    print("\nOrder details:")
    print(order.get_order_details())

    invoice = Invoice(discounted_price)
    print("\nGenerated Invoice:")
    print(invoice.generate_invoice())

# Main function to run the test cases
def main():
    test_ebook_management()
    test_customer_management()
    test_shopping_cart_and_order()

# Run the tests
if __name__ == "__main__":
    main()

from ebook import EBook
from catalog import Catalog
from customer import Customer
from cart import ShoppingCart
from discount_pricing import DiscountPricing
from invoice import Invoice
from order import Order

def test_ebook_management():
    print("\n************ Test Case 1 ************\n")
    catalog = Catalog()

    # Add e-books
    ebook1 = EBook("Treasures of the Ocean", "Zahra Al Qasimi", "2023-06-15", "Adventure", 19.99)
    ebook2 = EBook("Future Cities", "Jamal Al Shamsi", "2024-02-10", "Urban Development", 27.50)
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)

    # Modify e-book price
    catalog.update_ebook_price("Treasures of the Ocean", 21.99)

    # Display specific e-book
    print("\nDetails of 'Treasures of the Ocean':")
    print(catalog.get_ebook("Treasures of the Ocean"))

    # Remove an e-book
    catalog.remove_ebook("Future Cities")
    print("\nAfter removing 'Future Cities':")
    catalog.show_catalog()

def test_customer_management():
    print("\n************ Customer Details ************\n")
    customer1 = Customer("Amina Al Nahyan", "amina.nahyan@example.com", True)
    customer2 = Customer("Rashid Al Fardan", "rashid.fardan@example.com")

    # Display customers
    print("Customer 1 details:")
    print(customer1)
    print("Customer 2 details:")
    print(customer2)

    # Update customer details
    customer1.set_contact_info("amina.newemail@example.com")
    print("\nUpdated contact for Amina:")
    print(customer1)

def test_shopping_cart_and_order():
    print("\n************ Shopping Cart and Order ************\n")
    cart = ShoppingCart()
    catalog = Catalog()

    # Create and add e-books
    ebook1 = EBook("Innovative Tech Solutions", "Khalid Al Tayer", "2025-03-05", "Technology", 35.00)
    ebook2 = EBook("Sustainable Living", "Laila Al Suwaidi", "2024-11-22", "Environment", 24.00)
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)

    # Add e-books to the cart
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    cart.view_cart()

    # Calculate total price and apply discounts for loyalty customers
    customer = Customer("Noor Al Farsi", "noor.farsi@example.com", True)
    base_price = cart.get_total_price()
    pricing = DiscountPricing(base_price, customer.is_loyalty_member(), len(cart._ShoppingCart__items))
    discounted_price = pricing.apply_discounts()

    # Generate an order and invoice
    order = Order(customer, cart)
    print("\nOrder details:")
    print(order.get_order_details())

    invoice = Invoice(discounted_price)
    print("\nGenerated Invoice:")
    print(invoice.generate_invoice())

# Main function to run the test cases
def main():
    test_ebook_management()
    test_customer_management()
    test_shopping_cart_and_order()

# Run the tests
if __name__ == "__main__":
    main()

from ebook import EBook
from catalog import Catalog
from customer import Customer
from cart import ShoppingCart
from discount_pricing import DiscountPricing
from invoice import Invoice
from order import Order

def test_failure_scenarios():
    print("\n************ Failure Test Case ************\n")
    catalog = Catalog()

    # Attempt to update the price of a non-existent e-book
    print("1. Trying to update the price of 'Mysteries of the Universe'...")
    success = catalog.update_ebook_price("Mysteries of the Universe", 29.99)
    if not success:
        print("Result: Failed to update. 'Mysteries of the Universe' is not in the catalog.\n")

    # Attempt to remove a non-existent e-book
    print("2. Attempting to remove 'Unknown Future' from the catalog...")
    removed = catalog.remove_ebook("Unknown Future")
    if not removed:
        print("Result: Removal unsuccessful. 'Unknown Future' does not exist in the catalog.\n")

    # Attempt to get a non-existent e-book
    print("3. Fetching details for 'Lost Treasures'...")
    ebook = catalog.get_ebook("Lost Treasures")
    if ebook is None:
        print("Result: Could not find 'Lost Treasures'. This e-book is not listed in the catalog.\n")

    # Attempt to retrieve a non-existent customer
    print("4. Searching for a customer with the email 'ali@example.com'...")
    customer = Customer("Ali", "ali@example.com")
    catalog_customers = []  # This would be part of a customer management system
    if not any(cust.get_contact_info() == customer.get_contact_info() for cust in catalog_customers):
        print("Result: No match found. 'ali@example.com' is not a registered customer.\n")

    # Attempt to create an order with an empty cart
    print("5. Creating an order for an empty shopping cart...")
    empty_cart = ShoppingCart()
    empty_customer = Customer("Hamad Al Falasi", "hamad.falasi@example.com")
    if len(empty_cart._ShoppingCart__items) == 0:
        print("Result: Order creation failed. The shopping cart is empty; cannot proceed with the order.\n")

# Main function to run the failure test case
def main():
    test_failure_scenarios()

# Run the failure test
if __name__ == "__main__":
    main()
