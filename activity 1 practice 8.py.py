Dictionary = {"NIM" : "L200184134",
     "Name" : "Mahardhika Bathiarto Dim Zarita",
     "Address" : "Perum Panorama Indah Blok H1. no.19",
     "Post_Code" : "41117",
     "no.HP" : "087778953481",
     "Instagram" : "mahardhikbdz",
     "Email" : "mahardhika120800@gmail.com"}

print("""
option available:
b to show this help
N to show NIM
a to show Name
A to show Address
K to show Post Code
S to show no.HP
R to show Instagram
G to show Email
k Out
""")
k = "Thank you"
M = input ("your choice : ")
while M != "k" :
     if M == "N" :
        print (Dictionary["NIM"])
        print("")
        M = input ("your choice : ")
     elif M == "a" :
        print (Dictionary["Name"])
        print ("")
        M = input ("your choice : ")
     elif M == "A" :
        print (Dictionary["Address"])
        print("")
        M = input ("your choice : ")
     elif M == "K" :
        print (Dictionary["Post_Code"])
        print ("")
        M = input ("your choice : ")
     elif M == "S" :
        print (Dictionary["no.HP"])
        print("")
        M = input ("your choice : ")
     elif M == "R" :
        print (Dictionary["Instagram"])
        print ("")
        M = input ("your choice : ")
     elif M == "G" :
        print (Dictionary["Email"])
        print("")
        M = input ("your choice : ")
     elif M == "b":
        print ("""
option available :
b to show this help
N to show NIM
a to show Name
A to show Address
K to show Post Code
S to show no.HP
R to show Instagram
G to show Email
k Out
""")

        print ("")
        M = input ("your choice : ")
     else : 
        print ("it is not definded")
        print ("")
        M = input ("your choice : ")
print (k)
