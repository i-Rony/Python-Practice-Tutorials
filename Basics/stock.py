import json
from operator import attrgetter, itemgetter
from copy import copy
from functools import reduce, partial

class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
   
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
    
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw = True)


##### itemgetter and attrgetter
#pub_sort = sorted(RAW_BOOKS, key = itemgetter('publish_date'))
#print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
#
#pages_sort = sorted(BOOKS, key = attrgetter('number_of_pages'))
#print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

##### map
def sales_price(book):
    """ Apply a 20% discount to the book's price """
    book = copy(book)
    book.price = round(book.price - book.price * .2, 2)

    return book

#sales_book = list(map(sales_price, BOOKS))
#print(BOOKS[0].price)
#print(sales_book[0].price)

#sales_book = [sales_price(book) for book in BOOKS]
#print(sales_book[0].price)

##### filter
def is_long_book(book):
    """ Does this book has 600+ pages """
    return book.number_of_pages >= 600

#long_books = list(filter(is_long_book, BOOKS))
#print(len(BOOKS))
#print(len(long_books))
#
#long_books_2 = [book for book in BOOKS if is_long_book(book)]
#long_books_3 = [book for book in BOOKS if book.number_of_pages >= 600]
#
#print(len(long_books_2))
#print(len(long_books_3))

##### map and filter
def has_roland(book):
    return any(["Roland" in subject for subject in book.subjects])

def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book

#print(len(list(map(titlecase, filter(has_roland, BOOKS)))))

#def is_good_deal(book):
#    return book.price <= 5
#
#cheap_books = sorted(filter(is_good_deal, map(sales_price, BOOKS)), key = attrgetter('price'))
#print(cheap_books[0])
#print(cheap_books[0].price)

##### map and reduce, filter
#def product(x, y):
#    return x * y
#
#print(reduce(product, [1, 2, 3, 4, 5]))

#total = 1
#for x in [1, 2, 3, 4, 5]:
#    total = x * total
#print(total)

def add_book_prices(book1, book2):
    return book1 + book2

#total = reduce(add_book_prices, [b.price for b in BOOKS])
#
#print(total)
#
#def long_total(a=None, b=None, books=None):
#    if a is None and b is None and books is None:
#        return None
#    if a is None and b is None and books is not None:
#        a = books.pop(0)
#        b = books.pop(0)
#        return long_total(a, b, books)
#    if a is not None and books and books is not None and b is None:
#        b = books.pop(0)
#        return long_total(a, b, books)
#    if a is not None and b is not None and books is not None:
#        return long_total(a+b, None, books)
#    if a is not None and b is not None and not books:
#        return long_total(a+b, None, None)
#    if a is not None and b is None and not books or books is None:
#        return a

#print(long_total(None, None, [b.price for b in BOOKS]))

#def factorial(n):
#    if n == 1:
#        return 1
#    else:
#        return n * factorial(n-1)
#
#print(factorial(5))


##### Lambda
total = reduce(lambda x, y: x+y, [b.price for b in BOOKS])
#print(total)

long_books = list(filter(lambda book: book.number_of_pages >= 600, BOOKS))
#print(len(long_books))



##### partial
#currying

def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price - book.price * discount, 2)
    return book

standard = partial(mark_down, discount = .2 )
half = partial(mark_down, discount = .5)

half_price_book = list(map(half, filter(is_long_book, BOOKS)))

print(half_price_book)