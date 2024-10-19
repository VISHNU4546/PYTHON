# # # '''
# # # x= 1 
# # # def fun ():
# # #     global x
# # #     x= x+1



# # # fun()
# # # print(x)


# # # def f1():
# # #     global x
# # #     x += 1
# # #     print(x)


# # # x= 12
# # # f1()
# # # print("x")'''

# # # # name ="b"
# # # # d = ord(name)
# # # # print(d)

# # # x,y = int(input().split())
# # # a = input()

# # # print('type of x',type(x))
# # # print('type of y',type(y))
# # # print('type of z',type(a))


# # # x= 2.8
# # # y= float(2.8)
# # # print(type(x),type(y));

# # # # print((x))
# # # print(type(["apple","akik"]))

# # from os import *
# # from sys import *
# # from collections import *
# # from math import *

# # # p = int(input())
# # # r = float(input())
# # # y = float(input())

# # # a = int((p/100)*r*y)
# # # print(a)

# # # print(round(45.8))

# # # print(0.1+0.2 ==0.3)
# # # print(3^4)  011  xor 100 = 111


# # # for num  in range (5,15,5):
# # #      print(num, end =",")

# # # for i in range(0,2,-1):
# # #     print("Hello")

# # # n= 5
# # # while(n>0):
# # #     print(n,end = " ")
# # #     n-=1

# # i = 0
# # while i<5:
# #     if i == 2:
# #         continue
# #     else:
# #         print(i, end =" ")
# #         i+=1


# #Your code goes here

# # A = int(input())
# # evnSUm= 0
# # oddSum = 0
# # i = 0
# # while A>0:
# #     digit = A%10
# #     print(digit)
# #     if digit %2==0:

# #          evnSUm +=digit
# #     else:
# #         oddSum +=digit

# #     A = A//10

# # print(evnSUm,oddSum)
# from os import *
# from sys import *
# from collections import *
# from math import *

# def febo(n):
#   if n==0:
#       return 1

#   return n * febo(n-1)     


# n = int(input())
# print(febo(n))

# def fun(a):
#     a = a+10
#     return a

# a = 5
# fun(a)
# print(a)

# def fun(**kwa):
#     for key,value in kwa.items():
#         print(key,value,end="")

# fun(com = "jai",loc = "shreeRam")
from typing import List

def printDivisors(n: int) -> List[int]:
    i = 1
    print("ho")
    while i<n+1:
          print(i)
          if i %n ==0:
            print(i)
            List[i]
            i+=1
    
   
    return List
print(printDivisors(6))