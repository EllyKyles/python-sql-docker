class Pet:
    def __init__(self, name="molly",age=3,sex='female', species="dog", **kwargs):
        self.name = name
        self.species = kwargs["species"] if species in kwargs else species
        self.age = kwargs["age"] if age in kwargs else age
        self.sex = kwargs["sex"] if sex in kwargs else sex  

def __str__(self):
    return "{} is a {} and is {} years old {}".foramt(self.name, self.species, self.age, self.sex)

def __repr__(self):
    return self.__str__()