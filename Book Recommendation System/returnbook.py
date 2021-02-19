import datetime
import bookimport
from bookimport import lstb,lstofb,lstofa,lstofbq,lstofp
from record import name
def returnBook(l1,sno):
    l1[int(sno-1)][3] = str(int(l1[int(sno-1)][3])+1)
    print("The Quantity of a book has been increased to",l1[int(sno-1)][3])
    file = open("text","w")
    for i in l1:
        i = ','.join(i)
        file.write(i)
        file.write('\n')
    file.close()


def returnrecord(username,lst):
    fh = open("returnrecord.txt", "a")
    fh.write('\n\n\n')
    fh.write("#########################################")
    fh.write("\n\n\n")
    fh.write('Customer Name = ')
    fh.write(username)
    fh.write("\n")
    fh.write("Book name = ")
    for i in lst:
        fh.write(i)
    fh.write("\n")
    fh.write("Returned date = ")
    fh.write(str(datetime.date.today()))
    fh.write('\nReturned time = ')
    fh.write(str(datetime.datetime.now().hour))
    fh.write(':')
    fh.write(str(datetime.datetime.now().minute))
    fh.write("\n")
    fh.write('Price of the book = ')
    #fh.write(str(lst[int(SN)][4]))  # price
    fh.write("\n")
    fh.close()



def returnbook_():
        bookimport.enumerate_b()
        print()
        lstofrb=[]
        raks=1
        rask=int(input("Enter how many books you have to return "))
        while raks<=rask:
            r=int(input("Enter which book you want to return "))
            try:
                print('You have returned book named "',lstofb[r-1],'" written by',lstofa[r-1])
                returnBook(lstb,r)
                lstofrb.append(lstofb[r-1])
                print('\n\n')
            except:
                print("You have enter wrong book no.")
            if raks==rask:
                raks+=rask
                #returnrecord(name, lstb)
            raks+=1
        returnrecord(name, lstofrb)