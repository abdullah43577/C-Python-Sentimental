# Build a basic translator

#giraffe translator

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation += 'G'
#             else:
#                 translation += 'g'
#         else:
#             translation += letter
#     return translation

# print(translate(input("Enter a phrase: ")))

# Try except
# try:
#     answer = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError:
#     print("Divided by zero")
# except ValueError:
#     print("Invalid Input")






#reading from external files in python
# i stored the file being opened in a variable called employee_file.

# employee_file = open("employee.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# # make sure to always close a file whenever you're done suing it.
# employee_file.close()





# writing to a file in python
# employee_file = open("employee.txt", "a")

# employee_file.write("\nKelly - Customer Service")

# employee_file.close()


# file = open("test.txt1", "w")
# file.write("Kelly - Customer Service")
# file.close()


#object oriented  test program using classses!
from test2 import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Banana?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)

























