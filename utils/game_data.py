import json
import os
from classes.player import Player
from classes.item import Item, WEAPON_POOL, POTION_POOL

SAVE_FILE = "save_data.json"

def save_game(player):
    # Nested dictionary w/ player to save stats
    save_data = {
        "player": {
            "name": player.name,
            "level": player.level,
            "hp": player.hp,
            "max_hp": player.max_hp,
            "strength": player.strength,
            "exp": player.exp,
            "inventory": [],
            "equipped_weapon": None
        }
    }

    for item in player.inventory:
        item_data = {
            "name": item.name,
            "type": item.item_type,
            "value": item.value
        }
        # Saves items in inventory to save data
        save_data["player"]["inventory"].append(item_data)

    if player.equipped_weapon:
        save_data["player"]["equipped_weapon"] = {
            "name": player.equipped_weapon.name,
            "type": player.equipped_weapon.item_type,
            "value": player.equipped_weapon.value
        }

    # Writes save to file
    try:
        with open(SAVE_FILE, "w") as saved_file:
            json.dump(save_data, saved_file, indent=4)
        print("Game Saved.")
    # Returns error if exception is raised
    except Exception as e:
        print(f"Error saving game: {e}")


def load_game():

    try:
        # Checks for save file
        if not os.path.exists(SAVE_FILE):
            print("No save file found.")
            return None
        
        with open(SAVE_FILE) as saved_file:
            save_data = json.load(saved_file)

        player_data = save_data["player"]
        player = Player(player_data["name"])

        # Restore player stats
        player.level = player_data["level"]
        player.hp = player_data["hp"]
        player.max_hp = player_data["max_hp"]
        player.strength = player_data["strength"]
        player.exp = player_data["exp"]

        # Recreate inventory items
        for item_data in player_data["inventory"]:
           # Find matching item type from pools
           if item_data["type"] == "WEAPON":
               pool = WEAPON_POOL
           else:
               pool = POTION_POOL
               
           # Find matching item from pool
           for item_type in pool:
               if item_type.name == item_data["name"]:
                   player.add_item(Item(item_type))
                   break

       # Restore equipped weapon if any
        if player_data["equipped_weapon"]:
           weapon_data = player_data["equipped_weapon"]
           for weapon_type in WEAPON_POOL:
               if weapon_type.name == weapon_data["name"]:
                   player.equipped_weapon = Item(weapon_type)
                   break
               
        print("Saved game loaded successfully.")
        return player
    
    except Exception as e:
        print(f"Error loading game: {e}")
        return None
    

def delete_save():
   try:
       if os.path.exists(SAVE_FILE):
           os.remove(SAVE_FILE)
           print("Save file deleted!")
       else:
           print("No save file found!")
   except Exception as e:
       print(f"Error deleting save file: {e}")