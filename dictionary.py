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
print("Mars exam score", mars_score)