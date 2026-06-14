contacts = {"Alex":567879865,
            "sita":579202299,
            "Gita":781458907,
            "Mahi":896755780,
            "jiya":994578432
            }

phone_number = set(contacts.values())

while True:
    print("1.Add contats:")
    print("2.Search contats:")
    print("3.Update contats:")
    print("4.Delete contats:")
    
    choice = int(input("Enter your choice from (1-4): "))
    
    if choice == 1:
        name = input("Enter name : ")
        number = int(input("Enter phone number :"))
        if number in phone_number:
            print("Already saved !..")
        else:
            contacts[name]= number
            phone_number.add(number)
            print("Add Successful!")

    elif choice == 2:
        name = input("Enter name for search : ")
        if name in contacts:
            print("name",name)
            print("number",contacts[name])
        else:
            print("Contact not found!!!")

    elif choice == 3:
        name = input("Enter the name to update : ")
        if name in contacts:
            new_number = int(input("Enter the new number : "))
            if new_number in phone_number:
                print("Already Exists !!")
            else:
                old_number = contacts[name]
                phone_number.remove(old_number)
                phone_number.add(new_number)
                print("Update Successfull")
        else:
         print("Contact not found!")
    elif choice == 4:
        name = input("Enter name to delete : ")
        if name in contacts:
            phone_number.remove(name)
            del contacts[name]
            print("Contact Name delete successfully")
        else:
            print("Contact not found: ")   

    else:
        print("Please choose number between (1-4)")         
        
