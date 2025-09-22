import requests
import json
import random

# URL of the API
url = "https://sports.core.api.espn.com/v3/sports/football/nba/athletes?limit=20000"

# Send a GET request to the API
response = requests.get(url)

# Initialize player count
count = 0

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract player information
    players = []
    for player in data.get('items', []):
        player_id = player.get('id')
        player_name = player.get('fullName')
        player_age = player.get('age')
        player_height = player.get('displayHeight')
        player_weight = player.get('displayWeight')

        # Birthplace
        birth_place_info = player.get('birthPlace', {})
        city = birth_place_info.get('city', '')
        state = birth_place_info.get('state', '')
        country = birth_place_info.get('country', '')
        birthplace = ", ".join(filter(None, [city, state, country]))

        # Experience
        experience_info = player.get('experience', {})
        years_experience = experience_info.get('years', 'N/A')

        # Jersey Number
        jersey_number = player.get('jersey', 'N/A')

        players.append({
            'id': player_id,
            'name': player_name,
            'age': player_age,
            'height': player_height,
            'weight': player_weight,
            'birthplace': birthplace,
            'experience': years_experience,
            'jersey': jersey_number
        })

    # Print extracted player information
    for player in players:
        print(f"Player ID: {player['id']}, Name: {player['name']}, Age: {player['age']}, "
              f"Height: {player['height']}, Weight: {player['weight']}, Birthplace: {player['birthplace']}, "
              f"Experience: {player['experience']} years, Jersey #: {player['jersey']}")
        count += 1
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

print("Player Count:", count)

random_playerPick = random.choice(players)


# Prompt the user to input a search name
# search_name = input("Enter player name to search: ")

def player_pick():
    player = random_playerPick

    print(f"Player ID: {player['id']}, Name: {player['name']}, Age: {player['age']}, "
          f"Height: {player['height']}, Weight: {player['weight']}, Birthplace: {player['birthplace']}, "
          f"Experience: {player['experience']} years, Jersey #: {player['jersey']}")

    return str("ID# " + player['id'] + " - " + str(player['name']) +
               f"  " + " Age: " + str(player['age']) + " Height: " + str(player['height']) + " Weight: " + str(
        player['weight']) + " ")


def player_pick_name():
    return random_playerPick['name']
