class Order:
    """
    This class represents an order made by a customer.
    """
    def __init__(self, customer, cart):
        # Private attributes for order details
        self.__customer = customer  # attribute for customer 
        self.__cart = cart    # attribute for cart
        self.__order_id = "ORD12345"  # Unique order ID
        self.__order_date = "2024-11-05"  # Fixed order date
        self.__status = "Processing"  # Status of the order
        self.__total_amount = cart.get_total_price()  # Total amount of the order

    # Getter for order id
    def get_order_id(self):
        return self.__order_id

    # setter for order id
    def set_order_id(self, order_id):
        self.__order_id = order_id

    # getter for order date
    def get_order_date(self):
        return self.__order_date

    # setter for order date
    def set_order_date(self, date):
        self.__order_date = date

    # getter for status
    def get_status(self):
        return self.__status

    # setter for status
    def set_status(self, status):
        self.__status = status

    # getter for total amount
    def get_total_amount(self):
        return self.__total_amount

    # setter for total amount
    def set_total_amount(self, amount):
        self.__total_amount = amount

    # Method to get order details
    def get_order_details(self):
        return "Order ID: " + self.__order_id + ", Date: " + self.__order_date + ", Status: " + self.__status + ", Total Amount: $" + str(self.__total_amount)

    # String representation of the order
    def __str__(self):
        return "Order ID: " + self.__order_id + ", Customer: " + self.__customer.get_name() + ", Total Amount: $" + str(self.__total_amount)
