import random
number=random.randint(1,100)
result=False
def medium_easy():
  global lives
  global result
  while not result:
    while not lives==0:
      chosen=int(input(f"You have {lives} attempts remaining to guess the number: "))
      if not chosen==number:
        if abs(chosen-number)<10 and chosen<number:
          print("You are near, just add some more...")
        elif abs(chosen-number)<10 and chosen>number:
          print("You are near, just reduce some...")
        elif abs(chosen-number)>25 and chosen<number:
          print("You are very far, add a lot...")
        elif abs(chosen-number)>25 and chosen>number:
          print("You are very far, reduce a lot...")
        elif chosen<number:
          print("You are low...")
        elif chosen>number:
          print("You are high...")
        lives-=1
      else:
        print("You have guessed the number. Let's party...")
        lives=0
    if not chosen==number:
      print(f"Better luck next time, by the way the number in my mind is {number}")
    result=True
def hard():
  global lives
  global result
  while not result:
    while not lives==0:
      chosen=int(input(f"You have {lives} attempts remaining to guess the number: "))
      if not chosen==number:
        if chosen<number:
          print("Too low...")
        elif chosen>number:
          print("Too high...")
        lives-=1
      else:
        print("You have guessed the number. Let's party...")
        lives=0
    if not chosen==number:
      print(f"Better luck next time, by the way the number in my mind is {number}")
    result=True
print('''
   _____                                _     _                                            _                   
  / ____|                              | |   | |                                          | |                  
 | |  __   _   _    ___   ___   ___    | |_  | |__     ___     _ __    _   _   _ __ ___   | |__     ___   _ __ 
 | | |_ | | | | |  / _ \ / __| / __|   | __| | '_ \   / _ \   | '_ \  | | | | | '_ ` _ \  | '_ \   / _ \ | '__|
 | |__| | | |_| | |  __/ \__ \ \__ \   | |_  | | | | |  __/   | | | | | |_| | | | | | | | | |_) | |  __/ | |   
  \_____|  \__,_|  \___| |___/ |___/    \__| |_| |_|  \___|   |_| |_|  \__,_| |_| |_| |_| |_.__/   \___| |_|   
                                                                                                               
                                                                                                               
''')
print("Welcome to the number guessing game\nI have a number between 1 and 100 in my mind")
difficulty=input("Choose difficulty,  'easy' or 'medium' or 'hard' and try to read my mind\n:").lower()
if difficulty=="easy":
  lives=10
  medium_easy()
elif difficulty=="hard":
  lives=5
  hard()
elif difficulty=="medium":
  lives=5
  medium_easy()
else:
  print("I can't understand you. Please type 'easy', 'medium' or 'hard'")