# About Class
'''class Person():
    
    def __init__(self, name, age, sex, height):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
    
    def __repr__(self):
        return {self.name, self.age, self.sex, self.height)
    
    def __str__(self):
        return f"{self.name} is of age {self.age} with sex {self.sex} and height {self.height}"

    

Mithun = Person('Mithun', 22, 'M', 180)
print(Mithun)
print(str(Mithun))
print(Mithun.__str__)
print(Mithun.__repr__)
print(type(Mithun.__repr__))
'''
# removing extra strings
'''
S = "AABBCCDEDEACBED"
u = []
for i in S:
    if i not in u:
        u.append(i)
    else:
        continue

print(u)

x = [i for i in range(10)]
print(x[::-1])

'''
'''
class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def up(self, x):
        self.y +=x
    
    def down(self, x):
        self.y -= x
    
    def right(self, x):
        self.x += x
    
    def left(self, x):
        self.x -= x
    
    def dist(self, s):
        a = (self.x - s.x)**2
        b = (self.y - s.y)**2
        return (a + b)**0.5

    def dir(self, s, x):
        if s == 'E':
            self.right(x)
        if s == 'W':
            self.left(x)
        if s == 'N':
            self.up(x)
        if s == 'S':
            self.down(x)
    
    def alt_nearest(self, s1, s2):
        if self.dist(s1) > self.dist(s2):
            return [s2]
        
        if self.dist(s1) < self.dist(s2):
            return [s1]
        
        else:
            return [s1, s2]

    
    def farthest(self, s):
        far = 0
        for i in s:
            if self.dist(i) > far:
                far = i
        
        return far

    def nearest(self, s):
        near = -1
        for i in s:
            if self.dist(i) < far:
                far = i
        
        return near



p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = Point(1, 2)
p4 = Point(3, 5)
p5 = Point(3, 6)

s = [p2, p3, p4, p5]

print(p1.farthest(s))


'''
'''
# methods and types

def outer_function(func):
    def inner_function():
        print('This is executed too')
        return func()
    return inner_function


@outer_function
def display():
    print("Executed Display") #  display = outer_func(display)
'''
# ISOGRAM
'''
st = input('ENTER A WORD')
u = []
flag = 0
for i in st:
    if i not in u:
        u.append(i)
    else:
        flag = 1
        break

if flag == 0:
    print("ISOGRAM")

elif flag==1:
    print("NON-ISOGRAM")

'''

# classes, inheritance , network ,data structures in depth 
'''
class Employee():
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.name = first + ' ' + last
    
    def increment(self):
        self.salary *= 1.1
    
    def decrement(self):
        self.salary *= 0.9
    
    def change_salary(self, value):
        self.salary *= (1 + value/100)

class Developer(Employee):
    pass
    #def change_salary(self, value):
       # self.salary *= (1 + value/100)
    def increment(self):
        self.salary *= 1.2


class animal():

    kind = 'Dog'

    def __init__(self,color):
        self.color = color
        self.data = []
    
    def add(self, value):
        self.data.append(value)

a1 = animal('Black')
b1 = animal('White')
a1.add('Slack')
b1.add('Lazy')

'''
# Strings in Python
'''
my_string = "banana"

# string.find returns the index where the letter is 
print(my_string.find('an', 2))

my_string = " banana "
print(my_string.strip())

word = "Have it"
print(word.upper().endswith('T'))

new = "i am in amsterdam"
print(new.count('s'))

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
a = data.find('S')
b = data.find('8', a)
print(f"{data[a:b]}")

while True:
    line = input('>')
    if line.startswith("#") and len(line) > 0:
        continue
    elif line == "done":
        break
    print(line)
    '''
# Knowledge
'''

class Implication:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def test(self):

        if self.a == self.b or self.a is False:
            return True
        
        return False

class BiImplication(Implication):

    def test(self):

        if self.a == self.b:
            return True
        
        return False

a1 = Implication(True, False)
b1 = BiImplication(False, False)
print(a1.test())
print(b1.test())

'''

# LTTS Examps
'''
from itertools import cycle

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10, 11, 12, 13]

l3 = [l1[i%len(l1)] + l2[i%len(l2)] for i in range(max(len(l1), len(l2)))]
print(l3)

l4 = [x+y for x,y in zip(l1, l2)]
print(l4)

def modify(L):
    L.append(10)
    L.append(20)
    return L
    

L1 = [1, 2, 3, 4, 5]
L2 = modify(L1[:])
print(L2)
print(L1)

#posistional parameters

def calc(a,b,c):
    a += 10
    b += 20
    c += 30
    print(f"{a},{b},{c}")

calc(c=3,a=1,b=2)


# default arguments

def degree(age, branch='ECE', name='Mithun'):
    print(f"Name {name} of age {age} in branch {branch}")

degree(age=22)
'''
# posistional arguments then keyword arguments
'''
def sum(*args, **kwargs):
    s = 0
    for i in args:
        s += i
    for j in kwargs.values():
        s += j
    return s

print(sum(1,2,3,4,5,6, a=7, b=8))
'''
'''

import os
lst = [6, 4, 5, 3, 1, 2]
i = 0
os.chdir('/Users/mithu/Desktop/edx_2020_AI')
for f in os.listdir():
    new_name = str(lst[i]) + '_' + f
    os.rename(f, new_name)
    i += 1
'''
    

# Sets operations
'''
s1 = set([1, 3, 4, 4, 5, 2, 3])
s2 = set([6,7])
s1.add(1)
s1.remove(1)
s1.update([8,9,10], s2)
s1.discard(0)

l1 = {1, 2, 3}
l2 = {3, 4, 5}
l3 = {5, 6, 7, 8}

l4 = l1.intersection(l2,l3)
l5 = l1.union(l2, l3)
l6 = l1.difference(l2, l3)

'''
'''
VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

# just returns an assigned variable
def select_unassigned_variable(assignment):

    for variable in VARIABLES:
        if variable not in assignment:
            return variable
    return None

def consistent(assignment):

    for x,y in CONSTRAINTS:

        if x not in assignment or y not in assignment:
            continue
        
        if assignment[x] == assignment[y]:
            return False
    
    return True
        


def backtrack(assignment):

    if len(assignment) == len(VARIABLES):
        return assignment
    
    var = select_unassigned_variable(assignment)
    for value in ['Monday', 'Tuesday', 'Wednesday']:
        assignment[var] = value
        print(assignment)
        if consistent(assignment):
            backtrack(assignment)
        continue
   
        
solution = backtrack(dict())
print(solution)

'''
# Natural Language Processing(NLTK -> Natural Language Tool Kit)

'''
import nltk

grammar = nltk.CFG.fromstring("""

S -> NP VP

NP -> D N | N
VP -> V | V NP

D -> "the" | "a"
N -> "she" | "city" | "car"
V -> "saw" | "walked"

""")

parser = nltk.ChartParser(grammar)

sentence = input("Sentence: ").split()

try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
        tree.draw()
except ValueError:
    print('No sentence possible')

'''
import cv2
import time

# reading from a image file.
'''
img = cv2.imread('cat_goog.jpg', 0) # can use -1, 0 , 1
cv2.imshow('image', img)
k = cv2.waitKey(0)      # in 32 bit use a bitwise ' & ' with 0xff
if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('copycat.png', img)
    cv2.destroyAllWindows()

'''
# Reading from a video source.

'''
capt = cv2.VideoCapture(0)

while True:
    ret, frame = capt.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', gray)
    

    if cv2.waitKey(1) == 27:
        cv2.imwrite('my_image.png', gray)
        break

capt.release()
cv2.destroyAllWindows()

frame = cv2.imread('my_image.png', 0)
color = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
cv2.imwrite('new.png', color)
cv2.destroyAllWindows()

'''
