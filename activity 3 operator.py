Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = "Mahardhika Bathiarto Dim Zarita"
>>> ##this command put string "Mahardhika Bathiarto Dim Zarita" to the function of name, if we call it.
>>> Name
'Mahardhika Bathiarto Dim Zarita'
>>> NIM = "L200184134"
>>> ##this command put string "L200184134" to the function of NIM.so the python will print "L200184134" if we call function of NIM.
>>> NIM
'L200184134'
>>> X= "1" + NIM[7:]
>>> ##this command add a slice of NIM data (from 7th character until the end string) and to combination with "1".
>>> X
'1134'
>>> a = int(X)
>>> ##this command to change a type of NIM, from type is string to type integer.
>>> a
1134
>>> b =len (Name)
>>> ##this command to know what how many a character of Name.
>>> b
31
>>> type(a)
<class 'int'>
>>> 
>>> ## this command to know what is the type of function a.
>>> type (b)
<class 'int'>
>>> ##this command to know what is the type of function b.
>>> a/b
36.58064516129032
>>> ##this command to change value of a, divide it by value of b.
>>> a//b
36
>>> ##this command to change value of divide value of b, from float to integer
>>> 10*(a-999)
1350
>>> ##this command subtract value of a-999, and then multiply 10.
>>> b**2
961
>>> ##this command to the power of two from value of function b.
>>> a%b
18
>>> ##this command give result after dividing the value of a and b. and count the divide remainder.
>>> c = 12.5
>>> ## this command value of c.
>>> c
12.5
>>> type(c)
<class 'float'>
>>> ##this command to know what is the type of function c.
>>> a/c
90.72
>>> ##this command to make value of a divide value of c.
>>> a//c
90.0
>>> ##this command to change value of a divide value of b to simplify.
>>> a%c
9.0
>>> ##this command give result after dividing the value of a and b. and count the divide remainder.
>>> c>b
False
>>> ##this command is c not bigger from b. so the python print False.
>>> type(c > b)
<class 'bool'>
>>> ##this command for take decision.and the decision is point true and false.
>>> a > b and b > c
True
>>> ##this command stated that point a is more bigger point from b, and point b is more bigger from c.
>>> a > 1100 or b < 10
True
>>> ##this command stated that point a is more biggest from 1100, because point a is 1134. or b is smaller from 10.
>>> 
