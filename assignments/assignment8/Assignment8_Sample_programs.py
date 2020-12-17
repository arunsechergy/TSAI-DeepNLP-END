#!/usr/bin/env python
# coding: utf-8

# In[7]:


# write a python class that defines a Tree and add child

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children =[]
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

t = TreeNode("Arun")
t.add_child(TreeNode("Shruthi"))


# In[63]:


# write a python function that takes two path strings and return the combined path string
import os

def path_join(PARENT_DIR, DIR):
    joined_path = os.path.join(PARENT_DIR, DIR)
    return joined_path
path_join("C:/", "DATA")


# In[78]:


# write a python function to read a text file and return the result
def read_file(filepath='test.txt'):
    with open(filepath, 'r') as file_reader:
        f_read = file_reader.read()
    return f_read
read_file()


# In[83]:


# write a python function to read a text file, if no filepath is given raise Exception
def read_file(filepath=None):
    if filepath:
        with open(filepath, 'r') as file_reader:
            f_read = file_reader.read()
        return f_read
    else:
        raise Exception("filepath not found")
read_file()


# In[87]:


# write a python program to handle exception when a given value is less than 10

def check(x):
    if x < 10:
        raise ValueError('x should not be less than 10!')
    else:
        return x
check(9)


# In[104]:


# write a python function to check if the given structure is a instance of list or dictionary
def check_insst(obj):
    if isinstance(obj, list):
        return "list"
    elif isinstance(obj, dict):
        return "dict"
    else:
        return "unknown"
   
check_insst({})


# In[102]:


# write a python function to check if the given structure is a instance of tuple or string
def check_inst_tup_str(obj):
    if isinstance(obj, set):
        return "set"
    elif isinstance(obj, tuple):
        return "tuple"
    else:
        return "unknown"
check_inst_tup_str({1})


# In[110]:


# write a python class to instantiate an object with two string attributes and write a function to return the list of attributes
class Myclass:  
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def get_attributes_list(self):  
         return [self.attr1, self.attr2]
dress = Myclass("pant","shirt")
dress.get_attributes_list()


# In[114]:


# write a python function that call another function and that function prints "Inside B"
def A():
    B()

def B():
    print("Inside B")

A()


# In[119]:


# write a python program to return the biggest character in a string (printable ascii characters)
from functools import reduce

input_str = 'tsai'
res = reduce(lambda x, y: x if ord(x) > ord(y) else y, input_str)
print(f"{res}")


# In[120]:


# write a python program to adds every 3rd number in a list
from functools import reduce
input_list = [x for x in range(10)]
res = reduce(lambda x, y: x+y, [i for idx, i in enumerate(input_list) if (idx+1)%3==0])

print(f"{res}")


# In[111]:


# write a python program which iterates two lists of numbers simultaneously and adds corresponding values, print the result
f_list = [1,2,3,4]
s_list = [2,3,4,5]
res = [f_n +s_n for f_n, s_n in zip(f_list, s_list)]
print(f"{res}")


# In[19]:


# write a python function that takes a list of numbers and calculate square of each number and return it in a list
def square_num(mynumbers):
    return list(map(lambda num: num**2,mynumbers))
square_num([1,2,3])


# In[21]:


# write a python function that takes two lists and combines them without any duplicates and return the list
def combine_lists(L1, L2):
    return L1 + [items for items in L2 if items not in L1]

L1 = [1,2,3]
L2 = [2,4,3]

combine_lists(L1,L2)


# In[29]:


# write a python function that removes all the vowels from the given list of strings and return the list
def myfunc(listitems):
    final=[]
    for strchar in listitems:
        for letters in strchar:
            if letters in ('a','e','i','o','u', 'A','E','I','O','U'):
                strchar = strchar.replace(letters,"")            
        final.append(strchar) 
    return final
    
myfunc(["rohan", "END"])


# In[43]:


# write a python program to print all the keys in the dictionary and store it in a list
sample_dict = {'1':1, '2':2, '3':3}
key_list = list(sample_dict.keys())
print(f"{key_list}")


# In[45]:


# write a python program to remove duplicates from a list and print the result in list
input_list = [1,2,3,4,4,33,2,5]
dedup = list(set(input_list))
print(f"{dedup}")


# In[46]:


# write a python function that takes a list of elements and n as input, extract and append first n characters and last n characters of each string and return the resultant list
def nchar (list1,no):
    return [items[:no]+items[-no:] for items in list1]
list1 = ["ROHAN", "END"]
nchar(list1, 3)


# In[56]:


# write a python function that takes two parameters, first parameter is a list of dictionary and second is a list of tuples. Append the list of tuples to the list of dictionary
def addentry (listname, addlist):
    for names,ages in addlist:
            listname.append(addlist)
    return listname
    
addentry([{'1':"A"}], [("2", "B")])


# In[57]:


# write a python function that takes a dictionary and a string, appends the string to the list of values
def addnames_in_dict (dictname, name):
    for i in dictname:
        dictname[i].append(name)
    return dictname
addnames_in_dict({"1":["A"]}, "Arun")


# In[59]:


# write a python program to iterate through the list and create a dictionary with integers as keys
list_= [1,2,3,4]
dict_comp = {idx:value for idx,value in enumerate(list_)}
print(f"{dict_comp}")


# In[60]:


# write a python function to add all even numbers between minimum and maximum value
def add_even_num(min, max):
    return sum([i for i in range(min, max) if i%2==0])

add_even_num(1, 6)


# In[123]:


# write a python program to iterate through a string using for loop
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(f"{h_letters}")


# In[127]:


# write a python program to iterate through a string using lambda and print the result
letters = list(map(lambda x: x, 'human'))
print(letters)


# In[129]:


# write a python function to calculate the price after tax for a list of transactions
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = list(map(get_price_with_tax, txns))
print(f"{final_prices}")


# In[138]:


# write a python program to print python version using sys
import sys

print(f"{sys.version}")


# In[140]:


# write a python program to print system time
import time
print(f"{time.time()}")


# In[143]:


# write a python function to inherit a parent class person in a child class Student
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass


# In[130]:


# write a python program to replace all the negative values to zero and keep only positive values in the list
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(f"{prices}")


# In[133]:


# write a python function to generate random number between a  given range
import random

def get_weather_data(min, max):
    return random.randrange(min, max)

rand_num = get_weather_data(11, 20)
print(f"{rand_num}")


# In[135]:


# write a python function which uses generator to sum all the numbers in a range
min_value = 10
max_value = 10000
sum_all = sum(i * i for i in range(min_value, max_value))
print(f"{sum_all}")


# In[126]:


# write a python program to transpose Matrix using Nested Loops and print the result
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(f"{transposed}")


# In[142]:


# write a python function to create two threads and start and join the two threads 
import threading 
  
def print_cube(num): 
    print("Cube: {}".format(num * num * num)) 
    
t1 = threading.Thread(target=print_cube, args=(10,)) 
t2 = threading.Thread(target=print_cube, args=(10,)) 

t1.start() 

t2.start() 

t1.join()
t2.join()






