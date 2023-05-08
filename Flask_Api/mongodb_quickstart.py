import mongoengine as db
import pymongo
database_name = 'Timi'
DB_URL = 'mongodb+srv://olarotimi:Dickfish1.@cluster0.elfv34i.mongodb.net/?retryWrites=true&w=majority'
db.connect(host = DB_URL)
class Book(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField()

    def to_json(self):
        return{' book_id': self.book_id,
               'name': self.name,
               'author': self.author
        }
print('Create a book')
book = Book(book_id = 1,
            name = 'a game of thrones',
            author = 'george washinton'
)
book.save()
print('\n Fetch a book')
book = Book.objects(book_id = 1).first()
print(book.to_json())
book.update(name = 'Harrypotter',
            author = 'jnnejj')
book = Book(book_id = 2,
            name = 'the alchemist',
            author = 'paulocoelho')
book.save()
print('\n fetch all books')
books = []
for book in books:
    books.append(book.to_json())
print(books)