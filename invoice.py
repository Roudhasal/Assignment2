class Invoice:
    """
    This class handles invoice generation for an order.
    """
    VAT_RATE = 0.08  # Constant for VAT rate

    def __init__(self, discounted_price):
        # Private attributes for invoice details
        self.__discounted_price = discounted_price
        self.__vat_amount = 0  # VAT amount calculated
        self.__total_price = 0  # Final price including VAT
        self.__invoice_id = "INV12345"  # Unique invoice ID

    # Getter for the discounted price
    def get_discounted_price(self):
        return self.__discounted_price

    # setter for the discounted price
    def set_discounted_price(self, discounted_price):
        self.__discounted_price = discounted_price

    # getter for the VAT amount 
    def get_vat_amount(self):
        return self.__vat_amount

    # setter for the VAT amount
    def set_vat_amount(self, vat_amount):
        self.__vat_amount = vat_amount

    # getter for the total price
    def get_total_price(self):
        return self.__total_price

    # setter for the total price
    def set_total_price(self, total_price):
        self.__total_price = total_price

    # getter for the invoice id
    def get_invoice_id(self):
        return self.__invoice_id

    # setter for the invoice id
    def set_invoice_id(self, invoice_id):
        self.__invoice_id = invoice_id

    # Method to generate the invoice details
    def generate_invoice(self):
        self.__vat_amount = self.__discounted_price * self.VAT_RATE
        self.__total_price = self.__discounted_price + self.__vat_amount
        invoice = "Invoice ID: " + self.__invoice_id + "\n"
        invoice += "Discounted Price: $" + str(self.__discounted_price) + "\n"
        invoice += "VAT (8%): $" + str(self.__vat_amount) + "\n"
        invoice += "Total Price (with VAT): $" + str(self.__total_price) + "\n"
        return invoice

    # String representation of the invoice
    def __str__(self):
        return "Invoice ID: " + self.__invoice_id + ", Total Price (with VAT): $" + str(self.__total_price)