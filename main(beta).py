from asyncio import sleep
from cgitb import text
import imp
import json
from signal import pause
import time
import os
from x_def import x
from x_def import z
import json



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


while 1 : 
  D2 = input('Make question to tobi:')
  if D2.upper().lower() == 'who are u?' :
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == 28: 
          runing = False 
        if number_of_characters == 28:
          print('im a tobi :) nice to meet u!')
    animate_text('im a tobi :) nice to meet u!')

  if D2.upper().lower() == 'who are u' :
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == 28: 
          runing = False 
        if number_of_characters == 28:
          print('im a tobi :) nice to meet u!')
    animate_text('im a tobi :) nice to meet u!')
  if D2.upper().lower() == 'who are you?' :
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == 28: 
          runing = False 
        if number_of_characters == 28:
          print('im a tobi :) nice to meet u!')
    animate_text('im a tobi :) nice to meet u!')

  if D2.upper().lower() == 'who are you' :
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == 28: 
          runing = False 
        if number_of_characters == 28:
          print('im a tobi :) nice to meet u!')
    animate_text('im a tobi :) nice to meet u!')
 
  if D2.upper().lower() == 'what your name?' :
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == 28: 
          runing = False 
        if number_of_characters == 28:
          print('im a tobi :) nice to meet u!')
    animate_text('im a tobi :) nice to meet u!')
  
  if D2.upper().lower() == 'what your name' :
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == 28: 
          runing = False 
        if number_of_characters == 28:
          print('im a tobi :) nice to meet u!')
    animate_text('im a tobi :) nice to meet u!')

  if D2.upper().lower() == 'what you name' :
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == 28: 
          runing = False 
        if number_of_characters == 28:
          print('im a tobi :) nice to meet u!')
    animate_text('im a tobi :) nice to meet u!')

  if D2.upper().lower() == 'what you name?' :
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == 28: 
          runing = False 
        if number_of_characters == 28:
          print('im a tobi :) nice to meet u!')
    animate_text('im a tobi :) nice to meet u!')

  y = json.dump(D2)
     
  if D2.upper().lower() == 'exit()' :
    break
 
  if D2.upper().lower() != x:

   if D2.upper().lower() in y:
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == len(y): 
          runing = False 
        if number_of_characters == len(y):
          print(y)
    animate_text(y)
  
  if D2.upper().lower() not in y:
    def animate_text(text) : 
      number_of_characters=1
      runing = True
      while runing == True:
        print('\n')
        print(text[0:number_of_characters])
        number_of_characters += 1 
        if number_of_characters > len(text):
          number_of_characters = 0
        time.sleep(0.1)
        os.system('clear')
        if number_of_characters == len("i can't understund :("): 
          runing = False 
        if number_of_characters == len("i can't understund :("):
          print("i can't understund :(")
    animate_text("i can't understund :(") 