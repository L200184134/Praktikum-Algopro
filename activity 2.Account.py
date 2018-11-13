## Program Akun
## Dibuat Oleh Mahardhika Bathiarto Dim Zarita L200184134
import random
angka_random = random.randint(0,1000)
Nama = 'Mahardhika Bathiarto Dim Zarita'
TanggalLahir='12 Agustus 2000'
Nama_Singkat = Nama[0] +'.'+ Nama[11] +'.'+ Nama[21]+'.'+ Nama[25:31]
Username = Nama[0]+TanggalLahir[0:2]+TanggalLahir[11:15]
Password = Nama[0:3]+str(angka_random)
