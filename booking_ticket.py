# book a tiket
# cancel a ticket
# view All booking
import random
import time

t=True
bookedtick={}
def book():
    name=(input("enter your name: "))
    ticknum=random.randint(503245,999999)
    bookedtick.update({name:ticknum})
    print("your ticket has been booked")
    print(f"your ticket number is {ticknum}")

def cancel():
        usernaem=input("enter the username you entered while creating ticket: ")
        print("searching for your name------")
        time.sleep(2)

        try:
            del bookedtick[f"{usernaem}"]
            print("your ticket has been canceled")
        except:
            print("your username is incorrect")

def view():
    print(bookedtick)



while t!=False:
    print('''
    1)book a tiket
    2)cancel a ticket
    3)view All booking''')
          
          
    try:
        user=int(input("enter from the above: "))
    except ValueError:
        print("enter a valid int option ")
        continue

    if user == 1:
        book()
    
    elif user== 2:
        cancel()

    
    elif user==3:
        print(bookedtick)
    

        
        
        




