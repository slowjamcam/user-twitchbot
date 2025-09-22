import socket
from Twitch_Commands import commands, seen_chatters


# Replace these with your details
HOST = 'irc.chat.twitch.tv'
PORT = 6667
NICK = 'SJC_BOT_'
TOKEN = 'oauth:8d0vncz699zqynacbiywacw1xrzz0d'
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
                elif "man city sucks" in message.lower():
                    send_message(f"/timeout {username} 30")


    except KeyboardInterrupt:
        print("Bot shutting down...")
        break


    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    SJC_BOT.py.run()
