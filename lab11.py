#1 open 
file = open("To-Do.txt", "a+", encoding="UTF-8")


while True:
    UserNote = input("Do you want to add a new To-Do item yes or no?? ")
    if UserNote == "y":
        UserItem = input("Please write your item: ")
        file.write(UserItem + "\n")
    elif UserNote == "n" :
        UserNo =input("Do you want to list your To-Do items: ")
        if UserNo == "y":
            file.seek(0)
            print(file.read())
        else: 
            print("thank you for using the To-Do program, come back again soon")
            break
    file.close()
    
   
    
    