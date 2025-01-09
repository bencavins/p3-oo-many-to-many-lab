class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        results = []
        for contract in Contract.all:
            if contract.author is self:
                results.append(contract)
        return results

    def books(self):
        results = []
        for contract in self.contracts():
            results.append(contract.book)
        return list(set(results))
    
    def sign_contract(self, book, date, royalties):
        return Contract(author=self, book=book, date=date, royalties=royalties)
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

    def __repr__(self):
        return f'<Author {self.name}>'


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        results = []
        for contract in Contract.all:
            if contract.book is self:
                results.append(contract)
        return results
    
    def authors(self):
        results = []
        for contract in self.contracts():
            results.append(contract.author)
        return results
    
    def sign_contract(self, author, date, royalties):
        return Contract(author=author, book=self, date=date, royalties=royalties)    

    def __repr__(self):
        return f'<Book {self.title}>'


class Contract:
    all = []

    @classmethod
    def contracts_by_date(cls, date):
        results = []
        for contract in cls.all:
            if contract.date == date:
                results.append(contract)
        return results

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        # return self
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception("author needs to be an Author object")
        # if not isinstance(new_author, Author):
        #     raise Exception("author needs to be an Author object")
        # else:
        #     self._author = new_author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception("book needs to be an Book object")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str):
            self._date = new_date
        else:
            raise Exception("date needs to be a string")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, new_royalties):
        if isinstance(new_royalties, int) or isinstance(new_royalties, float):
            self._royalties = new_royalties
        else:
            raise Exception("royalties needs to be a number")
    
    def __repr__(self):
        return f'<Contract {self.author} {self.book} {self.date} {self.royalties}>'


# instantiation
# instantiate
a1 = Author(name='Charles Dickens')
b1 = Book(title='Tale of Two Cities')

c1 = Contract(author=a1, book=b1, date='2025-01-09', royalties=100.00)
