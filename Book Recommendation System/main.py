import bookimport
from bookimport import lstb,lstofb,lstofa,lstofbq,lstofp
import returnbook
import borrowbook

loop='y'
while loop=='y':
    try:
        a=int(input("\n\nEnter 1 if you want to display all the books\n"
        "Enter 2 if you want to burrow book\n"
        "Enter 3 if you want to return the book\n"
        "Enter 4 if you want to exit" 
        "\n==>  "))
        if a == 1:
            showall=bookimport.display_items(lstb)
        elif a==2:
            borrowbook.borrowbook_()
        elif a==3:
            returnbook.returnbook_()
        elif a==4:
            loop='n'
    except:
        loop='y'



