shopping_list = []

def show_help():
    print("TOO SEE YOUR CURRENT LIST ENTER: SHOW")
    print("IF YOU ARE DONE ENTER: DONE")
    print("IF YOU NEED HELP ENTER: HELP")
    
def add_item(new_item):
    shopping_list.append(new_item)
    print(new_item, "was added to your list and have {} items in your shopping list".format(len(shopping_list)))
    

def show_items():
    for items in shopping_list:
        print("===>", items)


show_help()

while True:
  
    new_item = input("whats do you need from the supermarket >   ")
    if new_item.lower() =="done":
        break
        
    elif new_item.lower() == "show":
        print("HERE YOUR CURRENT LIST")
        show_items()
        continue
            
    elif new_item.lower() == "help":
        show_help()
        continue
    elif new_item == "":
        continue
    
    add_item(new_item)

print("HERE YOUR FINAL SHOPPING LIST")

show_items()

print("THANK YOU FOR SHOPPING AT TESCO AND COME AGAIN")
        
        
       
