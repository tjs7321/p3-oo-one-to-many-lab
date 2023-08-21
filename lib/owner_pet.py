class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Sorry, not a valid pet type.")
        Pet.all.append(self)

class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError('Pet must be an instance of Pet class.')

    def get_sorted_pets(self):
        def name_sort(e):
            return e.name
        return sorted([pet for pet in Pet.all if pet.owner == self], key=name_sort)