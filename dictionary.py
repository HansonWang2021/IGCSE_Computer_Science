#creat a dicionary (key-value pairs) aka "HasMap, Map, HashTable"
score = {"Mars": 90, "Amy": 93, "Rain": 98, "Charlie": 98}


#Dictionaries or Hashmaps have fast lookup due to how they're stored in memory

#create a dicionary (key-value pairs) aka "HashMap, Map, HashTable"
assignment_scores = { "Mars": 90, "Amy": 93, "Rain": 98, "Charlie": 98 }
amy_assignment_score = assignment_scores.get("Amy")
print("Amy assignment score", amy_assignment_score)
#create a dictionary using built in dict function (same thing, different way to write it)
exam_scores = dict(Mars=90, Amy=93, Rain=98, Charlie=98)
mars_score = exam_scores.get("Mars")
<<<<<<< HEAD
print("Mars exam score", mars_score)

student_scores = {
"Adrian": [90, 91, 88],
"Charlie": [88, 99, 100],
"Mandy": [90, 95, 99],
"Yujing": [100, 99, 95],
"Angelina": [99, 98, 99],
"Mr. Amini": [50, 99, 99]
}
student_scores = student_scores.get("Adrian")
for score in student_scores:
    print(score)
=======
print("Mars exam score", mars_score)
>>>>>>> 242e07e1cf3741538c39a6bfa822b690f06122bb
