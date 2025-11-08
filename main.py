import random

# Global settings and state
game_name = "Soyed's Quest"
name = "Tester"
events = ["find a coin", "encounter monster", "nothing"]
map_size = 9

player = {
    "name": name,
    "health": 100,
    "coin": 0,
    "x": 0,
    "y": 0
}

def get_random_event():
    return random.choice(events)

def check_event():
    """
    Applies a random event to the global player.
    Per instructions, this function does not print anything.
    It returns a short message describing the event so the caller can print it.
    """
    global player
    event = get_random_event()
    if event == "find a coin":
        player["coin"] += 1
        return "You found a coin!"
    elif event == "encounter monster":
        player["health"] -= 1
        return "You encountered a monster and lost 1 health."
    else:
        return "You wandered around... nothing happened."

def draw_ui(x, y):
    """
    Draw the map and player stats.
    x is column (horizontal), y is row (vertical).
    Player 'C' at (x,y). Gate 'M' at (map_size-1, map_size-1).
    """
    print("=" * 25)
    for i in range(map_size):        # i = row index (y)
        row_cells = []
        for j in range(map_size):    # j = column index (x)
            if j == x and i == y:
                row_cells.append("C")
            elif i == map_size - 1 and j == map_size - 1:
                row_cells.append("M")
            else:
                row_cells.append(".")
        # join with space and print the row
        print(" ".join(row_cells))
    print("=" * 25)
    print(f"Health: {player['health']}")
    print("-" * 25)
    print(f"Coin: {player['coin']}")
    print("=" * 25)

def move(direction):
    """
    Update player's x,y according to direction with bounds checking.
    Returns True if movement occurred, False otherwise.
    """
    moved = False
    if direction == 'w' and player['y'] > 0:
        player['y'] -= 1
        moved = True
    elif direction == 's' and player['y'] < map_size - 1:
        player['y'] += 1
        moved = True
    elif direction == 'a' and player['x'] > 0:
        player['x'] -= 1
        moved = True
    elif direction == 'd' and player['x'] < map_size - 1:
        player['x'] += 1
        moved = True
    return moved

def main():
    print(f"Welcome to {game_name}!")
    print("=" * 25)
    print(f"Great {player['name']}! Let's begin your quest!")
    print(f"{player['name']}, you start with {player['health']} health and {player['coin']} coins.")
    draw_ui(player['x'], player['y'])

    direction = input("Your next move (w/a/s/d/q): ").strip().lower()
    while direction != 'q':
        if direction not in ('w', 'a', 's', 'd'):
            print("Invalid input. Use w/a/s/d to move or q to quit.")
        else:
            moved = move(direction)
            if not moved:
                print("You cannot move that way!")
            else:
                # Check if reached gate
                if player['x'] == map_size - 1 and player['y'] == map_size - 1:
                    print("Congratulations! You reach the gate for next level.")
                    break
                # Apply event and print its outcome
                message = check_event()
                print(message)
        draw_ui(player['x'], player['y'])
        # Early exit if health falls to 0 or below
        if player['health'] <= 0:
            print(f"{player['name']} has perished in the quest. Game over.")
            break
        direction = input("Your next move (w/a/s/d/q): ").strip().lower()

if __name__ == '__main__':
    main()

