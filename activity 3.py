c = ("pagi","siang","sore","malam")
name = input ("what is your name : ")
time = float(input ("what time is it : "))
if 00.00 <=time<=11.59 :
    print ("selamat"+' '+ c[0] + ' '+name)
elif 12.00 <= time <= 14.59 :
    print ("selamat"+' '+ c[1]+' ' +name) 
elif 15.00<= time <= 17.59 :
    print ("selamat"+' '+ c[2]+' ' +name) 
elif 18.00 <= time <= 23.59 :
    print ("selamat"+' '+ c[3]+' ' +name) 