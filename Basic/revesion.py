# a=eval(input("Enter first number : "))
# b=eval(input("Enter second number  : "))
# c=eval(input("Enter third number : "))
# if a>b:
#     if a>c:
#         print("A is greater")
#     else:
#         print("C is greater")
# else :
#     if b>c:
#         print("B is greater") 
#     else:
#         print("C is greater")               



# if a>b:
#     print("A")
# if b>c:
#     print("B")    
# if c>a:
#     print("C")
# if c>b:
#     print("D")
# else:
#     print("E")    


# sum=0
# for i in range(1,11):
#     sum=sum+i
# print("Sum : ",sum)    

# n=int(input("Enter number : "))
# for i in range (1,11):
#     print(n*i)

# loop with string

# a="JAAT SAAB"
# for i in a:
#     print(i)


# a="Hello I am learning python"
# count=0
# for i in a:
#     if i == "a":
#         count=count+1
# print(count)        

# even number
# i=1
# while i<=100:
#     print(i)
#     i=i+2

# i=1
# while i<=100:
#     if i%2==0:
#         print(i)
#     i=i+1  


# while True:
#     print("A")    

# i=0
# while i<=99:
#     if i==3:
#         break
#     else:
#         print(i)
#     i=i+1    

#rev 
# i=100
# while i>0:
#     if i%2!=0:
#         print(i)
#     i=i-1    


# i=99
# while i>0:
#     print(i)
#     i=i-2    



#------------> Functions <------------
# 1. TNRN ,  2. TSRN , 3.TNRS , 4.TSRS
 
#Take Nothing Return Nothing

# def add():
#     a=eval(input("Enter first number : "))
#     b=eval(input("Enter second number : "))
#     print("Sum : ",a+b)
# add()    

# def records():
#     n=input("Enter your name : ")
#     print("Name : ",n)
# records()    

# def odd_even():
#     n=eval(input("Enter number : "))
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")    
# odd_even()        


# Take Something Return Nothing

# def record(n):
#     print("Name : ",n)
# n=input("Enter Name : ")
# record(n)    
# print("Take Something Return Nothing")
# def add(a,b):
    
#     print("Sum : ",a+b)
# a=eval(input("Enter first number : "))
# b=eval(input("Enter second number : "))
# add(a,b)    


# # Take Nothing Return Something


# def add():
#     a=eval(input("Enter first number : "))
#     b=eval(input("Enter second number : "))
#     return a+b
# z=add()
# print("Sum : ",z)



# Take Something Return Something 


# def add(a,b):
#     return a+b
# a=eval(input("Enter first number : "))
# b=eval(input("Enter second number : "))
# z=add(a,b) # call by value
# print("Sum : ",z)
