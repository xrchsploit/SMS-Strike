# -*- coding: utf-8 -*-

import smtplib
import getpass
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    NORMAL = '\033[0m'




def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

# Banner

print(bcolors.RED + '''
  ██████  ███▄ ▄███▓  ██████      ██████ ▄▄▄█████▓ ██▀███   ██▓ ██ ▄█▀▓█████ 
▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒    ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒ ██▄█▒ ▓█   ▀ 
░ ▓██▄   ▓██    ▓██░░ ▓██▄      ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▓███▄░ ▒███   
  ▒   ██▒▒██    ▒██   ▒   ██▒     ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░▓██ █▄ ▒▓█  ▄ 
▒██████▒▒▒██▒   ░██▒▒██████▒▒   ▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ █▄░▒████▒
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ▒ ▒▒ ▓▒░░ ▒░ ░
░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░   ░ ░▒  ░ ░    ░      ░▒ ░ ▒░ ▒ ░░ ░▒ ▒░ ░ ░  ░
░  ░  ░  ░      ░   ░  ░  ░     ░  ░  ░    ░        ░░   ░  ▒ ░░ ░░ ░    ░   
      ░         ░         ░           ░              ░      ░  ░  ░      ░  ░
                                                                             
IG - xrchsploit

** IN ORDER FOR THIS TO WORK YOU WILL NEED A VALID EMAIL ALONG WITH LESS SECURE APPS ENABLED **
How to turn on less secure apps: https://www.youtube.com/watch?v=BPFkiLnN6h0
''')

bcolors.NORMAL

def options():
    global phone_number, phone_extension, phone_number_user, repeater, message
    phone_number = input(bcolors.OKGREEN + "➫ What is the phone number without the dashes and parentheses? " + bcolors.NORMAL)
    if not phone_number:
        print(bcolors.RED + "⇝ You need to specify a phone number! Exiting" + bcolors.NORMAL)
        exit()
    if "-" in phone_number:
       print(bcolors.RED + '⇝ Detected one of the following [- ()] ! Exiting' + bcolors.NORMAL)
       exit()
    elif '(' in phone_number:
        print(bcolors.RED + '⇝ Detected one of the following [- ()] ! Exiting' + bcolors.NORMAL)
        exit()
    elif ')' in phone_number:
        print(bcolors.RED + '⇝ Detected one of the following [- ()] ! Exiting' + bcolors.NORMAL)
        exit()
    else:
        pass
    phone_extension = input(bcolors.MAGENTA + "⇝ What is the phone numbers extension? Leave this blank if you dont know it. " + bcolors.NORMAL)
    if not phone_extension:
        print(bcolors.CYAN + "➫ To find it go to https://www.freecarrierlookup.com/" + bcolors.NORMAL)
        exit()
    elif '@' not in phone_extension:
        print(bcolors.RED + '➫ You need to include the @ symbol in front of the extension, to get it go to https://www.freecarrierlookup.com/ ! Exiting.' + bcolors.NORMAL)
        exit()
    else:
        pass
    message = input(bcolors.CYAN + "What message would you like to send? " + bcolors.NORMAL)
    phone_number_user = phone_number + phone_extension
    repeater = input("How many messages? ")
    print(bcolors.CYAN + "Working..." + bcolors.NORMAL)

def email_details():
    global message_final
    global email, password
    email = input("What is your email? ")
    password = getpass.getpass("Enter your emails password: ")
    message_final = "From: {} \r\nTo: {} \r\n\r\n {}".format(email, phone_number_user, message)

def sender_func():
    for x in range(int(repeater)):
        try:
            spam = smtplib.SMTP("smtp.gmail.com:587")
            spam.starttls()
            spam.login(email, password)
            spam.sendmail(email, phone_number_user, message_final)
            print(spam.sendmail())
        except:
            print("Sending!")

def main():
    options()
    email_details()
    sender_func()

main()
