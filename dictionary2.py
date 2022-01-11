#key = 
has_pets = {"Mars":False, "Henry":False, "Adrian":True, "Angelina":False}

student_has_pets = has_pets.get("Mars")
print("The student has a pes", student_has_pets)


for student in has_pets:
    print(student, "has pets: ", has_pets.get(student))



student_removed = has_pets.pop("Adrian")
print(student_removed)
print(has_pets)


