import datetime
class LibraryItem(object):
    def __init__(self,t,a,i):
        self.__title = t;
        self.__author__artist = a;
        self.__itemID = i;
        self.__onloan = False;
        self.__duedate = datetime.date.today();
        self.__borrowerID = 0;

    def gettitle(self):
        return (self.__title);

    def getitemID(self):
        return self.__itemID

    def borrowing(self,ID,x):
        self.__onloan = True;
        self.__duedate = self.__duedate + datetime.timedelta(weeks=3);
        self.__borrowerID = ID;
        x.updateitemsonloan(1);
    
    def returning(self,x):
        self.__onloan = False;
        self.__borrowerID = 0;
        x.updateitemsonloan(-1);

    def printdetails(self):
        print(self.__title,'; ',self.__author__artist,'; ',end = '');
        print(self.__itemID,'; ',self.__onloan,'; ',self.__duedate);
        print(self.__borrowerID);


class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i);
        self.__isrequested = False;
        self.__requestedby = [];
        
    def getisrequested(self):
        return(self.__isrequested)
    
    def setisrequested(self,x):
        self.__isrequested = True;
        self.__requestedby.append(x.getborrowername());

    def printdetails(self):
        print('Book details');
        LibraryItem.printdetails(self);
        if self.__isrequested:
            print('the book is requested by',self.__requestedby);
        else:
            print('no request');
            

class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i);
        self.__genre = "";

    def getgenre(self):
        return (self.__genre);

    def printdetails(self):
        print('Cd features:');
        LibraryItem.printdetails(self);
        print(self.__genre);
        print('')

class Borrower(object):
    def __init__(self,n,e,i):
        self.__borrowername = n;
        self.__emailaddress = e;
        self.__borrowerID = i;
        self.__itemsonloan = 0;

    def getborrowername(self):
        return self.__borrowername

    def getemailaddress(self):
        return self.__emailaddress

    def getborrowerID(self):
        return self.__borrowerID

    def getitemsonloan(self):
        return self.__itemsonloan

    def updateitemsonloan(self,i):
        self.__itemsonloan += i;
        print('borrow ',self.__itemsonloan,'time(s)');

    def printdetails(self):
        print()
        print('borrower info:')
        print(self.__borrowername,';',self.__emailaddress,';',end = '');
        print(self.__borrowerID,';',self.__itemsonloan);
        print('')
        
def DisplayMenu():
    print('');
    print('1 - Add a new borrower')
    print('2 - Add a new book')
    print('3 - Add a new CD')
    print('4 - Borrow book')
    print('5 - Return book')
    print('6 - Borrow CD')
    print('7 - Return CD')
    print('8 - Request book')
    print('9 - Print all details')
    print('99 - Exit program')
    print
    print('Enter your menu choice: ')

def main():
    finish = 0;
    B = [];
    C = [];
    Bo = [];
    B.append(Book('The Martian','AndyWeir',1));
    C.append(CD('Reputation','Taylor',1));
    Bo.append(Borrower('zhangrex','zcyrex@qq.com',1))
    while finish == 0:
        DisplayMenu();
        choice = int(input('choice: '));
        if choice == 1:
            print('Add a new borrower');
            name = input('name: ');
            email = input('email: ');
            boID = input('borrower ID: ');
            boID = int(boID);
            Bo.append(Borrower(name,email,boID));
        elif choice == 2:
            print('Add a new book');
            bookname = input('book name: ');
            author = input('author name: ');
            bookID = input('book ID: ');
            bookID = int(bookID);
            B.append(Book(bookname,author,bookID));
        elif choice == 3:
            print('Add a new CD');
            cdname = input('cd name: ');
            artist = input('artist name: ');
            cdID = input('CD ID: ');
            cdID = int(cdID);
            C.append(CD(cdname,artist,cdID));
        elif choice == 4:
            print('Borrow book');
            bookID = int(input('book ID: '));
            boID = int(input('borrower ID: '));
            bookindex = -1;
            borrowerindex = -1;
            for i in range(len(B)):
                if B[i].getitemID() == bookID:
                    bookindex = i;
                    break
            for i in range(len(Bo)):
                if Bo[i].getborrowerID() == boID:
                    borrowerindex = i;
                    break
            if bookindex == -1:
                print('Book not found');
            elif borrowerindex == -1:
                print('Borrower not found');
            else:
                B[bookindex].borrowing(boID,Bo[borrowerindex]);
        elif choice == 5:
            print('Return book');
            bookID = int(input('book ID: '));
            boID = int(input('borrower ID: '));
            bookindex = -1;
            borrowerindex = -1;
            for i in range(len(B)):
                if B[i].getitemID() == bookID:
                    bookindex = i;
                    break
            for i in range(len(Bo)):
                if Bo[i].getborrowerID() == boID:
                    borrowerindex = i;
                    break
            if bookindex == -1:
                print('Book not found');
            elif borrowerindex == -1:
                print('Borrower not found');
            else:
                B[bookindex].returning(Bo[borrowerindex]);
        elif choice == 6:
            print('Borrow CD');
            cdID = int(input('CD ID: '));
            boID = int(input('borrower ID: '));
            cdindex = -1;
            borrowerindex = -1;
            for i in range(len(C)):
                if C[i].getitemID() == cdID:
                    cdindex = i;
                    break
            for i in range(len(Bo)):
                if Bo[i].getborrowerID() == boID:
                    borrowerindex = i;
                    break
            if cdindex == -1:
                print('CD not found');
            elif borrowerindex == -1:
                print('Borrower not found');
            else:
                C[bookindex].borrowing(boID,Bo[borrowerindex]);
        elif choice == 7:
            print('Return CD');
            cdID = int(input('CD ID: '));
            boID = int(input('borrower ID: '));
            cdindex = -1;
            borrowerindex = -1;
            for i in range(len(C)):
                if C[i].getitemID() == cdID:
                    cdindex = i;
                    break
            for i in range(len(Bo)):
                if Bo[i].getborrowerID() == boID:
                    borrowerindex = i;
                    break
            if cdindex == -1:
                print('CD not found');
            elif borrowerindex == -1:
                print('Borrower not found');
            else:
                C[bookindex].returning(Bo[borrowerindex]);
        elif choice == 8:
            print('request book');
            bookID = int(input('book ID: '));
            boID = int(input('borrower ID: '));
            bookindex = -1;
            borrowerindex = -1;
            for i in range(len(B)):
                if B[i].getitemID() == bookID:
                    bookindex = i;
                    break
            for i in range(len(Bo)):
                if Bo[i].getborrowerID() == boID:
                    borrowerindex = i;
                    break
            if bookindex == -1:
                print('Book not found');
            elif borrowerindex == -1:
                print('Borrower not found');
            else:
                B[bookindex].setisrequested(Bo[borrowerindex]);

        elif choice == 9:
            print('print all details');
            for i in B:
                i.printdetails()
            for i in Bo:
                i.printdetails()
            for i in C:
                i.printdetails()
        elif choice == 99:
            finish = 1;
            print('Finish the program');
            
main()
        

