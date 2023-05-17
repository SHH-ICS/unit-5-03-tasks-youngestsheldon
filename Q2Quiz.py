# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
import json

with open("Question.json", "r") as f:
    Data = json.loads(f.read())

print(Data["Question"])
for i in range(4): print(f"{i+1}) {Data['Answers'][i]}")
Ans = int(input("Correct Index: "))

if Ans == Data["Correct"]:
    print("Correct")
else:
    print("Incorrect")
