# Angel Raul Alba-Perez
# Identity Crisis
print("Welcome back to FallenRise Inc., the only company planning ahead for your future.\nStarting up, one moment "
      "please.\nPlease log in to proceed with start up.")
firstIdentity = input("\nPlease state your first name.")
lastIdentity = input("Now state your last name.")

# Identification number can be used later for potential questions.

import random

userIdentificationNumber = (random.randint(0, 1000000))
print("\nIt is good to hear back from you " + firstidentity + ' ' + lastidentity + ' '"\nIdentification number: " + str(
    useridentificationnumber) + ".\n\nWe have a few questions for you.\nThe purpose of these questions are to check "
                                "your mental capacity.")

# Asking for age can be anything at the moment, I need to make it an if else while loop so only a int() can be accepted.

age = input("\nHow old are you " + firstidentity + '?\nPlease use years as the measurement.')
print("\n" + age + "? \nYou think it's still 2019, don't you?\nWhat a shame.")
print("\nBesides that we need to know you can still preform basic calculations.\n\nWe will start with basic "
      "addition.\nAs an example I will solve a addition "
      "problem with numbers you give me to hopefully refresh your memory.")

# For the example math below I should use a loop to make sure its only numbers being entered, also to allow them to
# re-enter a proper number if they didn't follow the rules they were told.

exampleNumberA = input("\nWhat is your first number?\nMake it simple for your sake.")
examNumA = int(examplenumbera)
exampleNumberB = input("Now for your second number, remember to keep it simple.")
examNumB = int(examplenumberb)
print("\nNow I am going to simply add your numbers together, try and remember how math works and where my solution "
      "came from.")
exampleSolution = examNumA + examNumB
print("Your answer is:", exampleSolution)

print("\nNow you need to answer my addition problem correctly.")

# Definitions for the random addition (can be used and changed for various random numbers in different questions).
# I don't know why correctAnswer1 keeps being highlighted.
import random


def numberadditionquesthard():
    randomQuesthard1 = (random.randint(1, 100))
    randomQuesthard2 = (random.randint(1, 100))
    randomQuesthard3 = (random.randint(1, 100))
    print(randomQuesthard1)
    print(randomQuesthard2)
    print(randomQuesthard3)
    correctAnswer1 = (randomQuesthard1 + randomQuesthard2 + randomQuesthard3)
    return correctAnswer1


# The loop for double incorrect math flawed, can be fixed by possibly changing the first input before the if.

userAnswer1 = 2
correctAnswer1 = 4
print("\nI want you to add up these numbers, ")
while str(userAnswer1) != str(correctAnswer1):
    correctAnswer1 = numberadditionquesthard()
    userAnswer1 = int(input("Waiting for correct answer: "))
    if str(userAnswer1) != str(correctAnswer1):
        print("That number was incorrect, I need you to try again with new numbers.\nPlease take your time.")
        correctAnswer1 = numberadditionquesthard()
        userAnswer1 = int(input("Waiting for correct answer: "))
    else:
        print("\nThat was correct, I hope you wrote down how you solved that.\nWe wouldn't want you forgetting any of "
              "these important tools.")
print("\nSince you got the answer correct we can move on from that for now.")


# Using parameters and returning the function with values being given to the computer.
# Basic equation for finding smaller of two numbers, includes negatives.

def whichSmaller(val1, val2):
    if val1 < val2:
        smaller = val1
    else:
        smaller = val2
    return smaller


print("\nNow you will be given examples about which number is larger between two integers before you have to answer "
      "back.\nLike before, I will provide an example first.")


# Basic definition for finding the smaller number example (can be used as a frame for later use).

def whichSmallerExample():
    compSmallgen1 = (random.randint(1, 100))
    print("\nThis is the first number:", compSmallgen1)
    compSmallgen2 = (random.randint(1, 100))
    print("This is the second number:", compSmallgen2)

    smallerValue = whichSmaller(compSmallgen1, compSmallgen2)
    print("The smaller of the two numbers is", smallerValue)


# Using the def statment and parameters to type the example easily.

whichSmallerExample()

print("\nNow you will give me numbers and I will provide the answer before I am forced to make you answer the "
      "question yourself.")


# another example that needs to be modified with a if else while loop for int() input only.

def whichSmallerQuestion():
    userGen1 = int(input("\nEnter your first number: "))
    userGen2 = int(input("Enter your second number: "))

    smallerValue = whichSmaller(userGen1, userGen2)
    print("The smaller of the two numbers is", smallerValue)


whichSmallerQuestion()

print("\nI hope you know how I did that, it is now your turn.")

# this next step wil be a if else statement using true or false to check the correct answer
