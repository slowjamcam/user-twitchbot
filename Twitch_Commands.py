# commands.py
import time
import random
import numbers
import datetime
from password_gen import generate_password
from NBAplayers import player_pick, player_pick_name

seen_chatters = set()  # Still global, but accessible here


class CooldownCommand:
    def __init__(self, func, cooldown_seconds):
        self.func = func
        self.cooldown = cooldown_seconds
        self.last_used = 0 # Timestamp of last use

    def __call__(self, user):
        now = time.time()
        if now - self.last_used>= self.cooldown:
            self.last_used = now
            return self.func(user)
        else:
            remaining = int(self.cooldown - (now - self.last_used))
            return f"Please wait {remaining} seconds before using that again."


class GlobalOneTimeCommand:
    def __init__(self, func, cooldown_seconds):
        self.func = func
        self.cooldown = cooldown_seconds
        self.used = False
        self.reset_time = 0

    def __call__(self, user):
        now = time.time()

        if not self.used or now >= self.reset_time:
            self.used = True
            self.reset_time = now + self.cooldown
            return self.func(user)
        else:
            return f"@{user}, " + player_pick_name() + f" is player of the day. Try again later!"


def player_of_the_day(user):
    return f" The player of the day... " + player_pick() # ESPN SCRAPPING FUNCTION PICKING PALYERS/ a link to player would be a nice addition


def hello_command(user):
    return f"Hey @{user}! 👋"


def bot_command(user):
    return "I created this bot myself."


def joke_command(user):
    return random.choice([
        "Why did the streamer cross the road? To get better Wi-Fi!",
        "Bots can't cry... unless their API breaks.",
        "Streaming is 10% gameplay and 90% OBS troubleshooting."
    ])


def time_command(user):
    return f"The current time is {time.strftime('%H:%M:%S')}"


def viewers_command(user):
    if seen_chatters:
        return f"👥 Active chatters: {', '.join(list(seen_chatters)[:10])}"
    else:
        return "No one has chatted yet 😴"


def commands_help(user):
    return f"!hello,!bot,!joke,!time,!viewers"


def random_picture(user):
    return f"Here's an image: https://packaged-media.redd.it/842utlhhiv6e1/pb/m2-res_480p.mp4?m=DASHPlaylist.mpd&v=1" \
           f"&e=1753495200&s=2281efe871eb924a2e428810df0748ea4481771b"


def pc_command(user):
    return f'CPU: Intel I9 12900k '\
            f'GPU: RTX 5080 '\
            f'RAM: 32GB G.Skill DDR5-6000 '\
            f'Case: NZXT H9 ATX Tower '\
            f'CPU Fan: NZXT Kraken '\
            f'MB: MSI PRO Z690-A'


def lurk(user):
    return f'Thanks for the lurk {user}!'


def timeoutUser(user, duration=600):
    return f"timeout {user} {duration}"


def password(user):
    return f"your password " + generate_password() + f"shhh... Don't tell anyone. "


def website(user):
    return f"Check out my website: https://cameronhampton.com"


def add_chatter(user):
    seen_chatters.add(user)
    return f"Welcome to the chat, @{user}!"


def remove_chatter(user):
    seen_chatters.discard(user)
    return f"Goodbye, @{user}! We'll miss you."


def cat(user):
    return f"🐱"


def dog(user):
    return f"🐶"

def jamSeshScore(user):
    num = random.randint(1, 1000)
    choice = random.choice([1, 2])
    if num == 1000:
        # Log the user and timestamp
        with open("jam_sesh_legends.log", "a") as f:
            f.write(f"{datetime.datetime.now().isoformat()} - {user}\n")
        return f"{user}, Your Jam Sesh Score is {num}. What a legend!"
    elif choice == 1:
        return f"{user}'s Sesh Score is {num}. Poggers!"
    elif choice == 2:
        return f"{user}, Your Jam Sesh Score is {num}."


# Register all commands here
commands = {
    "!hello": hello_command,
    "!bot": bot_command,
    "!joke": joke_command,
    "!time": time_command,
    "!viewers": CooldownCommand(viewers_command, cooldown_seconds=60),
    "!commands": commands_help,
    "!image": CooldownCommand(random_picture, cooldown_seconds=1200),
    "!pc": pc_command,
    "!lurk": lurk,
    "!password": CooldownCommand(password, cooldown_seconds=300),
    "!POTD": GlobalOneTimeCommand(player_of_the_day, 12),
    "!website": website,
    "!add": add_chatter,
    "!remove": remove_chatter, # Optional: command to remove a user from seen_chatters
    "!cat": cat,
    "!dog": dog,
    "!jamseshscore": jamSeshScore,
    }
