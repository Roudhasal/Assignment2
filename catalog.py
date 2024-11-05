class Catalog:
    """
    This class manages the collection of e-books in the e-bookstore.
    """
    def __init__(self):
        # Private attribute to store a list of e-books
        self.__ebooks = []   # List to store e books catalog
        self.__catalog_name = "The Great E-Books Store"    # Caalog name 
        self.__last_updated = "2024-11-01"  # Last date when catalog was updated
        self.__total_ebooks = 0  # Total number of e-books in the catalog
        self.__catalog_id = "CAT12345"

    # Getter for catalog name
    def get_catalog_name(self):
        return self.__catalog_name

    # setter for catalog name
    def set_catalog_name(self, name):
        self.__catalog_name = name

    # getter for last updated
    def get_last_updated(self):
        return self.__last_updated

    # Setter for last updated
    def set_last_updated(self, date):
        self.__last_updated = date

    # Getter for total books
    def get_total_ebooks(self):
        return self.__total_ebooks

    # Setter for total books
    def set_total_ebooks(self, total):
        self.__total_ebooks = total

    # Getter for catalog ID
    def get_catalog_id(self):
        return self.__catalog_id

    # Setter for catalog ID
    def set_catalog_id(self, catalog_id):
        self.__catalog_id = catalog_id

    # Method to add an e-book to the catalog
    def add_ebook(self, ebook):
        self.__ebooks.append(ebook)
        self.__total_ebooks += 1
        print("E-book '" + ebook.get_title() + "' has been added to the catalog.")

    # Method to get an e-book by title
    def get_ebook(self, title):
        for ebook in self.__ebooks:
            if ebook.get_title() == title:
                return ebook  # Return the e-book object
        print("E-book not found.")
        return None  # E-book not found
    
    # Method to remove an e-book by title
    def remove_ebook(self, title):
        for ebook in self.__ebooks:
            if ebook.get_title() == title:
                self.__ebooks.remove(ebook)
                self.__total_ebooks -= 1
                print("E-book '" + title + "' has been removed from the catalog.")
                return
        print("E-book not found in the catalog.")

    # Method to display the catalog
    def show_catalog(self):
        if not self.__ebooks:
            print("The catalog is empty.")
        else:
            print("Catalog '" + self.__catalog_name + "' contains:")
            for ebook in self.__ebooks:
                print(ebook)

    # Method to update the price of an e-book by title
    def update_ebook_price(self, title, new_price):
        for ebook in self.__ebooks:
            if ebook.get_title() == title:
                ebook.set_price(new_price)
                print("Updated price for '" + title + "' to $" + str(new_price))
                return True  # Price updated successfully
        print("E-book not found in the catalog.")
        return False  # E-book not found
    
    # String representation of the catalog
    def __str__(self):
        return "Catalog Name: " + self.__catalog_name + ", Total E-books: " + str(self.__total_ebooks) + ", Last Updated: " + self.__last_updated

