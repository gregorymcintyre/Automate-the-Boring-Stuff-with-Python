
#inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    item_total = 0
    print('inventory:\n')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total+=v
    print('\ntotal number of items ' + str(item_total) + '\n')

def addtoInventory(inventory, addItems):
    for i in addItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inv)
addtoInventory(inv, dragonLoot)
displayInventory(inv)
