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
