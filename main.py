import random
game_name = "Soyed's Quest"
print(f"Welcome to {game_name}!")
print("=" * 25)
name = input("What is your name, adventurer? ")
print(f"Great {name}! Let's begin your quest!")
player = {
    "name": name,
    "health": 100,
    "coin" : 0
}
print(f"{player['name']}, you start with {player['health']} health and {player['coin']} coins.")

def get_random_event():
    events = ["find a coin", "encounter monster", "nothing"]
    return random.choice(events)
def update_stats(player, event):
    if event == "find a coin":
        player["coin"] += 1
        print(f"{player['name']} found a coin, now has {player['coin']} coins.")
    elif event == "encounter monster":
        player["health"] -= 1
        print(f"{player['name']} got hurt during the combat with a monster, health is now {player['health']}.")
    else:
        print(f"{player['name']} wandered around... nothing happened.") 
for _ in range(3):
    event = get_random_event()
    print(f"While exploreing, you found: {event}")
    update_stats(player,event)