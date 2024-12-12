from random import randint

computer=randint(1,100)

a=1
n=0
while a!=2:

    try:
        userinput=int(input("try to guess: "))
    
    except ValueError:
        print("enter a valid number")
        continue
    n+=1

    if userinput==computer:

        a=2
        print("congratulation! you guesed it correct")
   


    elif userinput==int:
        print("enter a valid number")

    elif userinput>computer:
        print("lower number please")
    
    elif userinput<computer:
        print("Higher number please")


if n==1:
    print(f"you took only 1 guess to guess the number {computer}")
else:

    print(f"you took {n} guesses to guess the number {computer}")