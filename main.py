# buil pet adoption service
# pet class
from pet import Pet
import sqlite3


def db_insert(pet):
    conn = sqlite3.connect('pet.db')
    c = conn.cursor()
    sql = "insert into pets values ('{}','{}',{},'{}')".format(pet.name, pet.species, pet.age, pet.sex)
    c.exectue(sql)

while True:
    response=input("(e)nter a pet or (f)ile or (q)uit: ")
    
    if response =='q':
        break

    if response =='e':
        name=input("name:")
        species = input('species:')
        age = input('age:')
        sex = input('sex:')
        p = Pet(name, species, age, sex)
        db_insert(p)


    if response =='f':
        file = input('filename:')
        with open(file) as f:
            for line in f:
                name, species, age, sex = line.strip().split(',')
                p = Pet(name, species, age, sex)
                print("p:", p)
                db_insert(p)