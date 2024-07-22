'''

1 for snake
-1 for water
0 for gun
'''
import random

Computer_choice=random.choice([-1,0,1])
Your_choice =input("Enter your choice:")
Choices={"s": 1,"w":-1,"g":0}

You=Choices[Your_choice]


print(f"You chose {(You)}\n Computer chose  {(Computer_choice)}")

if(Computer_choice==You):
    print("Tie")
else:
    if(Computer_choice==1 and You==-1):
       print("You lose!")

    elif(Computer_choice==1 and You==0):
        print("You Win!")

    if(Computer_choice==-1 and You==1):
        print("You Win!")

    elif(Computer_choice==-1 and You==0):
         print("You lose!")

    if(Computer_choice==0 and You==1):
         print("You lose!")

    elif(Computer_choice==0 and You==-1):
         print("You Win!")

    else:("Wrong Input") 


