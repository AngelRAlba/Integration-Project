"""
__author__ = Angel Alba-Perez
Identity Crisis, This code will put you in the position of a post
apocalyptic survivor that has just awoken from kryo sleep. You start logging
into the main system as a user to try and figure out what happened.
"""
import random

print("Welcome back to FallenRise Inc., the only company planning ahead for "
      "your future.\nStarting up, one moment "
      "please.\nPlease log in to proceed with start up.")
firstIdentity = input("\nPlease state your first name.")
lastIdentity = input("Now state your last name.")

# Identification number can be used later for potential questions.


userIdentificationNumber = int(random.randint(0, 1000000))
print("\nIt is good to hear back from you " + firstIdentity + ' ' +
      lastIdentity + ' '"\nIdentification number: " +
      str(userIdentificationNumber) + ".\n\nWe have a few questions for "
                                      "you.\nThe purpose of these questions "
                                      "are  to check your mental capacity.")

# Asking for age can be anything at the moment, I need to make it an if else
# while loop so only a int() can be accepted.
# Potentially fixed using the try function
# float would allow decimals (It would replace int)
wrong_age_input = True
while wrong_age_input:
    try:
        age_number = int(input("Enter you age as a whole number: "))
        print("\n" + str(age_number) + "? \nYou think it's still 2019, "
                                       "don't you?\nWhat a shame.")
        wrong_age_input = False
    except ValueError:
        print("This is not a whole number, please try again")

print("\nBesides that we need to know you can still preform basic "
      "calculations. \n\nWe will start with basic "
      "addition.\nAs an example I will solve a addition "
      "problem with numbers you give me to hopefully refresh your memory.")

# For the example math below I should use a loop to make sure its only
# numbers being entered, also to allow them to
# re-enter a proper number if they didn't follow the rules they were told.
# This has been corrected using proper try functions

wrong_math_example_A_input = True
exampleNumberA = None
while wrong_math_example_A_input:
    try:
        exampleNumberA = float(input("\nWhat is your first number?\nIt's "
                                     "best to keep it simple so you can "
                                     "understand and remember."))
        wrong_math_example_A_input = False
    except ValueError:
        print("This is not a valid number")
wrong_math_example_B_input = True
exampleNumberB = None
while wrong_math_example_B_input:
    try:
        exampleNumberB = float(input("\nNow for your second "
                                     "number.\nRemember you can keep it "
                                     "simple to understand."))
        wrong_math_example_B_input = False
    except ValueError:
        print("This is not a valid number")
print("\nNow I am going to simply add your numbers together, try and "
      "remember how math works and where my solution came from.")

math_example_solution = exampleNumberA + exampleNumberB
print("Your answer is:", math_example_solution)

print("\nNow you need to answer my addition problem correctly.")


# Definitions for the random addition (can be used and changed for various
# random numbers in different questions).
# I don't know why correctAnswer1 keeps being highlighted.

def number_addition_quest_hard():
    """
    Adding 3 random numbers
    :return: The sum of three random numbers
    """
    random_quest_hard1 = (random.randint(1, 100))
    random_quest_hard2 = (random.randint(1, 100))
    random_quest_hard3 = (random.randint(1, 100))
    print(random_quest_hard1)
    print(random_quest_hard2)
    print(random_quest_hard3)
    correct_answer1 = (random_quest_hard1 + random_quest_hard2 +
                       random_quest_hard3)
    return correct_answer1


# The loop for double incorrect math flawed, can be fixed by possibly
# changing the first input before the if.

userAnswer1 = 2
correctAnswer1 = 4
print("\nI want you to add up these numbers, ")
while str(userAnswer1) != str(correctAnswer1):
    correctAnswer1 = number_addition_quest_hard()
    userAnswer1 = int(input("Waiting for correct answer: "))
    if str(userAnswer1) != str(correctAnswer1):
        print("That number was incorrect, I need you to try again with new "
              "numbers.\nPlease take your time.")
        correctAnswer1 = number_addition_quest_hard()
        userAnswer1 = int(input("Waiting for correct answer: "))
    else:
        print("\nThat was correct, I hope you wrote down how you solved "
              "that. \nWe wouldn't want you forgetting any of "
              "these important tools.")
print("\nSince you got the answer correct we can move on from that for now.")


# Using parameters and returning the function with values being given to the
# computer.
# Basic equation for finding smaller of two numbers, includes negatives.

def which_smaller(val1, val2):
    """
    Finding which value is smaller
    :param val1: You are typing in the first number for the computer example
    :param val2:You are typing in the second number for the computer example
    :return: It will tell you which of the two values is larger
    """
    if val1 < val2:
        smaller = val1
    else:
        smaller = val2
    return smaller


print("\nNow you will be given examples about which number is larger between "
      "two integers before you have to answer back.\nLike before, I will "
      "provide an example first.")


# Basic definition for finding the smaller number example (can be used as a
# frame for later use).

def which_smaller_example():
    """
This code creates two random numbers and tells the user which of the two are
smallest.
    """
    comp_small_gen1 = (random.randint(1, 100))
    print("\nThis is the first number:", comp_small_gen1)
    comp_small_gen2 = (random.randint(1, 100))
    print("This is the second number:", comp_small_gen2)

    smaller_value = which_smaller(comp_small_gen1, comp_small_gen2)
    print("The smaller of the two numbers is", smaller_value)


# Using the def statement and parameters to type the example easily.

which_smaller_example()

print("\nNow I will give you numbers and you will provide the correct answer "
      "about which is the smallest.")


# another example that needs to be modified with a if else while loop for
# int() input only.


def which_smaller_bait_question():
    """
This code asks the user for two numbers and it will tell the user which is
smallest but starts causing errors onn purpose.
    """
    small_numb_gen_quest1 = (random.randint(1, 100))
    print("\nThis will be your first number:", small_numb_gen_quest1)
    small_numb_gen_quest2 = (random.randint(1, 100))
    print("\nThis will be your second number:", small_numb_gen_quest2)


input("Please type the answer.")
input("PleAse_tYpe_TThe_anSwEr..")
input("pLe__e_T_pe_th__a_sW_r")
input("..........Who are you?")

print("I don't know you...should I?")
userIdentificationNumberNeeded = int(input("What was your "
                                           "userIdentificationNumber?"))
if userIdentificationNumber == userIdentificationNumberNeeded:
    print("Oh, your part of the D-Personal, where is your instructor?")
else:
    print("The number provided does not match the corresponding kryo pod.")

Alone = int(input("Is there no instructors with you? 1 for yes and anything "
                  "else for no."))
if Alone == 1:
    print("I don't like liars.")
else:
    print("So the procedure was a failure...")

Truth = input("This is not good, I would ask you for details but you're only "
              "D class.\nWould you like to be educated on the world around "
              "you, 1 for yes and anything for no.")
if Truth == 1:
    print("I suppose I should start with the reason you ''volunteered''.\n "
          "Your personal history has been wiped from the system but you are "
          "currently in a simulation, an imaginary world if you want a "
          "simpler way of thinking. \n You are a low class individual in the "
          "simulation But it looks like no instructors have shown themselves "
          "to you.\n "
          "If there is no one then the Drost have infected the pods, "
          "they are a form of sentient electronic signals that take "
          "advantage of organisms once they enter the state of REM "
          "sleep.\nThey infect the brain and absorb the energy from the "
          "organism, causing gradual deterioration of the brain, leading to "
          "lack of memory, followed by lose of motor controls, and ending "
          "with violent seizures.\n We found them underground in the mines of "
          "an abandoned power plant. \nThe location was meant to distribute "
          "electricity in the city of -REDACTED- but after a cave-in the "
          "miners were stranded and forced to survive how ever they "
          "could.\nThe constant fear and depleting oxygen cause them to "
          "have extreme dreams and when one miners was presumably "
          "electrocuted by a loose cable "
          "while sleeping, the burst of energy caused the electronic energy "
          "of "
          "the brain to become sentient.\n This organism feeds on the "
          "electron energy of organisms that sleep since the brains electron "
          "energy is at its "
          "highest with lowest resistance.\nIt then multiplies and with a "
          "long story shortened "
          "humanity was placed in kryo stasis with no electron energy being "
          "produced. \n I do not know what is wrong but you should know "
          "this, you are awake, you are alone.\nThe others that you have "
          "seen are only AI, robots created to keep your brain activity "
          "normal.\n\n\nYou need to find ThE sOurCe oF tHe __nTam__ation "
          "aNd_pR__eNt_A_y_FurT_er_sPreAd,"
          "_yO__Sh_ulD_fInd_Cl_es_Ar___d_yO_r_hOmE"
          ".\nANd_bE_____________Corru__ion_iS_SpR_adi_g.")
# you need to find the source of the contamination and prevent any further
# spread, you should find clues around your home. And be careful,
# the corruption is spreading.
else:
    print("fine, ignorance is bliss for you poor organisms, its a shame to. "
          "\nI thoUght yOu WouLd HavE_l_ked_tHe_st_Ry.")
# I thought you would have liked the story.
print("Error\nError\nShutting Down")
input("Are you awake?")
