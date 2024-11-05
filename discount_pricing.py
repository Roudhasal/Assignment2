class DiscountPricing:
    """
    This class handles discount calculations for orders.
    """
    def __init__(self, base_price, loyalty_member=False, bulk_count=0):
        # Private attributes to store discount details
        self.__base_price = base_price  # attribute for the base price
        self.__loyalty_member = loyalty_member   # attribute for the loyalty member
        self.__bulk_count = bulk_count    # attribute for the bulk count of the books
        self.__discount_amount = 0  # Amount of discount applied
        self.__final_price = base_price  # Final price after discount

    # Getter for base price of the book
    def get_base_price(self):
        return self.__base_price

    # setter for base price of the book
    def set_base_price(self, base_price):
        self.__base_price = base_price

    # getter for discount amount 
    def get_discount_amount(self):
        return self.__discount_amount

    # setter for discount amount
    def set_discount_amount(self, discount_amount):
        self.__discount_amount = discount_amount

    # getter for final price
    def get_final_price(self):
        return self.__final_price

    # Method to calculate the final price after applying discounts
    def apply_discounts(self):
        discount = 0
        if self.__loyalty_member:
            discount += 0.10 * self.__base_price  # 10% discount for loyalty members
        if self.__bulk_count >= 5:
            discount += 0.20 * self.__base_price  # Additional 20% discount for bulk orders

        self.__final_price = self.__base_price - self.__discount_amount
        return self.__final_price

    # String representation of the discount details
    def __str__(self):
        return "Base Price: $" + str(self.__base_price) + ", Discount Amount: $" + str(self.__discount_amount) + ", Final Price: $" + str(self.__final_price)
