# import statements.
from globals import friends
from termcolor import colored
import re

# add new friends.
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '.',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    wholecheck = True
    while (wholecheck):
        tempcheck = True
        patternsalutation = '^Mr|Ms$'
        patternname = '^[A-Za-z][A-Za-z\s]+$'
        patternage = '^[0-9]+$'
        patternrating = '^[0-9]+\.[0-9]$'
        while tempcheck:
            new_friend['name'] = raw_input("Please add your friend's name: ")
            if (re.match(patternname, new_friend['name']) != None):
                tempcheck = False
            else:
                print colored("invalid name , try again", 'red')
        tempcheck = True
        while tempcheck:
            new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
            if (re.match(patternsalutation, new_friend['salutation']) != None):
                tempcheck = False
            else:
                print colored("invalid salutation , try again", 'red')
            new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

        while tempcheck:
            new_friend['age'] = raw_input("Age? ")
            if (re.match(patternage, new_friend['age']) != None):
                tempcheck = False
            else:
                print colored("invalid age , try again", 'red')
        tempcheck = True
        while tempcheck:
            new_friend['rating'] = raw_input("Spy rating? ")
            if (re.match(patternrating, new_friend['rating']) != None):
                tempcheck = False
            else:
                print colored("invalid rating , try again", 'red')
        wholecheck=False

    # users input validations
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50:
        friends.append(new_friend)
        print colored('Friend Added!','green')
    else:
        print colored('Sorry! Invalid entry. We can\'t add spy with the details you provided','red')

    # returning total no of friends.
    return len(friends)