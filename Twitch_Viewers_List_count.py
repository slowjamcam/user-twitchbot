import requests

# Replace with your channel (NO # and all lowercase)
CHANNEL_NAME = 'slowjamcam'

def get_chatters():
    url = f"https://tmi.twitch.tv/group/user/{CHANNEL_NAME.lower()}/chatters"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Combine viewers + moderators + VIPs, etc.
        chatters = []
        for role_list in data["chatters"].values():
            chatters.extend(role_list)

        return chatters

    except requests.exceptions.RequestException as e:
        print("Error getting viewers:", e)
        return []
