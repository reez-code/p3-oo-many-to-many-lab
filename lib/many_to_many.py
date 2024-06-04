class Author:
    all = []
    def __init__(self, name):
        self.name = name
        self.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]        
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
           return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(royalties)

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self] 
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self] 

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        else:
            self.author = author
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        else:
            self.book = book
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        else:
            self.date = date
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be a integer")
        else:
            self.royalties = royalties
        
        self.all.append(self)
    
    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]