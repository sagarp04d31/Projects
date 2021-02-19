
lstb=[]
file=open("text","r")
content=file.readlines()
for each_line in range (len(content)):
    lstb.append(content[each_line].replace("\n","").split(","))
 

lstofb=[]
lstofa=[]
lstofbq=[]
lstofp=[]


for i in range (len(lstb)):
    lstofb.append(lstb[i][1])

for i in range (len(lstb)):
    lstofa.append(lstb[i][2])

for i in range (len(lstb)):
    lstofbq.append(lstb[i][3])

for i in range (len(lstb)):
    lstofp.append(lstb[i][4])



def enumerate_b():
    for j,books in enumerate(lstofb,start=1):
        print(j,books)





def display_items(store):
    print("S.No.\t\tName of the Book\t\tAuthor's name\t\tBook quantity\t\tPrice")
    print("_____________________________________________________________________________________________________________")
    for i in range(len(store)):
        for j in range(len(store[i])):
            print(store[i][j],end="\t\t\t")
        print("\n")



#Record













