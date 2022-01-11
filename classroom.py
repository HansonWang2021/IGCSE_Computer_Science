student_names = ["M", "A", "C", "M", "D", "L", "R", "Ange"]



student_names.append("Mars")
student_names.insert(0, "Mr. Amini")


student_names.remove("C")


for name in student_names:
    print(name)


lengh = len(student_names)
print(lengh)


student_names.sort()
for name in student_names:
    print(name)





#integer list
numbers = [0, 0, 1, 1, 2, 3, 4, 0, 0, 1, 1, 0, 0, 1, 0, 0]
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)

numbers.sort()

for number in numbers:
    print(number)






#dictionary to represent sibling names of students
student_classes = {
"Howard": ["Computer Science", "Chemistry", "Think American 3"],
"Barbie": ["Computer Science", "Chemistry", "Think American 3"],
"Adrian": ["Computer Science", "Business", "Think American 3"],
"Mike": ["Computer Science", "Business", "Think American 3"],
"Hanson": ["Computer Science", "Business", "Think American 2"]
}
student_IGCSE_class = student_classes.get("Howard")
student_IGCSE_class.sort()
for classes in student_IGCSE_class:
   print(classes)




student_temperature = [36, 37.1, 35.8, 37, 39.1, 36.5, 36.4]
print(student_temperature)

student_temperature.append(37.6)
print(student_temperature)

index = student_temperature.index(37.6)
print(index)

student_temperature.remove(35.8)
print(student_temperature)

temperature = student_temperature[0]
print(temperature)

student_temperature.sort()

hughest_temperrature = student_temperature.pop()
print(hughest_temperrature)



#create a dictionary to store the student in
#IGCSE and whether or not they've been
#naughty = False, nice = Ture
#to show which students are getting gifts

has_gift = {"Mars":False, "Henry":False, "Adrian":True, "Angelina":False}

student_has_gifts = has_gift.get("Mars")
print("The student has a gift", student_has_gifts)


for student in has_gift:
    print(student, "has gifts: ", has_gift.get(student))


student_removed = has_gift.pop("Adrian")
print(student_removed)
print(has_gift)


#create a dictionary to represent Secret Santa
#Ex {"Mr. Amini": "Peter", "Ms. Jen": "Ms. Ana"}

secret_santa = {
    "Mr. amini": "Teacher Peter",
    "Ms.Jen": "Ms. Ana"
    }
teecipient = secret_santa.get("Mr. Amini")
print()