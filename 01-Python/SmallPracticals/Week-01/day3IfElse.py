
# Theory of Day 3 is in https://docs.google.com/document/d/1oeeQf_OkqgxglbDB5BxAp1POCwjxTRgMUObAsZACk1Y/edit?tab=t.faei58z2v1us

firstInput=int(input("Enter Some Number"))
secondInput=int(input("Enter Another Number"))
thirdInput=int(input("Enter Third Number"))
username=input("Enter Your Name")
password=input("Enter Your Password")

Username="Gaurav"
Password="1234"

if firstInput > 0:
    print("Number is Positive")
elif firstInput < 0:
    print("Number is Negative")
else:
    print("Number is Zero") 



if firstInput % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


if firstInput > secondInput:
    print("First Number is Greater")
elif firstInput < secondInput:
    print("Second Number is Greater")
else:
    print("Both Numbers are Equal")


if firstInput > secondInput:
    if firstInput > thirdInput:
        print("First Number is Big ")
    else:
        print("thirdNumber is greater")
elif firstInput == secondInput:
    if firstInput > thirdInput:
        print("both first and second are greater")
    elif firstInput == thirdInput:
        print("All are equal")
    else:
        print("thirdNumber is greater")
else:
    if secondInput>thirdInput:
        print("second number is greater")
    elif secondInput == thirdInput:
        print("All are equal")
    else:
        print("thirdNumber is greater")



if username == Username and password == Password:
    print("Login Successful")
else:
    print("Login Failed")

