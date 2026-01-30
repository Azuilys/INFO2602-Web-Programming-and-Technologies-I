from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

@app.get('/students')
#async def get_students():
#    return data
async def get_students(pref = None):
    if pref: 
        filteredStudents = []
        for student in data:
            if student['pref'] == pref:
                filteredStudents.append(student)
        return filteredStudents
    return data

@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: # Only return the student if the ID matches
      return student
  
@app.get ('/stats')
async def statistics():
    dictionary = {}
    Chicken = 0
    Fish = 0
    Vegetable = 0
    csMajor = 0
    csSpecial = 0
    itMajor = 0
    itSpecial = 0    
    for student in data:
        if student['pref'] == 'Chicken' :
            Chicken = Chicken + 1
        
        if student['pref'] == 'Fish' :
            Fish = Fish + 1
            
        if student['pref'] == 'Vegetable' :
            Vegetable = Vegetable + 1
        
        if student['programme'] == 'Computer Science (Major)' :
            csMajor = csMajor + 1
            
        if student['programme'] == 'Computer Science (Special)' :
            csSpecial = csSpecial + 1
        
        if student['programme'] == 'Information Technology (Major)' :
            itMajor = itMajor + 1
        
        if student['programme'] == 'Information Technology (Special)' :
            itSpecial = itSpecial + 1
    
    dictionary ['Chicken'] = Chicken
    dictionary['Computer Science (Major)'] = csMajor
    dictionary['Computer Science (Special)'] = csSpecial
    dictionary['Fish'] = Fish
    dictionary['Information Technology (Major)'] = itMajor
    dictionary['Information Technology (Special)'] = itSpecial
    dictionary['Vegetable'] = Vegetable
    
    return dictionary

@app.get ('/add/{a}/{b}')
async def addition (a, b):
    sum = int(a) + int(b) 
    return sum

@app.get ('/subtract/{a}/{b}')
async def subtract (a, b):
    difference = int(a) - int(b) 
    return difference

@app.get ('/multiply/{a}/{b}')
async def multiply (a, b):
    product = int(a) * int(b) 
    return product

@app.get ('/divide/{a}/{b}')
async def divide (a, b):
    quotient = int(a) / int(b) 
    return quotient