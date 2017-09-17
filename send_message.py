from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends

def send_message():
    # choose a friend from the list.
    friend_choice = select_friend()

    # prepare the message
    original_image = raw_input("Provide the name of the image to hide the message : ")
    output_image = raw_input("Provide the name of the output image  : ")
    text = raw_input("Enter your message here : ")
    # Encrypt the message
    Steganography.encode(original_image, output_image, text)

    # Successful message
    print "Your message encrypted successfully."

    # save the messages
    new_chat = {
        'message': text,
        'time': datetime.now(),
        'sent_by_me': True
    }

    friends[friend_choice]['chats'].append(new_chat)
    print "your secret message is ready."