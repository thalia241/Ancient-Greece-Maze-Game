# Charity Deel

# Dictionary
rooms = {
    'Maze Entrance': {'East': "Demeter's Garden"},
    "Demeter's Garden": {'North': "Athena's Library", 'South': "Ares's Weaponry", 'East': "Fate's Corridors",
                         'West': "Maze Entrance", 'item': "Golden Apple"},
    "Athena's Library": {'South': "Demeter's Garden", 'East': "Zeus's Throne Room", 'item': 'Scroll'},
    "Zeus's Throne Room": {'West': "Athena's Library", 'item': 'Lightning Bolt'},
    "Fate's Corridors": {'West': "Demeter's Garden", 'North': "Hecate's Corner", 'item': 'Ball of Yarn'},
    "Hecate's Corner": {'South': "Fate's Corridors", 'item': 'Potion of Strength'},
    "Ares's Weaponry": {'North': "Demeter's Garden", 'East': "Daedalus's Lair", 'item': ['Sword', 'Club']},
    "Daedalus's Lair": {'West': "Ares's Weaponry", 'item': 'Minotaur'}  # Villain
}


# Show status
def current_status(current_room, inventory):
    print('You are in the', current_room)
    print('Inventory:', inventory)
    if current_room in rooms and 'item' in rooms[current_room]:
        print('You see a', rooms[current_room]['item'])


# Move Between Rooms
def move(prompt, current_room):
    if current_room in rooms and prompt in rooms[current_room]:
        current_room = rooms[current_room][prompt]
        print('You moved to the', current_room)
    else:
        print('You cannot go that way.')
    return current_room


# Collect Items
def pickup_item(inventory, current_room):
    if current_room in rooms and 'item' in rooms[current_room]:
        item = rooms[current_room]['item']
        inventory.append(item)
        print('You picked up the', item)
        del rooms[current_room]['item']
    else:
        print('There is no item to pick up here.')
    return inventory


# Instructions
Instructions = "Welcome to the Maze. Collect all 6 items and defeat the Minotaur to win. To move, type: North, South, East, or West. To collect items, type: get 'item name'. To exit the game, type: Exit"


def main():
    current_room = 'Maze Entrance'
    inventory = []
    directions = {'North', 'South', 'East', 'West'}

    print(Instructions)
# Game Loop
    while True:
        current_status(current_room, inventory)

        if current_room == "Daedalus's Lair":
            if inventory ==
                print("Congratulations! You have entered Daedalus's Lair and defeated the Minotaur!")
            else:
                print("Oh no! You were slain by the Minotaur and lost the game!")
            break

        prompt = input('What would you like to do?')

        if prompt.lower() == 'exit':
            print('Thanks for playing!')
            break
        elif prompt in directions:
            current_room = move(prompt, current_room)
        elif prompt.startswith('get '):
            inventory = pickup_item(inventory, current_room)
        else:
            print('Invalid move. Try again.')


if __name__ == '__main__':
    main()
