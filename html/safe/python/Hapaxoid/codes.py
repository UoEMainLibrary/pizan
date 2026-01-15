'''
This module provides some utilities to the other parts of the
Hapaxoid application for the handling of the page numbering
convention found in the Queen's Manuscript.

Hapaxoid was written by Tommy Herbert for Charlie Mansfield and Jim
Laidlaw.  Please see readme.txt for an overview.

Version 1.0
15th August 2008
'''

# Import the standard Python library that deals with regular
# expressions.
import re
# An ordered list of the books in the manuscript.
books = ['PREL', 'TABL', 'PROL', 'CEBA', 'VIRL', 'BAEF', 'LAY1',
         'LAY2', 'ROND', 'JEUX', 'AUBA', 'CMP2', 'EABA', 'DAMO',
         'CMP1', '2AMA', '3JUG', 'POIS', 'OTEA', 'DVAL', 'DVAB',
         'DVAV', 'DVAR', 'DVAC', 'CHLE', 'PAST', 'EROS', 'EUST',
         'ORNS', 'PMOR', 'EMOR', 'ORND', '15JO', 'PRUD', 'CDAM',
         'CBAD', 'LAYD']

def getBooks(dataFilename):
   '''This is how I produced my list of books.  The function isn't
   called by anything in Hapaxoid, but I thought I might as well
   leave it in.'''
   books = []
   dataFile = open(dataFilename, 'r')
   line = dataFile.readline()
   while line != '':
      tokens = line.split()
      if len(tokens) > 0:
         code = tokens[0]
         # strip the brackets
         code = code[1:-1]
         [book, line] = code.split('.')
         if not book in books:
            books.append(book)
      line = dataFile.readline()
   dataFile.close()
   return books

def conforms(code):
   '''Checks that a given string is a legal example of a
   page-numbering code.'''
   matchResult = re.match('\[[\dA-Z]{4}\.\d{3}[rva-d]:\d\d\]\Z',
                          code)
   return matchResult != None

def comparePages(pageCode1, pageCode2):
   '''Returns -1 if the first code precedes the second in the
   manuscript, 1 if the reverse is the case, and 0 if they refer to
   the same column.  The implementation of this function is overkill,
   because it dates from before I realised you don't need the book
   name to establish the page number.  Still works, though.'''
   [book1, page1] = pageCode1.split('.')
   [book2, page2] = pageCode2.split('.')
   if book1 == book2:
      if page1[:-1] == page2[:-1]:
         letter1 = page1[-1]
         letter2 = page2[-1]
         if letter1 == letter2:
            return 0
         else:
            order = 'rabvcd'
            index1 = order.index(letter1)
            index2 = order.index(letter2)
            return cmp(index1, index2)
      else:
         return cmp(page1, page2)
   else:
      index1 = books.index(book1)
      index2 = books.index(book2)
      return cmp(index1, index2)
