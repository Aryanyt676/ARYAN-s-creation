from time import sleep
t=True

while (t==True):
    try:

        user=input("enter something: ")
    except:
        print("enter a valid number")

    print("processing..")
    sleep(2)
    print("analyzing every possibilities...")
    sleep(float(0.5))
    print("-------------")
    sleep(3)
    print("3")
    sleep(float(0.4))
    print("2")
    sleep(float(0.5))
    print("1")
    print(f"were you thinking of -{user}")
    print(f"right?\n1)yes\n2)no")

    review=int(input("enter:"))
    if review==1:
        t=False
        print("thanks for that")
    else:
       continue
