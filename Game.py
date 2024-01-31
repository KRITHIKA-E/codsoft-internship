import random
print("*WELCOME TO THE GAME*\n")
def main():
    while True:
        print("1.rock")
        print("2.paper")
        print("3.scissors\n")

        choice=input("enter your choice: ")
        
        ch=["rock","paper","scissors"]
        string=random.choice(ch)
        print("\ncomputers choice: ",string)
        
        if (choice=="rock" and string=="paper"):
            print("\nyou lose\n")
        elif(choice=="rock" and string=="scissors"):
            print("\nyou win\n")
        elif(choice=="paper" and string=="rock"):
            print("\nyou win\n")
        elif(choice=="paper" and string=="scissors"):
            print("\nyou lose\n")
        elif(choice=="scissors" and string=="rock"):
            print("\nyou lose\n")
        elif(choice=="scissors" and string=="paper"):
            print("\nyou win\n")
        else:
            print("\ntie\n")
            
        user=input('do you want to continue the game (yes/no): ')
        if(user=='yes'):
            main()
        elif(user=='no'):
            print("\nThank you for playing goodbye!!")
        break
    else:
        print("\nenter a valid choice\n")
        main()

if __name__=="__main__":
    main()
