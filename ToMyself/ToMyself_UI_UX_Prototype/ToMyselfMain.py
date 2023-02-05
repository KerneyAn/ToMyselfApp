#import os
#from twilio.rest import Client

import scheduleTxt # import my module

howFar = input("How many minutes into the future will you send? (Has to be more than 61 minutes): \n") #Ask user how far to send
timeNum = int(howFar) #CHange it to an int
myTxtSchedule =  scheduleTxt.scheduleTxt(timeNum) #Put in time to put message forward
futureTime = myTxtSchedule.theTimer() #Put in time for format
myTxtSchedule.timedMessage(futureTime) #Asks for prompt and then schedules message
askPath = input("Would you like to do a reply path for this conversation? YES OR NO? \n")
pathChoice = askPath.upper()
if pathChoice == "YES":
    OptionA = input("Put reply option A: \n") #Will add a function that can do dynamic conversations with Twilio.
    OptionB = input("Put reply option B: \n")
else:
    print("Ok")
