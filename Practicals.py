# Q1
for i in range (1,5):
    for j in range (i,0,-1):
        print(j,end="")
    print()    
    

#Leappyear
Year=int(input('Enter the Year: '))
if Year%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")
    

import math
x=0
while x<10:
    print(f"Sin is {math.sin(x)}, Cos is{math.cos(x)}, Tan is {math.tan(x)}")
    x=x+0.2

#Factorial
    def Factorial(n):
    if n==0 or n==1:
        return 1
    return n*Factorial(n-1)
a=Factorial(10)
print(a)

#Reverse
s=input("Enter string ")
s=s.lower()
a=(s[::-1])
print(a)


#Prime
Num=int(input("Enter the number u want to chk: "))
if Num>1:
    for i in range(2,int(Num/2)+1):
        if Num%i==0: 
            print(Num,"Not a prime")
            break
    else:
        print(Num, "Is a Prime")
else:
    print('Not a Prime')
    
   
  #Dictionary Cube
    d=dict()
for x in range(1,5+1):
    d[x]=x**3
print(d)  


#Lcm
num1=int(input("Enter the first number: "))
num2=int(input("Enter the Second number: "))
maxnum=max(num1,num2)
while True:
    if maxnum%num1==0 and maxnum%num2==0:
        break
    maxnum=maxnum+1
print(f"Lcm of {num1} and {num2} is {maxnum}") 



