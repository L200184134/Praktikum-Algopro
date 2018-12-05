##Kegiatan 2
file = open ("L200184134","w")
file.write ("L200184134 \n")
file.write ("12/08/2000 \n")
file.write ("MAHARDHIKA BATHIARTO DIM ZARITA \n")
file.write ("BANDUNG")
file.close ()

file = open ('L200184134','r')
x = file.readlines()
print (x[2])
print (x[3]+ ','+ x[1])
print (x[0])
file.close()


## Kegiatan 3
import shelve

file = open ("L200184134","r")
NIM = file.readline()
BORN = file.readline()
NAME = file.readline()
CITY = file.readline()

file = shelve.open ("MAHARDHIKA BATHIARTO DIM ZARITA")
file ["BIOGRAFI"] = [NIM, BORN , NAME, CITY]
file.close()
