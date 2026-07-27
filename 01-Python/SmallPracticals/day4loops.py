# # https://docs.google.com/document/d/1oeeQf_OkqgxglbDB5BxAp1POCwjxTRgMUObAsZACk1Y/edit?tab=t.gdxwe12dwbx
# for i in range(5):
#    print("Hello")


# #range(start,stop,step)
# array=[2,4,1,43,56,677,4353,65]
# for i in range(0,len(array),2):
#    print(array[i])


# #PRINT EVEN NUMBER
# for i in range(2, 21, 3):
#    print(i)


# #Print Odd NUMBER
# for i in range(1, 20, 2):
#    print(i)


# #Multiplication Table
# tableToPrint=int(input("Enter the number for which you wnt table"))
# for i in range(1,11):
#    print(i*tableToPrint)

# #Sum of first 10 numbers
# Sum = 0
# for i in range(1,11):
#     print(i)
#     Sum += i 

# print(Sum)

# #While Loop
# count=1
# while count<=5:
#   print(count);
#   count+=1

# #Continue in For loop 
# for i in range(9):
#     if(i==5):
#       continue
      
#     print(i)


# #break in For loop
# for i in range(9):
#     if(i==5):
#       break
      
#     print(i)    

# #nested for loop
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)



# #Sum of Even Numbers (1 to 100):
# sum=0
# for i in range(2,102,2):
#     print(i)
#     sum+=i
# print(sum)


# #Find the factorial of a number.
# # NumToFindFactorial=int(input("Enter any number to find factorial"))
# i=int(input("Enter number"))
# out=1
# while i>=1:
#       print(i)
#       out=i*out
#       i-=1;
# print(out)


# #Reverse counting from 10 to 1
# for i in range(10,0,-1):
#     print(i)


# number = int(input("Enter Number: "))
# count = 0

# while number > 0:
#     count += 1
#     number //= 8
#     print(number)
# print("Digits =", count)


#sum of digits of a number
# given_number = int(input("Enter a number: "))
# sum=0
# for d in str(given_number):
#     sum+=int(d)
# print("Sum of digits:", sum)   