'''
Created on 31/07/2013

@author: luke

IDoes the ISBN-13 have any meaning imbedded in the numbers?
    The five parts of an ISBN are as follows:
    1. The current ISBN-13 will be prefixed by "978"
    2. Group or country identifier which identifies a national or geographic grouping of publishers;
    3. Publisher identifier which identifies a particular publisher within a group;
    4. Title identifier which identifies a particular title or edition of a title;
    5. Check digit is the single digit at the end of the ISBN which validates the ISBN.
'''
import unittest
from library_catalog import Book, Library

class TestBook(unittest.TestCase):
    """
    A book should have a title, an ISBN, an author, a genre
    """
    
    def testInit(self):
        """
        On creation a book should have a title,
        an ISBN, an author, and a genre
        """
        self._book      = Book(title="Book Tests", isbn="000011112543",
                           author="Book Writer", genre="Educational",)
        self._class_vars= vars(self._book)

    def testTitle(self):
        def set_title(title):
            self._book.title    = title
        """
        A book should have a title when it is created;
        the title of a book should not be able to change
        as this would imply a new book has been created
        """
        
        title       = '_Book__title'
        # ensure book has a title
        self.assertIn(title,self._class_vars)
        self.assertNotEqual(self._class_vars[title],'','Expected legitimate title')
        # test if setting title fails
        self.assertRaises(AttributeError,set_title('should_fail'))
        
    def testISBN(self):
        def set_isbn(num):
            self._book.isbn     = num
        """
        An ISBN number is 13 numbers long
        A book should have an ISBN when created
        the ISBN of a book should not be able to change
        """
        isbn        = '_Book__isbn'
        isbn_num    = "000011112543"
        self.assertIn(isbn,self._class_vars)
        self.assertEqual(self._class_vars[isbn],isbn_num)
        self.assertRaises(AttributeError,set_isbn('someNumber'))
        self.assertEqual(len(self._class_vars[isbn]),13)
        # ISBN should be 13 chars long
        self.assertRaises(AttributeError,Book("title","123456789","author","genre"))
        
    def testAuthor(self):
        def set_author(author):
            self._book.author   = author
        """
        A book should have an author upon creation
        the author of a book should not be able to change
        """
        author      = '_Book__author'
        self.assertIn(author,self._class_vars)
        self.assertNotEqual(self._class_vars[author],'')
        self.assertRaises(AttributeError,set_author('fail'))
        
class TestLibrary(unittest.TestCase):        
    """
    A library should have a listing of all books the library owns;
    the books available for hire; the books that are currently being
    hired; the ability to check in and check out books; the ability
    to add/remove books from the library permanently.
    """
    _library    = Library()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()