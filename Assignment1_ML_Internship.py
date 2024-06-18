#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1
a = int(input("Enter num 1:"))
b = int(input("Enter num 2:"))

print("Sum = ", a+b)


# In[4]:


#Q2

num = int(input("Enter the number: "))

if num/2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# In[8]:


#Q3

num = int(input("Enter the number: "))
prod = 1
while num>0:
    prod = prod*num
    num = num - 1

print("Factorial is: ", prod)


# In[9]:


#Q4

name = input("Please type your name: ")
print("Hello! You're welcome here, ", name)


# In[12]:


#Q5 

str1 = input("Please enter a string: ")

f = open("test.txt", "w")
f.write(str1)
f.close()
f = open("test.txt", "r")
str2 = f.read()
print(str2)
print("Whole file has been read.")
f.close()


# In[13]:


#Q6

f = open("test.txt", "r")
str2 = f.read()
print(str2)
print("Whole file has been read.")
f.close()


# In[16]:


#Q7

str1 = input("Enter string: ")
a = 0
for i in str1:
    a = a+1
print("Length = ", a)


# In[18]:


#Q8

a = "roboto"

b = "font"

print(a+b)


# In[ ]:


#Q9

str1 = input("Enter the main string: ")

substr = input("Enter the string to be searched: ")



# In[19]:


#Q10

str1 = input("Enter string:")
s2 = str1.upper()
print(s2)


# In[7]:


#Q11

n1 = 0
n2 = 1
t = int(input("Enter the number of fibonacci numbers you want: "))

fsum = 0

for i in range(t):
    print(fsum)    
    fsum = n1+n2
    n1 = n2
    n2 = fsum
    
print("Sum of Fibonacci numbers is: ", fsum)


# In[11]:


#Q12

t = int(input("Enter number please: "))
dsum = 0
while t>0:
    remainder = int(t%10)
    dsum = dsum + remainder
    
    t = t/10

print("Sum of digits:", dsum)    


# In[13]:


#Q13

useryear = int(input("Enter birthyear: "))

age = 2024-useryear

print("Age:", age)


# In[ ]:


#Q14



# In[18]:


#Q15

from csv import DictReader

with open("test.csv", mode = "w") as csvfile:
    fieldnames = ["col1", "col2"]
    writer = csv.DictWriter(csvfile, fieldnames)
    
    writer.writeheader()
    writer.writerow({"col1":"hello", "col2":"new"})
    writer.writerow({"col1":"hello", "col2":"new"})
    writer.writerow({"col1":"hello", "col2":"new"})
    writer.writerow({"col1":"hello", "col2":"new"})
    
csvfile.close()

reader = open("test.csv", "r")
csvreader = DictReader(reader)
for row in csvreader:
    print(row)
    
reader.close()


# In[24]:


#Q16

mainstr = list(input("Enter the main string: "))
ctr = 0
print(mainstr)
num = len(mainstr)
i = 0
for letter in mainstr:
    ctr = 0
    for i in range(num):
        if letter == mainstr[i]:
            ctr = ctr + 1
    print("Counter for", letter, ":", ctr)


# In[25]:


#Q17

str1 = "halfui abiufbuai ia bahb faif a"

str2 = str1.title()

print(str2)


# In[ ]:


#Q18



# In[30]:


#Q19

str1 = input("Enter string: ")

for letter in str1:
    print(letter)
    if letter == ',':
        letter = " "

print("Changed:", str1)


# In[3]:


#Q20

num = []

n = int(input("Enter number of elements: "))
nsum = 0
for i in range(n):
    element = int(input("Num: "))
    nsum = nsum + element
    num.append(element)
    
print("Sum of elements:", nsum)


# In[2]:


#Q21

l1 = []

n = int(input("Enter number of elements in list: "))

for i in range(n):
    element = input("Enter anything: ")
    l1.append(element)
    
find = input("Enter the thing to be found: ")
ctr = 0

for i in range(n):
    if(find == l1[i]):
        ctr = ctr + 1

print("Frequency =", ctr)   


# In[6]:


#Q22

import sys

l1 = []

n = int(input("Enter size of list: "))

for i in range(n):
    element = int(input("Enter elements: "))
    l1.append(element)
    
min1 = sys.maxsize
max1 = -sys.maxsize - 1

for i in range(n):
    if l1[i]<min1:
        min1 = l1[i]
    if l1[i]>max1:
        max1 = l1[i]
        
print("Max element:", max1)
print("Min element:", min1)


# In[9]:


#Q23

#F = (9/5)C + 32

#C = (F - 32) * 5/9

choice = int(input("Specify which you'd like to convert: 1. C to F or 2. F to C:"))

if choice == 1:
             C = int(input("Enter temperature in celsius: "))
             F = (9/5)*C + 32
             print("Fahrenhiet result is:", F)
elif choice == 2:
             F = int(input("Enter temperature in fahrenhiet: "))
             C = (F - 32) * 5/9
             print("Celsius result is:", C)
else: 
             print("Entered invalid choice.")


# In[12]:


#Q24

choice = input("Enter operand out of these: +, -, /, * ")

if choice == "+":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("The result is:", a+b)
elif choice == "-":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("The result is:", a-b)
elif choice == "*":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("The result is:", a*b)
elif choice == "/":
    a = int(input("Enter the number to be divided: "))
    b = int(input("Enter the divisor: "))
    if b == 0:
        print("Can't perform division")
    else:
        print("The result is:", a/b)
else:
    print("You entered invalid choice")


# In[14]:


#Q25

with open("test.txt", "r") as f:
    lines = f.read()

f.close()

with open("text.txt", "w") as paste:
    paste.write(lines)
    
paste.close()

with open("text.txt", "r") as reader:
    text = reader.read()
    print(text)


# In[ ]:


#Q26

s1 = "hfauldhsfuia beaufwbo bawib ein fineaw lbawfbeuawfiawhenfkanw fcnakfa"



# In[16]:


#Q27

l1 = []

str1 = "anfoao w8r032 jfia h9a3t8h a9p8 a98 hap9o3ebn a"

for i in range(len(str1)):
    element = str1[i]
    l1.append(element)
    
print(l1)

