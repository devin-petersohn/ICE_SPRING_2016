import time
from random import randint

replies =["Yes","No","Possibly", "Ask again later", "Difficult to tell"]

def question():
    #Here is where you can ask the students what they would like the computer to ask
    #Let them decide how the user should be prompted
    print "What is your question?"
    question = raw_input()
    print replies[randint(0,4)]
    end()

def end():
    #Again let the students decide how to ask if user wants to go again
    print "Thanks for playing! Do you want to try again?"
    user_reply = raw_input()
    if user_reply == "yes":
        question()


print "Welcome to the magic 8-ball"
question()