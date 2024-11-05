class Customer:
    """
    This class represents a customer in the e-bookstore.
    """
    def __init__(self, name, contact_info, loyalty_member=False):
        # Private attributes to store customer information
        self.__name = name  # name attribute
        self.__contact_info = contact_info   # contact information attribute
        self.__loyalty_member = loyalty_member  # loyalty member attribute
        self.__customer_id = "CUST12345"  # Unique ID for the customer
        self.__purchase_history = []  # List of e-books purchased

    # Getter for name
    def get_name(self):
        return self.__name

    # setter for name
    def set_name(self, name):
        self.__name = name

    # getter for contact information
    def get_contact_info(self):
        return self.__contact_info

    # setter for contact information
    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info
    
    def is_loyalty_member(self):
        return self.__loyalty_member

    # setter for loyalty member
    def set_loyalty_member(self, status):
        self.__loyalty_member = status

    # getter for customer id
    def get_customer_id(self):
        return self.__customer_id

    # setter for customer id
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    # getter for purchase history
    def get_purchase_history(self):
        return self.__purchase_history

    # setter for purchase history
    def set_purchase_history(self, history):
        self.__purchase_history = history

    # String representation of the customer
    def __str__(self):
        loyalty_status = "Loyalty Member" if self.__loyalty_member else "Regular Customer"
        return "Customer ID: " + self.__customer_id + ", Name: " + self.__name + ", Contact: " + self.__contact_info + ", Status: " + loyalty_status
