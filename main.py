# import statements
from spy_details import spy_name, spy_salutation, spy_age, spy_rating, spy_is_online
from start_chat import  start_chat

print "Let's get started!"
question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N): "
existing = raw_input(question)

# validating users input
if (existing.upper() == "Y") :
    # user wants to continue as default user.

    # concatination of salutation and name of spy.
    spy_name = spy_salutation + " " + spy_name

    # starting chat application.
    start_chat(spy_name, spy_age, spy_rating, spy_is_online)
elif (existing.upper() == "N"):
    # user wants to continue as new user
    spy_name = raw_input("Provide your name here :")
    # chek wether spy has input something or not
    if len(spy_name) > 0:
        # input more details about user.
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False

        spy_salutation = raw_input("What should we all you ? : ")
        spy_age = int(raw_input("Enter your age. ?")) # converting users input to integer (typecasting)

        # concatination of salutation and name of spy.
        spy_name = spy_salutation + " " + spy_name

        spy_rating = float(raw_input("What is your spy rating?")) # converting users input to float (typecasting)
        spy_is_online = True

        # starting chat application.
        start_chat(spy_name, spy_age, spy_rating, spy_is_online)
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."