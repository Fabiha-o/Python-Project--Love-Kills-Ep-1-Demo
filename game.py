

#The text that the user will see first/ the introduction
introText = "Smash! With a smash of a vase, everything changes. The creaks of the old wooden door of your boyfriend's house have consumed your ears; however, your eyes are more set on the pieces of the vase in front of you, bathed in blood. That's not the worst part, as to your horror, the culprit shivering right beside the body is your beloved, Lily."
theStart = ["Love Kills", introText]
print(theStart[0])
print()
print(theStart[1])

#The question that will be asked first to all the users, put into a variable
introQ = "Cover for Lily or run away with Lily right now?"
print(introQ)
print()

# The two paths that the user will start diverging from, put into variables
bpathTwo = "What evidence do you want to hide?"
bpathOne = "The police are on to Lily. They have analyzed the data. They found Lily's fingerprints all over the murder weapon. Lily is now seen as the culprit, and you are her accomplice."
#The ending question and the text theh user will always see after they choose to end the game, put into a variable
endText = "Ep 2 is coming soon! Thanks for playing!"
# This function is for the end question
def endQ():
    print("Restart DEMO of Ep 1?")

introQ = "Cover for Lily or run away with Lily right now?"
print(introQ)
print()

#Start of the if statements and the loop gameRunning. This section will contain all the choices and their results
gameRunning = True
while gameRunning == True:
    
    option = int(input("Enter 1 for Runaway or 2 for Cover: "))
    if option == 1:
        print(bpathOne)
        sbpathQ = "Try going out of state or hide in the woods?"
        print(sbpathQ)
        sbOption = input("Enter 1 for out of state or 2 for the woods: ")
        if sbOption == "1":
            sbpathOne = "The police has caught Lily at the airport. You were at the bathroom at that time so they couldn’t catch you. You have decided to go and save Lily! To be Continued- END OF EP 1"
            print(sbpathOne)
            endQ()
            endOption = input("Choose 1 for restart or 2 for end: ")
            if endOption == "1":
                print("Reseting")
                gameRunning == False
            else:
                print(endText)
        else:
            print("You head off to a random forest. You get lost, and that’s not the worst part, as at that moment, a storm occurs. Luckily you see a cabin. But it looks old and dangerous. To be Continued- END OF EP 1")
            endQ()
            endOption = input("Choose 1 for restart or 2 for end: ")
            if endOption == "1":
                print("Reseting")
                gameRunning == False
            else:
                print(endText)
    elif option == 2:
        print(bpathTwo)
        print("pathtwo works!")
    else:
        print("Invalid input. Please enter 1 or 2.")

    print("End")