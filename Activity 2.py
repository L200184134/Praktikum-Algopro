Isi = input ("input your password :")
if Isi == "Mahardhika" :
    print ("you have succesfully login ")
else :
    Isi = input ("Sorry, password is wrong, input your password :")
    if Isi == "Mahardhika":
        print ("You have succesfully login")
    else :
        Isi = input ("Sorry, password is wrong, input your password :")
        if Isi == "Mahardhika":
            print ("You have succesfully login")
        else :
            print ("You have try your password until three times, your access is denied")
