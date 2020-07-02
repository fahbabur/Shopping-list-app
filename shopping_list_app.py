# Original code by fahbabur, Edited by Jordan Leich on 6/12/2020, email me at jordanleich@gmail.com to create and 
# code together. 


shopping_list = []
list_price = []


def restart():
    print()
    user_choice = str(input("Do you want to make another shopping list (yes | no): "))
    print()

    if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'y':
        print('Restarting Shopping List...')
        print()
        main()

    else:
        print('Thanks for using our Shopping List!')
        print()
        quit()


def show_help():
    print()
    print("To see your list: (Show) ")
    print()
    print("If you are done with your list: (Done) ")
    print()
    print("If you need help (Help) ")
    print()


def add_item(new_item, item_price):
    shopping_list.append(new_item)
    list_price.append(item_price)
    print(new_item,
          "was added to your list and you now have {} items in your shopping list.".format(len(shopping_list)))
    print()


def show_list():
    for items in shopping_list:
        print("> ", items)

    print('Grand Total:', sum(list_price))
    restart()


show_help()


def main():
    while True:
        new_item = input("Item name: ")
        print()
        item_price = float(input('Price: '))
        print()
        if new_item == "done" or new_item == 'Done' or new_item == 'd':
            show_list()
            break

        elif new_item == "show" or new_item == 'Show' or new_item == 's':
            print("Current list: ")
            show_list()
            continue

        elif new_item == "help" or new_item == 'Help' or new_item == 'h':
            show_help()
            continue

        elif new_item == '' and item_price == '':
            continue

        add_item(new_item, item_price)


main()

print("Here is your final shopping list")
print()

show_list()

print()
