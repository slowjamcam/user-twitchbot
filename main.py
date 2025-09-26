# from twitchio.ext import commands
# from twitchio.client import Client
# import os

# bot = commands.Bot(
#     client_secret='kgc7tj09p072zp15oycoidu6w9qbd3',
#     client_id='rfeu37kn23wpu96thm6o7w8nh2yf1g',
#     bot_id='Slowjam_bot',
#     owner_id='slowjamcam',
#     prefix='!',

# )

# client = Client(
#     client_id='rfeu37kn23wpu96thm6o7w8nh2yf1g',
#     client_secret='kgc7tj09p072zp15oycoidu6w9qbd3'
# )


# @bot.command(name='hello')
# async def hello_command(ctx):
#     await ctx.send("o" + "/" + " HELLO")


# if __name__ == '__main__':
#     bot.run()


# from twitchio.ext import commands
# from twitchio.client import Client
# import os


# bot = commands.Bot(
#     irc_token="kf90givw4gaje9l4zyalagsme2bxbj",
#     client_id="gp762nuuoqcoxypju8c569th9wz7q5",
#     nick='incompetent_robot',
#     bot_id="slowjam_bot",
#     client_secret="fx7slgfl7lgtt78xdy15857nwcucew",
#     prefix='!',
#     initial_channels=['incompetent_ian'],
# )


# client = Client(
#     client_id="rfeu37kn23wpu96thm6o7w8nh2yf1g",
#     client_secret="fx7slgfl7lgtt78xdy15857nwcucew",
# )


# @bot.event
# async def event_message(ctx):
#     print(ctx.author)
#     print(ctx.content)
#     await bot.handle_commands(ctx)


# @bot.command(name='test')
# async def test_command(ctx):
#     await ctx.send("this is a test response")


# @bot.command(name='who')
# async def get_chatters(ctx):
#     chatters = await client.get_chatters('incompetent_ian')
#     all_chatters = ' '.join(chatters.all)
#     await ctx.send(f"In chat: {all_chatters}")


# if __name__ == '__main__':
#     bot.run()

import socket
import time
from Twitch_Commands import commands, seen_chatters, timeoutUser

# Replace these with your details
HOST = 'irc.chat.twitch.tv'
PORT = 6667
NICK = 'SlowJamCam'
TOKEN = 'oauth:ng3hb5vv7otaqyv3sl627l7pwml1n5'
CHANNEL = '#slowjamcam'  # Include the '#' prefix

# Connect to Twitch IRC
sock = socket.socket()
sock.connect((HOST, PORT))
sock.send(f"PASS {TOKEN}\r\n".encode('utf-8'))
sock.send(f"NICK {NICK}\r\n".encode('utf-8'))
sock.send(f"JOIN {CHANNEL}\r\n".encode('utf-8'))

print(f"Joined {CHANNEL} as {NICK}")


def send_message(message):
    """Sends a message to the Twitch chat"""
    message_temp = f"PRIVMSG {CHANNEL} :{message}\r\n"
    sock.send(message_temp.encode('utf-8'))


# Main loop
while True:
    try:
        resp = sock.recv(2048).decode('utf-8')
        print("RAW:", resp)  # 👈 This prints the full incoming message

        if resp.startswith('PING'):
            sock.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
            send_message(f"Check out my website: https://cameronhampton.com")  # 👈 Respond to PINGs to stay connected

        elif "PRIVMSG" in resp:
            username = resp.split('!', 1)[0][1:]
            message = resp.split('PRIVMSG', 1)[1].split(':', 1)[1].strip()

            seen_chatters.add(username)  # 👈 Add speaker to known chatters

            print(f"{username}: {message}")

            print(f"Received command: '{message}' from {username}")

            # 🎯 Handle commands (start with !)
            if message.startswith("!"):
                command = message.split()[0]
                if command in commands:
                    response = commands[command](username)
                    send_message(response)

            # 💬 Handle casual chat (not commands)
            else:
                # You can add reactions to normal messages here
                if "hello" in message.lower():
                    send_message(f"Hi @{username}, how are you?")
                elif "good bot" in message.lower():
                    send_message("😊 Thanks!")
                elif "bad bot" in message.lower():
                    send_message("😢 I'm trying my best...")
                elif "you suck" in message.lower():
                    send_message(f"suck on this") and send_message(timeoutUser({username}, 600))
                elif "man city sucks" in message.lower():
                    send_message(f"/timeout {username} 30")
                elif "pog" in message.lower():
                    send_message("PogChamp!")
                elif "poggers" in message.lower(): 
                    send_message("PogChamp!")
                elif "bruh" in message.lower():
                    send_message("Just bruh.")
                elif "pogchamp" in message.lower():
                    send_message("PogChamp!")
                elif "lmao" in message.lower():
                    send_message("LMAO")
                elif "lol" in message.lower():
                    send_message("LOL")



    except KeyboardInterrupt:
        print("Bot shutting down...")
        break


    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
