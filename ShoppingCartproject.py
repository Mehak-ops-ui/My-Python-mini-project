shopping_cart = {"Teddy":500,
              "Jean":1000,
              "Bedminton":800,
              "Mixer":4000,
              "Saree":8000
              }
categories = {"toys","clothes","machine"}

while True:
    print("1.Add Items : ")
    print("2.Remove Items : ")
    print("3.Track Items : ")
    print("4.Compute total bill of Items : ")

    choice = int(input("Enter your chice betwwn (1-4) : "))

    if choice == 1:
        item = input("Enter item to add : ")
        price = int(input("Price of this item :"))
        category = input("Enter the catagory : ")
        shopping_cart[item]= price
        categories.add(item)
        print("Your item is added!")

    elif choice == 2:
        item = input("Enter the item to remove : ")
        if item in shopping_cart:
         del shopping_cart[item] 
         print("Item deleted successfully")
        else:
         print("Item not found")
    elif choice == 3:
       print("unique catagories : ")
       print(categories)
       
    elif choice == 4:
       total = sum(shopping_cart.values())
       print("Total Bill :" , total)

    else:
     print("please choose between (1-4)")       

       




