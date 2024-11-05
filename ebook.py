class EBook:
    """
    This class represents an e-book in the e-bookstore.
    """
    def __init__(self, title, author, publication_date, genre, price):
        # Private attributes that store information about the e-book
        self.__title = title  # Title of the Ebook
        self.__author = author  # Author of the ebook
        self.__publication_date = publication_date   # Date of Publication
        self.__genre = genre   # Genre of the ebook
        self.__price = price    # Price of the ebook
        self.__rating = 0.0  # Rating of the e-book
        self.__publisher = ""  # Publisher of the e-book

    # Getter for Title
    def get_title(self):
        return self.__title

    # Setter for title
    def set_title(self, title):
        self.__title = title
    
    # Getter for author
    def get_author(self):
        return self.__author
    
    # Setter for author
    def set_author(self, author):
        self.__author = author

    # Getter for Publication Date 
    def get_publication_date(self):
        return self.__publication_date

    # Setter for Publication Date
    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    # Getter for Genre
    def get_genre(self):
        return self.__genre

    # Setter for Genre 
    def set_genre(self, genre):
        self.__genre = genre

    # Getter for Price
    def get_price(self):
        return self.__price

    # Setter for Price
    def set_price(self, price):
        self.__price = price

    # Getter for rating
    def get_rating(self):
        return self.__rating

    # Setter for rating
    def set_rating(self, rating):
        if 0 <= rating <= 5:  # rating is between 0 and 5
            self.__rating = rating
        else:
            print("Rating must be between 0 and 5.")

    # Getter for Publisher
    def get_publisher(self):
        return self.__publisher

    # Setter for publisher
    def set_publisher(self, publisher):
        self.__publisher = publisher

    # String representation of the e-book
    def __str__(self):
        return "Title: " + self.__title + ", Author: " + self.__author + ", Genre: " + self.__genre + ", Price: $" + str(self.__price) + ", Rating: " + str(self.__rating)
