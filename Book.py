class Book:
    def __init__(self, title, author, cost):
        #initialize the attributes to the given values (the "__" indicates that the members are private and cannot be accessed outside class definition)
        self.__title = title
        self.__author = author
        self.__cost = cost

    def getTitle(self):
        #return title of the book
        return self.__title
    
    def getAuthor(self):
        #return the author of the book
        return self.__author
    
    def getCost(self):
        #return cost of the book
        return self.__cost
        
    def getInfo(self):
        #returns a string with the book's info
        #this is used manily to display the books in a list in the gui
        return f"{self.getTitle()}\nauthor: {self.getAuthor()}\ncost: {self.getCost()}\n"