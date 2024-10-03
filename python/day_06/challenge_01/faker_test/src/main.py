from faker import Faker
from faker.providers import internet
from pprint import pprint
from dataclasses import dataclass
faker = Faker()
faker.add_provider(internet)

@dataclass(eq=True)
class Person:
    name: str
    
@dataclass
class Machine:
    ip: str
        
list_of_names = [
    Person(name=faker.name())
    for _ in range(20)
]



machines = [ 
    Machine(ip=faker.ipv4_private())
    for _ in range(5)
]

pprint(list_of_names)
pprint(machines)