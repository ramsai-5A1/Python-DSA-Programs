class BookTemplate:
    def __init__(self, book_id, book_name, book_author, book_price, book_publishing_year):
        self.book_id = book_id 
        self.book_name = book_name 
        self.book_author = book_author 
        self.book_price = book_price 
        self.book_publishing_year = book_publishing_year 
        
    def printAllDetails(self):
        print("Book id is:", self.book_id)
        print("Book name is:", self.book_name)
        print("Book author is:", self.book_author)
        print("Book price is:", self.book_price)
        print("Book pubishing year is:", self.book_publishing_year)
    
    def printIdNamePrice(self):
        print("Book id is:", self.book_id)
        print("Book name is:", self.book_name)
        print("Book price is:", self.book_price)
        
    
    def printIsCostlier(self):
        if self.book_price > 100:
            print("Costlier")
        else:
            print("Affordable")
            
book1 = BookTemplate("501", "The Miracle Morning", "Hal Elrod", 276, 2015)
book2 = BookTemplate("502", "The Psychlogy of Money", "Morgan Housel", 198, 2008)
book3 = BookTemplate("503", "The Young that india wants", "Chetan Bhagat", 345, 2012)

book1.printAllDetails()
book1.printIdNamePrice()
book1.printIsCostlier()

book2.printAllDetails()
book2.printIdNamePrice()
book2.printIsCostlier()

book3.printAllDetails()
book3.printIdNamePrice()
book3.printIsCostlier()

    
    
    
    