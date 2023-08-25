import random
from colorama import Back,Style,Fore
com=random.randint(1,100)
Step=0
while 7:
    you=int(input("Guess a Number And Check Your Luck Point:"))
    Step+=1
    if you>com and you<101:
        print(Fore.GREEN+"\t\t************Your Choise Number Is High************")
    elif you<com and you>0:
        print(Fore.LIGHTBLUE_EX+'\t\t*************Your Choise Is Low**************')
    elif you<1 or you >100:
        print(Fore.RED+"********Please Choose Number In Between 1 To 100********")
    else:
        print("Your Guess Is Correct")
        print(Fore.CYAN+"_______Your Luck Point Is:",100-Step,'_______')
        exit()