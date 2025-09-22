import random
import time
from string import ascii_lowercase
from string import ascii_uppercase


class Password:
    def __init__(self, password):
        self.password = password

    def generate_password(self):
        # User inputs the length of the password needed
        length = int(input("Enter Password Length: "))
        # User enters what username or website etc. the password is being used for
        username = str(input("Enter Username: (Website, Username, One-time, etc.) "))
        # A single number between 1 - 10 as a string
        number_1 = str(random.uniform(0, 10).__round__())
        # A single number between 1 - 100 as a string
        number_2 = str(random.uniform(0, 10000).__round__())
        # A string of 20 lowercase letters
        lowercase_Letters = "".join([random.choice(ascii_lowercase) for s in range(20)])
        # A string of 20 uppercase letters
        uppercase_Letters = "".join([random.choice(ascii_uppercase) for d in range(20)])
        # Adds Special characters to the password
        special_characters = random.choices('!@#$%^&*()_+}{][?<>', k=random.randrange(10))
        # Choices of characters
        characters_Choices = list(
            str(lowercase_Letters) + str(uppercase_Letters) + number_1 + number_2 + "".join(special_characters))
        # Shuffles the characters chosen
        random.shuffle(characters_Choices)
        # Creates the password list
        password = []
        # Choices characters at random and puts into the password variable list
        for i in range(length):
            password.append(random.choice(characters_Choices))
        # Shuffles the password variable list
        random.shuffle(password)
        # Makes the password list into a string
        password_string = "".join(password)
        Password.password = password_string
        return password_string


"""def main():
    generate = generate_password()
    return generate"""

"""def characters_choices():
# Choices of characters
    characters = Password.character_Set()
    set = list(characters.lowercase_Letters + characters.uppercase_Letters + characters.number_1 + characters.number_2 + "".join(characters.special_characters))
    return set"""

# Generates a password with the length of 12, 10 random lower case, upper case, numbers, and special chars, with the addition of and 2 random numbers.
# All the Chars are randomaly placed to form the password
def generate_password():
    number_1 = str(random.uniform(0, 10).__round__())
    # A single number between 1 - 100 as a string
    number_2 = str(random.uniform(0, 10000).__round__())
    # A string of 20 lowercase letters
    lowercase_Letters = "".join([random.choice(ascii_lowercase) for s in range(20)])
    # A string of 20 uppercase letters
    uppercase_Letters = "".join([random.choice(ascii_uppercase) for d in range(20)])
    # Adds Special characters to the password
    special_characters = random.choices('!$%&?', k=random.randrange(10))
    # Choices of characters
    characters_Choices = list(
        str(lowercase_Letters) + str(uppercase_Letters) + number_1 + number_2) #"".join(special_characters))
    # Shuffles the characters chosen
    random.shuffle(characters_Choices)
    # Creates the password list
    password = []
    # Choices characters at random and puts into the password variable list
    for i in range(13):
        password.append(random.choice(characters_Choices))
    for n in range(2):
        password.append(random.choice(number_1))
    # Shuffles the password variable list
    random.shuffle(password)
    password[5]="-"
    password[11]="-"
    # Makes the password list into a string
    password_string = "".join(password)
    return password_string


def check():
    # User enters what username or website etc. the password is being used for
    username = str(input("Enter Username: (Website, Username, One-time, etc.) "))
    # check if the username has already been used
    check = open("New Microsoft Word Document.word", "r")
    for x in check:
        list = x.split()
        if str(list[2].lower()) == username.lower():
            print(x)
            username = str(input("Please be more specific: (This username has already been used.) "))
            check_again = True
            while check_again:
                check = open("New Microsoft Word Document.word", "r")
                check_again = False
                for v in check:
                    line = v.split()
                    if (str(line[2].lower()) == username.lower()):
                        print(v)
                        check_again = True
                        username = str(input("Please be more specific: (This username has already been used.) "))
                        return username


def skip():
    pass

# Adds to dictionary


'''
# Prints each specific process happening (for development purposes)
print(special_characters)
print(number_1)
print(number_2)
print(lowercase_Letters)
print(uppercase_Letters)
print(characters_Choices)
'''

if __name__ == '__main__':
    main()
