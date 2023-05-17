# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

import json

Question = input("Question: ")
Answers = []
for i in range(4):
    Answers.append(input(f"Answer ({i+1}): "))
CorrectIndex = int(input("Corect Index: "))

Data = {"Question":Question, "Answers":Answers,"Correct":CorrectIndex}
with open("Question.json", "w") as f:
    f.write(json.dumps(Data))