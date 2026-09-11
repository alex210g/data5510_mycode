class Pet: 
    species = "dog" #store the species of the pet

    def __init__(self, name, age, species): 
        self.name = name 
        self.age = age
        self.species = species

    def human_years_calc(self):
        return self.age * 7

    def average_lifespan(self, species):
        if species == "dog": 
            return 13
        elif species == "cat":
            return 15
        elif species == "bird":
            return 5
        else: 
            return "Unknown species"


pet_1 = Pet("Stitch", 13, "dog")
print("Pet 1",pet_1.name,"is",pet_1.human_years_calc(),"in human years. with a average lifespan of ",pet_1.average_lifespan(pet_1.species)," years.")

pet_2 = Pet("Lucy", 5, "cat")
print("Pet 2",pet_2.name,"is",pet_2.human_years_calc(),"in human years. with a average lifespan of ",pet_2.average_lifespan(pet_2.species)," years.")

pet_3 = Pet("Max", 2, "bird")
print("Pet 3",pet_3.name,"is",pet_3.human_years_calc(),"in human years. with a average lifespan of ",pet_3.average_lifespan(pet_3.species)," years.")
