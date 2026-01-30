#PYTHON SYNTAX 1

# Variables Assignment & Operators
x = 10
print("Variable 'x': ", x)

x = 23
print("Variable 'x' Reassigned: ", x)

y = None
print("Variable 'y': ", y)

y = 2
z = (x + y) / x + (78 % 3)
print("z = (x + y) / x + (78 % 3) = ", z)
print()

#Primitive Types and Strings
name = "bobby"
nameVariableType = type(name)
print ("'name' Variable Type: ", nameVariableType)

age = 12
ageVariableType = type(age)
print("'age' Variable Type: ", ageVariableType)

height = 6.5
heightVariableType = type(height)
print("'height' Variable Type: ", heightVariableType)

hasDate = False
hasDateVariableType = type(hasDate)
print("'hasDate' Variable Type: ", hasDateVariableType)

complexVariable = 7j
complexVariableType = type(complexVariable)
print("'complexVariable' Variable Type: ", complexVariableType)

message = f"Message: Hi my name is {name}, I am {age} years old" #String Interpolation: Put my variables inside my sentence without me suffering.”
print()

intHeight = int(height)
print("Height, Float to Int: ", intHeight)

strHeight = str(height)
print("Height, Int to Str: ", strHeight)

floatHeight = float(intHeight)
print("Height, Int to Float: ", floatHeight)
print()

#Input Output
name = input("Enter Name: ")
print("Name: ", name)
print()

#Comparison
if 3 > 5:
    print("more")
else:
    print("less")
print()
    
mark = input("Please Enter Mark: ")
mark = int(mark)

print("Grade: ", end = ' ')
if mark > 70:
    print("A")
elif mark > 60:
    print("B")
elif mark >= 50:
    print("C")
else:
    print("F")
print()
    
#Iteration
i = 1
while i < 10:
    print(i)
    i = i + 1
else:
    print("This is ran when the loop condition is no longer met")
print()
    
list = ["bob", "sally", "john"]
for j in list:
    print(j, end = ' ')
print()
print()
    
string = "Ackienee"
for i in string:
    print(i, end = ' ')
print()
print()
    
for i in range(0, 10, 2): #prints from 0 - 10 in increments of 2 excluding 10
    print(i, end = ' ')
print()
print()
    
#Functions
def add(a, b):
    return a + b
sum = add(3, 9)
print("Sum: ", sum)
print()

def printPerson(name, age, height):
    print("Name: ", name)
    print("Age: ", age)
    print("Height: ", height) 
printPerson(age = 12, name = 'Henry', height = 5)
print()
    
def sayHello(fName, lName = 'Smith'):
    print(f"Hello {fName} {lName}")
sayHello('Landon')
sayHello('Bill', 'Young')
print()

def multiReturnFunction(a, b):
    return a + b, a - b, a * b, a / b

sum, difference, product, quotient = multiReturnFunction(10, 5)
print("Sum: ", sum)
print("Sum: ", difference)
print("Product: ", product)
print("Quoatient: ", quotient)
print()

#Lists
list = ['item1', 'item2', 'item3']
print("List: ", list)

list.append('item4')
print("List After Appened: ", list)

item4 = list.pop()
print("List After Pop: ", list)
print("Popped Item: ", item4)
print()

list2 = [12, 33, 45, 58, 23]
print("List2[4]/ List2[-1]: ", list2[-1]) # Negative indexing counts from the end of a list: -1 is the last item, -2 the second-to-last, etc.

list3 = list2.copy()
print("List3 (Copy of List2): ", list3)
print()

num = [ 1, 2, 3, 4]
print("Num: ", num)
doubled = [n * 2 for n in num]
print("Num List Doubled (Num * 2): ", doubled)

odd = [n for n in num if n % 2 == 1]
print("Odd Numbers In Num List: ", odd)
print()

[first, second, *rest] = num # unpacking a list, lets you create variables from items in the list
print("First Element/ Num[0]: ", first)
print("Second Element/ Num[1]: ", second)
print("Rest Of Num: ", rest)
print()

num2 = [5, 6]
num3 = num + num2
print("num + num2: ", num3)
print()

num4 = num2.copy()
print("Num4 (Copy of Num2): ", num4)
print()

#Tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("Tuple: ", thistuple); 
print("Tuple First Element: ", thistuple[0]); 
print()

#Sets
data = [ 20, 3, 20, 42, 2, 3, 10, 32, 2]
mySet = {0, 1}

for num in data:
    mySet.add(num)
    
print("mySet: ", mySet)
numOfUnique = len(mySet)
print("Number of Unique Data Pieces: ", numOfUnique)
print()

myDictionary = {
    "name" : "bob",
    "age" : 34
}

print("myDictionary: ", myDictionary) 
print("myDictionary Age: ", myDictionary['age']) # assessing a key
myDictionary['height'] = 7 # adding a new key and value
print("myDictionary Height: ", myDictionary['height']) # assessing a key
print()

for key in myDictionary:
    print(key)
print()
    
for key in myDictionary:
    print(f"{key} : {myDictionary[key]}")
print()

if 'weight' in myDictionary:
    print(f"{key} : {myDictionary['weight']}")
else:
    print("No Weight Property!")
print()


class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def sayHello(self):
        print("Hello! I'm a person, my name is", self.name)
        
class Student(Person):
    def __init__(self, stid, name, height, weight):
        super().__init__(name, height, weight)
        self.stid = stid
    
    def sayHello(self):
        print("Hello! I'm a student, my name is", self.name)
        
bob  = Person('bob', 12, 34)
sally = Student(123, 'sally', 7, 34)

bob.sayHello()
sally.sayHello()
print(bob.name)