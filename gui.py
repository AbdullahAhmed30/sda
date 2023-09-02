import PyQt5.QtWidgets as qtw
from Book import Book
from Section import Section
from Library import Library

class MainWindow(qtw.QTabWidget):
    def __init__(self):
        super().__init__()
        #create a library object to store the books
        self.__lib = Library(0)

        #title of the window will be the title of the library object
        self.setWindowTitle(self.__lib.getTitle())

        #set layout
        self.setLayout(qtw.QVBoxLayout())
        
        #resize the mainwindow
        self.resize(1200, 700)

        #add a label to view the profit of the library
        self.__label = qtw.QLabel(f"Profit = {self.__lib.getProfit()}")
        self.layout().addWidget(self.__label)


        #add a searchbar
        self.__searcText = qtw.QLineEdit()
        self.__searcText.setPlaceholderText("search")

        #add a dropdown menue to choose whether to search by title or author
        self.__searchOption = qtw.QComboBox()
        self.__searchOption.addItems(["search by title", "search by author"])

        #add a button to search for the entered text
        self.__searchButton = qtw.QPushButton("Search")
        self.__searchButton.clicked.connect(self.searchButtonAction)

        #create a hbox to arrange the widgets of the search bar horizontally then add it to the qvbox
        searchBar = qtw.QHBoxLayout()
        searchBar.addWidget(self.__searcText)
        searchBar.addWidget(self.__searchOption)
        searchBar.addWidget(self.__searchButton)
        self.layout().addLayout(searchBar)


        #add a qlist to show all the books when first launching the app
        self.__booksList = qtw.QListWidget()
        #loop to add books to the list
        for i in self.__lib.getSections():
            items = i.showBooks()
            for j in items:
                self.__booksList.addItem(j)

        self.__booksList.setSpacing(10)
        self.layout().addWidget(self.__booksList)


        #button to buy selected book
        self.__buyButton = qtw.QPushButton("buy")
        self.layout().addWidget(self.__buyButton)
        self.__buyButton.clicked.connect(self.buyButtonAction)


        #button to view all books in the library again
        self.__homeButton = qtw.QPushButton("home")
        self.layout().addWidget(self.__homeButton)
        self.__homeButton.clicked.connect(self.homeButtonAction)




        self.show()

    
    def buyButtonAction(self):
        #gets the text of the selected item, split it before the first "\n" to get the title, then passes the title to sellaBook method
        #the item is then deleted from the list
        if self.__booksList.currentItem() == None:
            return
        
        itemText = self.__booksList.currentItem().text()
        title = itemText.split("\n")[0]
        self.__lib.sellaBook(title)
        self.__booksList.takeItem(self.__booksList.row(self.__booksList.currentItem()))
        self.__label.setText(f"Profit = {self.__lib.getProfit()}")

    
    def homeButtonAction(self):
        #returns to the normal view of all the books left in the library
        self.__booksList.clear()
        for i in self.__lib.getSections():
            items = i.showBooks()
            for j in items:
                self.__booksList.addItem(j)

        self.__booksList.setSpacing(10)

    
    def searchButtonAction(self):
        #gets the text enterd in the search bar and the option of either searching by title or author and class the corresponding funciton
        text = self.__searcText.text()
        if self.__searchOption.currentText() == "search by title":
            results = self.__lib.searchBookByTitle(text)
        else:
            results = self.__lib.searchBookByAuthor(text)

        if results == None:
            return
        
        self.__booksList.clear()
        for i in results:
            item = f"{i[0].getInfo()}secion: {i[1]}"
            self.__booksList.addItem(item)
        
        








app = qtw.QApplication([])
mw = MainWindow()

app.exec_()