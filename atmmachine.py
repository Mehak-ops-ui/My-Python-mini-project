pin = 1234
balance = 6000

entered_pin = int(input("Enter the PIN : "))
if entered_pin == pin :

    while True:
        print("=====ATM MENU=====")
        print("1 Check your Balance ")
        print("2 Deposit " )
        print("3 Withdraw ")
        print("4 Exit ")

        choice = input("Enter your Choice : ")
        if choice=="1":
            print("Current balance : ", balance)


        elif choice=="2":
            amount = float(input("Enter the amount to deposit : "))   
            balance += amount
            print("Deposit Succesfull !!!.....")
            print("Updated balance : ",balance)

        elif choice=="3":
            amount = float(input("Enter the amount to Withdraw : "))

            if amount <= balance:
                balance -= amount
                print("Withdrawl Successfull!!!....")
                print("Remaining Balance : ",balance)

            else:
                print("Insufficient Balance*********...")
        elif choice=="4":
            print("Thankyou for using SBI ATM!!!!")
            break
    
    else:
            print("Invalid choice !!")

else:
        print("Incorrect PIN!!***")


