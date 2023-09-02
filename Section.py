class Section:
    def __init__(self, title, books):
        #initialize the attributes to the given values (the "__" indicates that the members are private and cannot be accessed outside class definition)
        self.__title = title
        self.__books = books #list of book objects


    def getTitle(self):
        #return the title of the section
        return self.__title
    
    def getBooks(self):
        #return the list of books of the section
        return self.__books
    

    def addBook(self, book):
        #adds book to the list of books
        self.__books.append(book)


    def searchBookByTitle(self, title):
        #searches for a book given its title, it iterates on the books list and checks if the given title matches the title of the book
        #if the book is found it returns the book if not the function retunrs None
        result = []
        for i in self.__books:
            if i.getTitle() == title:
                result.append([i, self.__title])
                return result
            
        return None
    

    def searchBookByAuthor(self, author):
        #searches for a book given its author, it iterates on the books list and checks if the given author name matches the author of the book
        #if a book is found it adds it to a list of resutls and returns the final array if none is found the function retunrs None
        results = []
        for i in self.__books:
            if i.getAuthor() == author:
                results.append([i, self.__title])

        if results == []:
            return None
        
        else:
            return results
        
    
    def deleteBook(self, title):
        #deletes a book given its title, if the book is found, its removed from the list of books, if not the function returns None
        for i in self.__books:
            if i.getTitle() == title:
                self.__books.remove(i)
                return i

        return None


    def showBooks(self):
        #prints the details of the all the books in the books list
        #it also returns a list of strings containing the data of each book, this will be used in the gui
        bookData = []
        for i in self.__books:
            bookData.append(f"{i.getTitle()}\nauthor: {i.getAuthor()} \ncost: {i.getCost()} \nsection: {self.__title}")
            # print(f"{i.getTitle()} \nauthor: {i.getAuthor()} \ncost: {i.getCost()} \nsection: {self.__title}\n\n")
        
        return bookData

