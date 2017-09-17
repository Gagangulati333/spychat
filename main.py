# import statements
from spy_details import spy
from start_chat import  start_chat
from termcolor import colored

print "Let's get started!"
question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): "
existing = raw_input(question)

# validating users input
if (existing.upper() == "Y") :
    # user wants to continue as default user.

    # concatination of salutation and name of spy.
    spy_name = spy['salutation'] + " " + spy['name']

    # starting chat application.
    start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
elif (existing.upper() == "N"):
    # user wants to continue as new user
    spy['name'] = raw_input("Provide your name here :")
    # chek wether spy has input something or not
    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("What should we all you ? : ")
        spy['age'] = int(raw_input("Enter your age. ?")) # converting users input to integer (typecasting)

        # concatination of salutation and name of spy.
        spy['name'] = spy['salutation'] + " " + spy['name']

        spy['rating'] = float(raw_input("What is your spy rating?")) # converting users input to float (typecasting)
        spy['is_online'] = True

        # starting chat application.
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
    else:
        print  colored("Invalid name. Try again.",'red')
else:
    print colored("Wrong choice. Try again.",'red')