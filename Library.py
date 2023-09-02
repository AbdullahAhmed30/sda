import json
from Book import Book
from Section import Section

class Library:
    def __init__(self, profit, title="maktabet eleman"):
        #initialize the attributes to the given values (the "__" indicates that the members are private and cannot be accessed outside class definition)
        self.__title = title
        self.__sections = [] #list of section objects
        self.__profit = profit

        #read data from the json file the data will be read into a python dict
        with open("books.json", 'r') as f:
            data = json.load(f)

        #creates an empty dict
        sections = {}

        #use indexing to extract data about the books and create book objects from the dict obtained from reading the json file
        for bookTitle, bookData in data.items():
            bookAuthor = bookData['author']
            bookCost = bookData['cost']
            sectionTitle = bookData['section']
            book = Book(bookTitle, bookAuthor, bookCost)

            #if the section is not in the dict, it is added as a key and the value is an empty list then append the book created to this list
            if sectionTitle not in sections:
                sections[sectionTitle] = []

            sections[sectionTitle].append(book)

        #iterate in the dict and creates section objects with the corresponding books list, and add it to the sections list of the library class
        for sectionTitle, books in sections.items():
            section = Section(sectionTitle, books)
            self.__sections.append(section)


    def addSection(self, section):
        #adds book to the list of books
        self.__sections.append(section)

    def searchBookByTitle(self, title):
        #search for a book in all sections given its title
        #it calls the searchBookByTitle from the section class to search for the book in each section in the sections list, if the book isn't found the function returns None
        #x[0][0] = book, x[0][1] = section's title
        for i in self.__sections:
            if(i.searchBookByTitle(title)) != None:
                return i.searchBookByTitle(title)
            
        return None
            

    def searchBookByAuthor(self, author):
        #search for a book in all sections given its author
        #it calls the searchBookByAuthor from the section class to search for the book in each section in the sections list, if the book isn't found the function returns None
        #x[][0] = book, x[][1] = section's title
        for i in self.__sections:
            if(i.searchBookByAuthor(author)) != None:
                return i.searchBookByAuthor(author)
            
        return None

    def sellaBook(self, title):
        #deletes a book by searching for it by calling the searchBookByTitle method on each section in the sections list, if the book is found, the cost is added to the profit of the library and then the book is deleted by calling deleteBook method on the list where the book was found
        for i in self.__sections:
            if(i.searchBookByTitle(title)) != None:
                self.__profit += (i.searchBookByTitle(title))[0][0].getCost()
                i.deleteBook(title)
                return



    def getProfit(self):
        #returns the profit of the library
        return self.__profit
    
    def getTitle(self):
        #returns the title of the library
        return self.__title
    
    def getSections(self):
        #return the list of sections
        return self.__sections
   