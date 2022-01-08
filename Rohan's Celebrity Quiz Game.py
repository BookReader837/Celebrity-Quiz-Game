#Title of Celeb Quiz Game

print("")
print("Welcome to Rohan's Celebrity Quiz Game!")
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Introduction to the game

print("There will be 10 true or false questions. Each time you get a correct answer, you get 1 point.")
print("")
print("The total amount of points that you've earned will be displayed at the start of each new question.")
print("")
print("Once you've answered all ten questions, your final score will be displayed on the terminal.")
print("")
print("When answering the questions, keep in mind that your answers must start with uppercase letters and be either 'True' or 'False'.")
print("")
user_total_points = 0

#-----------------------------------------------------------------------------------------------------------------------
#Question 1: Taylor Swift's first job

print(str(user_total_points) + "/10")

print("")
user_q1_answer = input("1) True or false: Taylor Swift's first job was as a party princess. ")
print("")

if user_q1_answer == "True":
    print("Incorrect. Her first job was actually to knock praying mantises out of Christmas trees. Sounds crazy, right?")

elif user_q1_answer == "False":
    print("Correct! Her first job was actually to knock praying mantises out of Christmas trees. Sounds crazy, right?")
    user_total_points += 1
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 2: Donald Trump

print(str(user_total_points) + "/10")

print("")
user_q2_answer = input("2) True or false: Donald Trump owns & operates around 25 golf courses around the world. ")
print("")

if user_q2_answer == "True":
    print("Incorrect. Donald Trump actually owns around 19 golf courses around the world, not 25!")

elif user_q2_answer == "False":
    print("Correct! What a rich guy!")
    user_total_points += 1
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 3: Tiger Woods

print(str(user_total_points) + "/10")

print("")
user_q3_answer = input("3) True or false: Tiger Woods is a buddhist. ")
print("")

if user_q3_answer == "True":
    print("Correct! Pretty interesting, right?")
    user_total_points += 1

elif user_q3_answer == "False":
    print("Incorrect. Tiger Woods shared his belief in Buddhist to Sports Illustrated in 1996.")
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 4: Selena Gomez's first kiss

print(str(user_total_points) + "/10")

print("")
user_q4_answer = input("4) True or false: Selena Gomez had her first kiss when she was 12 years old with Cole Sprouse. ")
print("")

if user_q4_answer == "True":
    print("Incorrect. Her first kiss was at 12 years with Cole Sprouse, Dylan Sprouse's twin brother.")

elif user_q4_answer == "False":
    print("Correct! Her first kiss was at 12 years with Cole Sprouse, Dylan Sprouse's twin brother.")
    user_total_points += 1
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 5: Ashton Kutcher

print(str(user_total_points) + "/10")

print("")
user_q5_answer = input("5) True or False: Ashton Kutcher has webbed toes. ")
print("")

if user_q5_answer == "True":
    print("Correct! Webbed toes is a condition where two of your toes are literally fused together. Pretty gross!")
    user_total_points += 1

elif user_q5_answer == "False":
    print("Incorrect. Webbed toes is a condition where two of your toes are literally fused together. Pretty nasty!")
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 6: Jeremy Renner's job before acting

print(str(user_total_points) + "/10")

print("")
user_q6_answer = input("6) True or False: Jeremy Renner worked as a clown before becoming an actor. ")
print("")

if user_q6_answer == "True":
    print("Incorrect. Believe it or not, he used to be a makeup artist before striking it big in the acting industry!")

elif user_q6_answer == "False":
    print("Correct! Believe it or not, he used to be a makeup artist before striking it big in the acting industry!")
    user_total_points += 1
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 7: Robert Downey Jr.

print(str(user_total_points) + "/10")

print("")
user_q7_answer = input("7) True or False: Robert Downey Jr. claimed that Burger King saved his life from drug addiction. ")
print("")

if user_q7_answer == "True":
    print("Correct!. Pretty wholesome, right?")
    user_total_points += 1

elif user_q7_answer == "False":
    print("Incorrect. Sounds very wholesome, indeed.")
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 8: Dennis Rodman

print(str(user_total_points) + "/10")

print("")
user_q8_answer = input("8) True or False: Dennis Rodman has 28 siblings. ")
print("")

if user_q8_answer == "True":
    print("Correct! Sounds, crazy right?")
    user_total_points += 1

elif user_q8_answer == "False":
    print("Incorrect. Believe it or not, Dennis Rodman actually has 28 siblings!")
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 9: Leonardo DiCaprio and Tobey Maguire

print(str(user_total_points) + "/10")

print("")
user_q9_answer = input("9) True or False: Leonardo DiCaprio and Tobey Maguire are bitter enemies in real life. ")
print("")

if user_q9_answer == "True":
    print("Incorrect. Leonardo Dicaprio and Tobey Maguire have been friends for over 30 years, ever since they were kids!")

elif user_q9_answer == "False":
    print("Correct! Leonardo Dicaprio and Tobey Maguire have been friends for over 30 years, ever since they were kids!")
    user_total_points += 1
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Question 10: Bill Murray

print(str(user_total_points) + "/10")

print("")
user_q10_answer = input("10) True or False: Bill Murray was once arrested at 20 for bringing 15 pounds of marijuana on a plane. ")
print("")

if user_q10_answer == "True":
    print("Incorrect. He was actually arrested for bringing 10 pounds of marijuana on a plane, not 15!")

elif user_q10_answer == "False":
    print("Correct! He was actually arrested for bringing 10 pounds of marijuana on a plane.")
    user_total_points += 1
print("")

#-----------------------------------------------------------------------------------------------------------------------
#Final Results

print("Your final score is: " + str(user_total_points) + "/10")
if user_total_points >= 7:
    print("Great Job!")
elif user_total_points <= 3:
    print("Better luck next time...")