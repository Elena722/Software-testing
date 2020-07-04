import unittest
from library import Book
from library import Library

class BookTest(unittest.TestCase):
    def test_init(self):
        self.b = Book('Django', 'Elena Santasheva')
        self.assertEqual(self.b.title, 'Django')
        self.assertEqual(self.b.copies, 1)

    def test_borrow(self):
        self.b = Book('Django', 'Elena Santasheva')
        # self.b.borrow()
        # self.assertEqual(self.b.borrow(), 'You are unable to borrow this book, sorry!')
        self.assertEqual(self.b.borrow(), 'You have borrowed "Django" by Elena Santasheva')
        self.assertEqual(self.b.is_available(), False)  # after borrow -> False (self.available-=1)
        self.assertEqual(self.b.pretty_name(), '"Django" by Elena Santasheva')

    def test_return_book(self):
        self.b = Book('Django', 'Elena Santasheva')
        self.assertEqual(self.b.return_book(), 'This is impossible! All the copies are already there.')
        self.assertEqual(self.b.is_available(), True)  # after return -> True (self.available += 1)

class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.books_by_title = {}
        self.assertEqual(self.books_by_title, {})
        self.b = Book('Django', 'Elena Santasheva')
        self.l = Library()

    def test_add_book(self):
        self.l.add_book(self.b)
        self.assertEqual(self.l.books_by_title[self.b.title], self.b)  #self.object.param

    def test_remove_book(self):
        self.l.remove_book(self.b)
        self.assertFalse('Django' in self.l.books_by_title)  # after remove_book

    def test_check_book_status(self):
        self.l.add_book(self.b)
        self.l.check_book_status(self.b.title)
        self.assertTrue(self.b.title in self.l.books_by_title)
        self.assertTrue(self.l.books_by_title[self.b.title].is_available())

    def test_borrow(self):
        self.l.add_book(self.b)
        self.l.remove_book(self.b)
        self.assertEqual(self.l.borrow('Django'), 'We do not have Django. Try something else.')

    def test_return_book(self):
        self.l.add_book(self.b)
        self.l.remove_book(self.b)
        self.assertEqual(self.l.return_book('Django'), 'We do not have Django. Try something else.')


bookSuite = unittest.TestSuite(
    [
        BookTest("test_init"),
        BookTest("test_borrow"),
        BookTest("test_return_book"),
    ]
)

librarySuite = unittest.TestSuite(
    [
        LibraryTest("test_add_book"),
        LibraryTest("test_remove_book"),
        LibraryTest("test_check_book_status"),
        LibraryTest("test_borrow"),
        LibraryTest("test_return_book"),
    ]
)
