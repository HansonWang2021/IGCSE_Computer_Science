#Function with two parameters 
#write a function that takes in two arguments
#and returns the sum of those two args
def polynomial(number, anotherNumber):
    return 2 * number + 8 * anotherNumber
result = polynomial(3, 5)
print(result)

#Random Number generation
#Write code to generate a random number between (0 - 99) and print result on the screen
import random 

random_number = random.randint(0, 99)
print(random_number)

#While loop
#1. write a while loop to print ("Today, I am outstanding in every way") 4x
i = 1
while i < 5:
  print("Today, I am outstanding in every way")
  i += 1

#for loop
#1. write a for loop that says "I become what I think about most of the time" 200x
for i in range(200):
    print("I become what I think about most of the time")

#user input
#Write code that asks a user for input and prints the message “You look great today, name”
name = input("Enter your name: ")

print("You look great today", name) 

name = input("Enter your name: ")

print("You look great today", name)


#string operations
alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
#write a line of code to find the length of this string
#print the length on the screen 


#string operations
alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
 
#write code to find the index (position) of the letter "j"
#print the index on the screen



#data structures (Arrays)
from array import array
#create a new integer array using built in array method to store the class grades on the final exam
#data structures (Arrays)
#add another test scores to end of our array (append = add)
#data structures (Arrays)
#print the length of the Array on the screen 
final_exam_scores = array("i", [90, 70, 40, 60, 98, 97, 93])

final_exam_scores.append(100)
print(final_exam_scores[0])

for score in final_exam_scores:
    print(score)

length = len(final_exam_scores)
print("length of the array(number of scores): ", length)

#Write code - data structures (Lists)
#create a list of IGCSE computer science student names (list of strings)and include the name “Arsalon”
#Write code - data structures (Lists)
#Delete the name “Arsalon”
#Write code - data structures (Lists)
#Sort the list of names using the built in sort method of Python and print on the screen
student_names = ["Mike", "Amy", "Charlie", "Marco", "Arsalon"]

student_names.remove("Arsalon")
for name in student_names:
    print(name)

#data structures (dictionaries)
#create a dictionary (key-value pair)
#key = a string representing the student name
#value = list of integers representing scores on past three exams **include “Arsalon”: [99, 100, 99]
#Data Structures (dictionaries)
#Using python’s built in get method to retrieve “Arsalon”’s list of scores (list of integers) and print them on the screen 
student_scores = {
"Adrian": [90, 91, 88],
"Charlie": [88, 99, 100],
"Arsalon": [99, 100, 99]
}
student_scores = student_scores.get("Arsalon")
for score in student_scores:
    print(score)

