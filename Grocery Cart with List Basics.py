print("Welcome to the Grocery Store!")
list_items = []
while True:
    new_item = input("Add items into the grocery list? Type 'Q' to quit: ")
    if new_item == "q":
        print("thank you for using my grocery\nYour final grocery list is as follows:")
        break
    else:
        list_items.append(new_item)
        #print(list_items)


for item in sorted(list_items):
    print("-"+item)
