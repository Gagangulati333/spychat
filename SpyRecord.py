print "Let's get started!"
spy_name = raw_input("Enter your name :")
#check wether spy input somthing or notQ
if len(spy_name) > 0:
    #code blocks if condition is true
    print "Alright" + spy_name + "i would like to know more about you before we proceed further"
    spy_age = 0
    spy_rating= 0.0
    spy_is_online = False
    spy_salutation = raw_input("enter your salutation :")
    spy_age = raw_input("enter your age :")
    spy_rating = raw_input("enter your rating:")
    spy_is_online = raw_input("enter your status :")
else:
    print "a spy needs to have a valid name . try again please"
#spy name and salutation concatinated
spy_name = spy_name + " " + spy_salutation
print "WELCOME " + spy_name + " glad to have you back with us"      1