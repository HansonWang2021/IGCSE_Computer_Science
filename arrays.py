import array
#create a new array using built in array
test_scores = array("i", [98, 70, 48, 60, 98, 97, 93])

#add another test scores to end of our array
test_scores.append(100)
print(test_scores[1])


for score in test_scores:
    print(score)


length = len(test_scores)
print("length of the array(number of score): ", length)

#other array methods
test_scores.remove["90"]



letter_grades = ["A", "A-", "A", "B", "B", "C", "C-", "A-" "B+"]
letter_grades.append("B")
letter_grades.append("A")
letter_grades.append("A")


#count number of people with grade A
number_of_A_grades = letter_grades.count("A")
print("number of grades A:", number_of_A_grades)

#integer list
numbers = [0, 0, 1, 1, 2, 3, 4, 0, 0, 1, 1, 0, 0, 1, 0, 0]
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)
