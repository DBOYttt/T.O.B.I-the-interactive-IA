from asyncio import sleep
from cgitb import text
from signal import pause
import time
import os

print(
    '''
██████████████████████████████████████████████████
█╔╗╔╗╔╦══╦════╦═══╗╪╔╗╪╪╔╦═══╦═══╦════╦═══╦═╗╔═╗╪█
█║║║║║╠╣╠╣╔╗╔╗║╔═╗║╪║║╪╪║║╔══╣╔═╗║╔╗╔╗║╔══╣║╚╝║║╪█
█║║║║║║║║╚╝║║╚╣║╪║║╪║║╪╪║║╚══╣╚══╬╝║║╚╣╚══╣╔╗╔╗║╪█
█║╚╝╚╝║║║╪╪║║╪║╚═╝╠╗║║╔╗║║╔══╩══╗║╪║║╪║╔══╣║║║║║╪█
█╚╗╔╗╔╬╣╠╗╪║║╪║╔═╗║╚╝║║╚╝║╚══╣╚═╝║╪║║╪║╚══╣║║║║║╪█
█╪╚╝╚╝╚══╝╪╚╝╪╚╝╪╚╩══╝╚══╩═══╩═══╝╪╚╝╪╚═══╩╝╚╝╚╝╪█
█╪╪╪╪╪╪╪╪╪╪╪╪╪╔════╦═══╗╔══╗╪╔══╗╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪█
█╪╪╪╪╪╪╪╪╪╪╪╪╪║╔╗╔╗║╔═╗║║╔╗║╪╚╣╠╝╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪█
█╪╪╪╪╪╪╪╪╪╪╪╪╪╚╝║║╚╣║╪║║║╚╝╚╗╪║║╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪█
█╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪║║╪║║╪║║║╔═╗║╪║║╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪█
█╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪║║╔╣╚═╝╠╣╚═╝╠╦╣╠╗╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪█
█╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╚╝╚╩═══╩╩═══╩╩══╝╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪█
█╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪█
██████████████████████████████████████████████████
'''
)

time.sleep(2)

def animate_text(text):
  number_of_characters=1
  running = True
  while running == True:
    print("\n")
    print(text[0:number_of_characters])
    number_of_characters += 1
    if number_of_characters > len(text):
      number_of_characters = 0
    time.sleep(0.1) 
    os.system('clear')
    if number_of_characters == 16:
        if running == True:
           running = False
        
animate_text("what's your name?:")

D1 = input("what's your name?:")
DH = len(D1)

def animate_text(text):
  number_of_characters=1
  running = True
  while running == True:
    print("\n")
    print(text[0:number_of_characters])
    number_of_characters += 1
    if number_of_characters > len(text):
      number_of_characters = 0
    time.sleep(0.1) 
    os.system('clear')
    if number_of_characters == DH + 35 :
        if running == True:
           running = False

animate_text(f'{D1} that a nice name, good to see u :)')

print(f'{D1} that a good name, good to see u :)')

D2 = input('Make Question to T.O.B.I:')

if D2.upper().lower() == 'who are u?' : 
 def animate_text(text):
   number_of_characters=1
   running = True
   while running == True:
    print("\n")
    print(text[0:number_of_characters])
    number_of_characters += 1
    if number_of_characters > len(text):
      number_of_characters = 0
    time.sleep(0.1) 
    os.system('clear')
    if number_of_characters == 28 :
        if running == True:
           running = False
    if number_of_characters == 28 :
      print('im a tobi :) nice to meet u!')
 animate_text('im a tobi :) nice to meet u!')


if D2.upper().lower() == 'who are you?' : 
 def animate_text(text):
   number_of_characters=1
   running = True
   while running == True:
    print("\n")
    print(text[0:number_of_characters])
    number_of_characters += 1
    if number_of_characters > len(text):
      number_of_characters = 0
    time.sleep(0.1) 
    os.system('clear')
    if number_of_characters == 28 :
        if running == True:
           running = False
    if number_of_characters == 28 :
      print('im a tobi :) nice to meet u!')
 animate_text('im a tobi :) nice to meet u!')


if D2.upper().lower() == 'who are you' : 
 def animate_text(text):
   number_of_characters=1
   running = True
   while running == True:
    print("\n")
    print(text[0:number_of_characters])
    number_of_characters += 1
    if number_of_characters > len(text):
      number_of_characters = 0
    time.sleep(0.1) 
    os.system('clear')
    if number_of_characters == 28 :
        if running == True:
           running = False
    if number_of_characters == 28 :
      print('im a tobi :) nice to meet u!')
 animate_text('im a tobi :) nice to meet u!')


if D2.upper().lower() == 'who are u' : 
 def animate_text(text):
   number_of_characters=1
   running = True
   while running == True:
    print("\n")
    print(text[0:number_of_characters])
    number_of_characters += 1
    if number_of_characters > len(text):
      number_of_characters = 0
    time.sleep(0.1) 
    os.system('clear')
    if number_of_characters == 28 :
        if running == True:
           running = False
    if number_of_characters == 28 :
      print('im a tobi :) nice to meet u!')
 animate_text('im a tobi :) nice to meet u!')










