Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Mahardhika Bathiarto Dim Zarita"
>>> NIM = 134
>>> Tinggi = 1.68
>>> Berat = 57
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type (Aku)
<class 'tuple'>
>>> ##this command to know what is the type of Aku, Why the python print <calss 'tuple'> ? because Aku is type tuple.
>>> Aku [0]
2000
>>> ##this command call word in the tuple. why just 2000 ? why not the other ? because in tuple the row of object and it is start (0,1,2,...),if you write Aku[0] so the python print 2000.
>>> a = NIM % 4 ; Aku [a]
1.68
>>> ##this command slice word in the tuple. why 1.68 ? because value of a is 2. so Aku[a] call the row 2 on the Aku is Tinggi.
>>> type (Aku[a])
<class 'float'>
>>> ##this command to know what is type of Aku[a], type is float because value Aku[a] is 1,68.
>>> Aku[a:4]
(1.68, 134)
>>> ##this command slice word in the tuple. why 1.68 and 134 ? because value of Aku [a:4] is Tinggi and NIM.so the python print 1.68,134.
>>> type(Aku[4])
<class 'str'>
>>> ##this command to know what is type of Aku[4]. why class string ? because in type Aku[4] is Nama. so value nama is "Mahardhika Bathiarto Dim Zarita", it's type string.
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> ##because tuple element is can not be changed
>>> type(Data)
<class 'list'>
>>> ##this command to know what is the type of Data.
>>> type(Data[4])
<class 'str'>
>>> ##this command to know what is type of Data[4]. because in the Data[4] is Nama, so the python print type is class 'str'.
>>> Data[4][5]
'd'
>>> ##because there is d in fifth object.
>>> Data[4][a:6]
'hard'
>>> ##because Data[4] is nama, and [a:6] is value of a and then slice "Ma", so started by h until d.it's "hard".
>>> Data[0] = 'ok'; Data
['ok', 57, 1.68, 134, 'Mahardhika Bathiarto Dim Zarita']
>>> ##because the first object already to changed with 'ok'.
>>> Data[-a]
134
>>> ##because the second last in the Data is NIM.
>>> range(a)
range(0, 2)
>>> ##because in the "a" data there is only 2 object.
