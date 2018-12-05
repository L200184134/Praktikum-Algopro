##Kegiatan 4
import shelve

file = shelve.open ("MAHARDHIKA BATHIARTO DIM ZARITA")
print (file["BIOGRAFI"][0])
print (file["BIOGRAFI"][1])
print (file["BIOGRAFI"][2])
print (file["BIOGRAFI"][3])
file.close()
