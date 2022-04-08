# CREATE LIBRARY CLASS
# DISPLAY BOOK
# LEND BOOK - (WHO OWNS BOOK IF NOT PRESENT)
# ADD BOOK
# RETURN BOOK
# HARRYLIBRARY = LIBRARY(LISTOFBOOKS,LIBRARYNAME)
# DICIONARY (LIST OF BOOKS NAME)
# CREATE A MAIN FUNCTION ANDS RUN AN INFINITE LOOP
# USERS FOR THEIR INPUT

class Library:

    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}


    def displaybooks(self):
        print(f'We have following books in our library : {self.booklist} ')
        for books in self.booklist:
            print(books)

    def lendbooks(self):
        if books not in self.lendDict.keys():
            self.lendDict.update({books:User})
            print('Book database has been updated. You van take book now.')
        else:
            print('Book being used by {self.lendDict[book]}')

    def addbooks(self):
        self.booklist.append(books)
        print('Book has been added to list.')

    def returnbooks(self):
        self.booklist.remove(books)
        print('Book has been returned.')

if __name__ == "__main__":

    # book = Book("Sherlock Holmes","Abu",85)
    # bookList= []
    # bookList.append(book)
    parag = Library(['QQQ'],"Verma")

    while(True):
        print('WELCOME TO LIBRARY!!!')
        print("CHOOSE OPTIONS : \n 1. Display Books \n 2. Lend Books \n 3. Add Books \n 4. Return Books \n 5.Exit" )

        user_input = int(input("Enter your choice : "))

        if user_input == 1:

            parag.displaybooks()

        elif user_input == 2:

            books = input('Enter books name : ')
            User = input('Enter your Name : ')

            parag.lendbooks()

        elif user_input == 3:
            books = input("Enter the name of book you want to add : ")
            parag.addbooks()

        elif user_input == 4:
            books = input("Enter the name of book you want to return : ")
            parag.returnbooks()

        elif user_input == 5:
            print('Libary is closed now')
            exit()

        else:
            print("Invalid Option ")

        print("Enter q to quit or c to continue : ")
        while(user_input != 'q' and user_input != 'c'):
            user_input = input()
            if user_input == "q":
                exit()

            elif user_input == "c":
                continue




