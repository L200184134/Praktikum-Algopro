def temperatureConversion(C = 0,F = 0):
    if C != 0 :
        y = ((9*C/5)+32)
        y = int(y)
        y = str(y)
        print ("Temperature "+str(C)+" Celcius the same with ",y, " Fahrenheit.")
    elif F != 0 :
        p = (5/9*(F-32))
        p = int(p)
        p = str(p)
        print ("Temperature "+str(F)+" Fahrenheit the same with ",p," Celcius.")
    else :
        print ("Temperature 0 celcius the same with 32 Fahrenheit.")
