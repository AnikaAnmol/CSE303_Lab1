#!/usr/bin/env python
# coding: utf-8

# 1:


a= int(input("A:"))
b= int(input("B:"))

product = a*b
sumOfProduct = a+b

if( product > 1000 ):
    print(sumOfProduct)
else:
    print(product)


# 2:


rad = int (input("radius:"))

area = 3.1416 *rad

parameter = 2*area

print("Area:", area)
print("Parameter: 2", parameter)


# 3:


P = int(input("Enter the pricciple amount: "))
R = float(input("Enter the interest rate: "))
T = int(input("ENter the time(in year): "))

a= 1 + R/100
b= a**T

def compund_interest_2019_1_60_210(P,R,T):
    A = P*(b)
    return A

A = compund_interest_2019_1_60_210(P, R, T)

print (A)


# 4:


N= int(input("The Value Of N :"))

sum = 0

for i in range(1, N + 1, 1):
    sum = sum + (i*i)

print("The value of the series: ", sum)


# 5:


def prime_2019_1_60_210(n):
    if (n==1):
        return False

    elif (n==2):
        return True;
    
    else:
        for x in range(2, n):
            if(n % x==0):
                return False
        return True   

n = int(input("Enter a number: "))         
print(prime_2019_1_60_210(n))


# 6:


N = int(input("Enter Number:"))
f1=0
f2=1
for i in range(2,N):
    f = f1+f2
    f1 = f2
    f2 = f
print("The Fibonacci number is:",f2)


# 7:


list = [0,1,2,3,4,5,6,7,8,9,10,50,100]
s = 0
for i in range (0, len(list)):
    s = s + list[i]
print("Sum of the list is:",s)


# 8:


Even_Sum = 0
NumList = [19, 6, 7, 12, 15]

length = len(NumList)
for i in range(length):
    if(NumList[i] % 2 == 0):
        Even_Sum = Even_Sum + NumList[i]

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)


# 9:


def largest_number_2019_1_60_210(list):
    max=-9999999
    for i in range(0, len(list)):
        if(list[i]>max):
            max = list[i]
    return max
def smallest_number_2019_1_60_210(list):
    min=9999999
    for i in range(0, len(list)):
        if(list[i]<min):
            min = list[i]
    return min
list=[1,2,3,4,5,6,7,8,9,50]
print("Largest_number is :",largest_number_2019_1_60_210(list))
print("Smallest_number is :",smallest_number_2019_1_60_210(list))


# 10:


num_lst = [11, 22, 44, 45, 99]
 
mx= max(num_lst[0], num_lst[1])
secondmax= min(num_lst[0], num_lst[1])

n = len(num_lst)

for i in range(2, n):
    if num_lst[i] > mx:
        secondmax= mx
        mx= num_lst[i]
        
    elif num_lst[i] > secondmax and         mx != num_lst[i]:
        secondmax= num_lst[i]
 
print("Second highest number is : ",      str(secondmax))


# 11:


s = input("Enter a String:")
n = int(input("Enter a number  less than  string: "))

a = s[n-1:0]
b = s[n: ]

print("New String is ", a+b)


# 12:


string  = input("Enter a String: ")

sub_string = 'CSE303'
print(sub_string)

count = 0
sub_len=len(sub_string)

for i in range(len(string)):
    if string[i:i+sub_len] == sub_string:
        count += 1
print (count)


# 13:


a = input("Enter a String: ")
n = int(input("Enter the Integer: "))
print(a[n+1:])


# 14:


def palindrome_checker_2019_1_60_210(A):
       if A == A[::-1]:
         return True
A = input("Enter word: ")
if palindrome_checker_2019_1_60_210(A)==True:
          print(A,"is a palindrome")
else:
    print(A,"is not a palindrome")


# 15:


list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,2,3,4,5,6,7,8,9,10]
newlist=[]
for i in range(0,len(list1)):
    x=list1[i]
    if(x%2!=0):
        newlist.append(x)
for i in range(0,len(list2)):
    y=list2[i]
    if(y%2==0):
        newlist.append(y)
print(newlist)







