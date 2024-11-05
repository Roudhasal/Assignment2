class ShoppingCart:
    """
    This class represents a shopping cart for a customer.
    """
    def __init__(self):
        # Private attributes to store the list of items and cart details
        self.__items = []  # list to store cart items
        self.__cart_id = "CART12345"  # Unique ID for the cart
        self.__total_items = 0  # Total number of items in the cart
        self.__owner = ""  # Name of the cart owner
        self.__last_updated = "2024-11-01"  # Last date the cart was updated

    # Getter for cart id
    def get_cart_id(self):
        return self.__cart_id

    # setter for cart id
    def set_cart_id(self, cart_id):
        self.__cart_id = cart_id

    # getter for total items
    def get_total_items(self):
        return self.__total_items

    # setter for total items
    def set_total_items(self, total):
        self.__total_items = total

    # getter for owner name
    def get_owner(self):
        return self.__owner

    # setter for owner name
    def set_owner(self, owner):
        self.__owner = owner

    # getter for last updated the cart
    def get_last_updated(self):
        return self.__last_updated

    # setetr for last update the cart
    def set_last_updated(self, date):
        self.__last_updated = date

    # Method to add an item to the cart
    def add_item(self, ebook):
        self.__items.append(ebook)
        self.__total_items += 1
        print("Added '" + ebook.get_title() + "' to the cart.")

    # Method to remove an item from the cart by title
    def remove_item(self, title):
        for ebook in self.__items:
            if ebook.get_title() == title:
                self.__items.remove(ebook)
                self.__total_items -= 1
                print("Removed '" + title + "' from the cart.")
                return
        print("E-book not found in the cart.")

    # Method to calculate the total price of all items in the cart
    def get_total_price(self):
        total_price = 0
        for ebook in self.__items:
            total_price += ebook.get_price()
        return total_price
    
    # Method to display the items in the cart
    def view_cart(self):
        if not self.__items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for ebook in self.__items:
                print(ebook)

    # String representation of the cart
    def __str__(self):
        return "Cart ID: " + self.__cart_id + ", Owner: " + self.__owner + ", Total Items: " + str(self.__total_items)