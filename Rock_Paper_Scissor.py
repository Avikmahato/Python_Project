import random
def gameWin(a,b):
    if (a=="Rock" and b=='Scissor') or (a=='Scissor' and b=='Paper') or (a=='Paper' and b=='Rock'):
        return False
    elif (a=='Rock' and b=='Paper') or (a=='Scissor' and b=='Paper') or (a=='Scissor' and b=='Rock'):
        return True
    else:
        return None
point=0
for i in range(10):
    com=random.randint(1,3)
    if com==1:
        cm_s="Rock"
    elif com==2:
        cm_s="paper"
    else:
        cm_s="Scissor"
    ch=input("Enter Rock ,Paper Or Scissor :")
    print("Computer Chosse :",cm_s)
    print("You Choose      :",ch)
    ch=ch.capitalize()
    Result=gameWin(cm_s,ch)
    if Result==1:
        print("You Win")
        point+=1
    elif Result==0:
        print('You Loss')
        point-=1
    else:
        print("Tied")
    print("\t\t\tPOINT------->",point)
