from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends
from termcolor import colored
import re


def read_message():
    # choose friend from the list
    sender = select_friend()
    patternimage='[A-Za-z][0-9A-Za-Z\s]*\.jpg$'
    temp=True
    while temp:
        encrypted_image = raw_input("Provide encrypted image : ")
        if (re.match(patternimage,encrypted_image)!= None) :
            temp=False
        else:
            print colored("enter Again!!!",'red')
    try:
        text = secret_message = Steganography.decode(encrypted_image)
        print "message:",text
    except TypeError:
            print colored('image doesnot have any message','red')
    except IOError:
            print colored("image does not exist!!",red)

    # save the messages
    new_chat = {
        'message': secret_message,
        'time': datetime.now(),
        'sent_by_me': False
    }

    friends[sender]['chats'].append(new_chat)
    print colored("your secret message has been saved.",'green')