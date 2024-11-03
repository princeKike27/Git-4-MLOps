# import pydantic
from pydantic import BaseModel 

# data
data = {
    'name': 'Murthy',
    'age': '28',
    'course': 'MLOps Bootcamp',
    'ratings': [4, 4, '4', '5', 4]
}

# Instructor Class >> Inherits from BaseModel
class Instructor(BaseModel):
    # data rules definition
    name: str
    age: int
    course: str 
    ratings: list[int] = []


# create instance of Instructor class
user = Instructor(**data) 

# print after pydantic parser
print(f'Found a Instructor: {user}', '\n')