from colorama import Fore, Back, Style, init
init(autoreset=True)  
import time
import random 

def result(r,attempts,secret_number):
    with open("result.txt","a") as file:
        file.write(f"{r}   | Attempts : {attempts} |  Secret Number : {secret_number}|\n")
def history():
   with open("result.txt") as file:
      data=file.read()
      if data : 
        print(Fore.GREEN+data)
      else :
         print(Fore.RED+"No History Recorded\n")

def stat_storing(s):
    try:
        with open("stats.txt", "r") as f:
            lines = f.readlines()
            win = int(lines[0].split(":")[1].strip())
            losses = int(lines[1].split(":")[1].strip())
    except:
        win = 0
        losses = 0

    if s == "Win":
        win += 1
    else:
        losses += 1

    with open("stats.txt", "w") as f:
        f.write(f"Wins : {win}\nLoss : {losses}")
    
def stat():
    print(Fore.CYAN + "\n📊 Game Stats:")
    try:
        with open("stats.txt", "r") as f:
            content=f.read().strip()
            if content:
              print(Fore.YELLOW + content)
              print()
            else :
               print(Fore.RED+"No Stats Found Yet\n")
    except:
        print(Fore.LIGHTBLACK_EX + "No stats found yet.")

def clear():
   with open("result.txt", "w"), open("stats.txt", "w"):
        pass
   print(Fore.RED + "\n🧹 History and stats cleared!")

def game():
    print("="*35)
    print(Back.WHITE+ Fore.BLACK+"        NUMBER GUESSING GAME       ")
    print("="*35)
    secret_number=random.randint(1,15)
    print(Fore.YELLOW+"You Have 7 Tries to Guess the secret number(Between 1 to 15)")
    for i in range(1,8):
        guess=int(input(f"Enter your attempt no {i} : "))
        while True:
           if guess>15 or guess<0:
              print(Fore.RED+"Invalid number selected.. (0-15) ")
              guess=int(input("Enter Again : "))
           else :
             break
        if guess > secret_number :
            print(Fore.GREEN+"checking...")
            time.sleep(0.3)
            print(Fore.RED+"Wrong Guess ")
            print(Fore.YELLOW+" Hint...! A Lesser Number ") 
        elif guess < secret_number :
          print(Fore.GREEN+"checking...")
          time.sleep(0.3)
          print(Fore.RED+"Wrong Guess ")
          print(Fore.YELLOW+" Hint...! A Greater Number ") 
        else :
            print(Back.GREEN+Fore.BLACK+f"    Congratulations..! 🎉   ")
            print(Fore.GREEN+f"You Guessed it Right in your attempt no {i}")
            print()
            result(" Win",i,secret_number)
            stat_storing("Win")
            break
    else : 
        print(Fore.BLACK+Back.RED+"You LOOSE")
        print(Fore.BLACK+Back.YELLOW+f"The Correct Number was : {secret_number}")
        result("Lose",7,secret_number)
        stat_storing("Lose")

while True:
    print(Fore.GREEN+"1. Play Game")
    print(Fore.CYAN+"2. Show Game Stats ")
    print(Fore.CYAN+"3. Previous Games History")
    print(Fore.CYAN+"4. Clear All Histroy")
    print(Fore.RED+"5. EXIT Game ")

    C=int(input("Enter Your choice : "))
    if C==2:
     stat()
    elif C==3:
     history()
    elif C==4: 
     clear()
    elif C==1:
     game()
    elif C==5:
     print(Fore.GREEN + "\nThanks for playing! 🎉")
     break
    else : 
       print(Fore.RED+"Invalid Choice...Enter Again(1-5) : ")





