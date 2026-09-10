class Pet: 
    species = species

    def __init__(self, name, age): 
        self.name = name 
        self.age = age

    def human_years_calc(self):
        return self.age * 7


pet_1 = Pet()
print(pet_1.human_years_calc())

pet_2 = Pet()
print(pet_2.human_years_calc())

pet_3 = Pet()
print(pet_3.human_years_calc())

