from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Pet:
    name: str
    species : str

@dataclass
class Job:
    title: str
    salary: float


@dataclass(init=True, frozen= True)
class Person:
    """Class for person."""
    name: str
    age: int
    job : Optional [Job] = None
    friends: List['Person'] = field(default_factory=list)  # Default to an empty list
    pet : Optional [Pet] = None
    
    def add_friend(self, friend: 'Person') -> None:
        """Adds a person to the friends list."""
        if friend not in self.friends:
            self.friends.append(friend)
        else:
            print(f"{friend.name} is already a friend.")
            
    def remove_friend(self, friend: 'Person') -> None:
      
        if friend not in self.friends:
            print(f"{friend.name} is not a friend.")
            
        else:
            self.friends.remove(friend)
            print(f"{friend.name} has been removed.")
            
    def add_pet(self, pet: 'Pet') -> none:
        
        if self.pet = None:
            self.pet = pet
            
        else:
           print(f"{self.pet} is already a pet.") 
    

    
software_engineer = Job(title="Software Engineer", salary=100000)
person1 = Person(name="Alice", age=30, job=software_engineer)
person2 = Person(name="Asdruval", age=30, job=software_engineer)

person1.add_friend(person2)
print(person1.friends)
    