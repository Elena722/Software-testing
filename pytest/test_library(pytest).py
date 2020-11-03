import pytest
from library import Book
from library import Library

class TestBook():
    @pytest.mark.BookTest
    def test_init(self):
        self.b = Book('Django', 'Elena Santasheva')
        assert self.b.title == 'Django'
        assert self.b.copies == 1

    @pytest.mark.BookTest
    def test_borrow(self):
        self.b = Book('Django', 'Elena Santasheva')
        # self.b.borrow()
        # self.assertEqual(self.b.borrow(), 'You are unable to borrow this book, sorry!')
        assert self.b.borrow() == 'You have borrowed "Django" by Elena Santasheva'
        assert self.b.is_available() is False  # after borrow -> False (self.available-=1)
        assert self.b.pretty_name() == '"Django" by Elena Santasheva'

    @pytest.mark.BookTest
    def test_return_book(self):
        self.b = Book('Django', 'Elena Santasheva')
        assert self.b.return_book() == 'This is impossible! All the copies are already there.'
        assert self.b.is_available() is True  # after return -> True (self.available += 1)

class TestLibrary():

    def setup(self):
        self.books_by_title = {}
        assert self.books_by_title == {}
        self.b = Book('Django', 'Elena Santasheva')
        self.l = Library()

    @pytest.mark.LibraryTest
    def test_add_book(self):
        self.l.add_book(self.b)
        assert self.l.books_by_title[self.b.title] == self.b  #self.object.param

    @pytest.mark.LibraryTest
    def test_remove_book(self):
        self.l.remove_book(self.b)
        assert 'Django' not in self.l.books_by_title  # after remove_book

    @pytest.mark.LibraryTest
    def test_check_book_status(self):
        self.l.add_book(self.b)
        self.l.check_book_status(self.b.title)
        assert self.b.title in self.l.books_by_title
        assert self.l.books_by_title[self.b.title].is_available() is True

    @pytest.mark.LibraryTest
    def test_borrow(self):
        self.l.add_book(self.b)
        self.l.remove_book(self.b)
        assert self.l.borrow('Django') == 'We do not have Django. Try something else.'

    @pytest.mark.LibraryTest
    def test_return_book(self):
        self.l.add_book(self.b)
        self.l.remove_book(self.b)
        assert self.l.return_book('Django') == 'We do not have Django. Try something else.'

