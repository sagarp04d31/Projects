import datetime
import bookimport
from  bookimport import lstofb,lstofa,lstofp,lstb
from record import name
def borrowBook(l1,sno):
    l1[int(sno-1)][3] = str(int(l1[int(sno-1)][3])-1)
    print()
    print("The Quantity of a book has been decreased to",l1[int(sno-1)][3])
    file = open("text","w")
    for i in l1:
        i = ','.join(i)
        file.write(i)
        file.write('\n')
    file.close()

def borrowrecord(username,lst):
    fh = open("borrowrecord.txt", "a")
    fh.write('\n\n\n')
    fh.write("#########################################")
    fh.write("\n\n\n")
    fh.write('Customer Name = ')
    fh.write(username)
    fh.write("\n")
    fh.write("Book name = ")
    for i in lst:
        fh.write(i)
        fh.write('\t')
    fh.write("\n")
    fh.write("Borrowed date = ")
    fh.write(str(datetime.date.today()))
    fh.write('\nBorrowed time = ')
    fh.write(str(datetime.datetime.now().hour))
    fh.write(':')
    fh.write(str(datetime.datetime.now().minute))
    fh.write("\n")
    fh.write('Price of the book = ')
    #fh.write(str(lst[int(SN)][4]))  # price
    fh.write("\n")
    fh.close()

def borrowbook_():
    bookimport.enumerate_b()
    print()
    num=0
    ask='y'
    lstofbb=[]
    while ask=='y':
            b=int(input("Enter which book you want to burrow "))
            try:
                print('You have borrowed book named "',lstofb[b-1],'" written by',lstofa[b-1],'and price of book is',lstofp[b-1])
                borrowBook(lstb,b)
                lstofbb.append(lstofb[b-1])
                num += 1
            except:
                print("You have entered wrong book no.")
            if num==2:
                print()
                print("You cannot burrow more than 2 books ")
                print('\n\n')
            if num==2:
                ask='n'
                #borrowrecord(name,lstb,b-1)

            if num==2:
                break
            ask1=input("Enter y if you want to burrow more books ")
            ask=ask1.lower()
    borrowrecord(name, lstofbb)