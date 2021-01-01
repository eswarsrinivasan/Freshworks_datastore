import os
import json
import sys
import datetime as dt
from datetime import datetime

user_input = {}
filename = "data.json"


# Creating Directory
def create_dir(choice):
    choice = input("Do want to specify the directory? ('yes' or 'no')")
    if choice == 'no':  # Creating a default directory
        os.makedirs('data')
        with open('data/data.json', 'wb') as f:
            f.seek(1024 * 1024 * 1024)  # One GB

    else:  # Creating a  directory as clinet wishes
        user_dir = input("Enter the folder")
        os.mkdir(user_dir)
        os.chdir(user_dir)
        with open('data.json', 'wb') as f:
            f.seek(1024 * 1024 * 1024)  # One GB


# Creating a Key-Value Pair
def create(key, value):
    try:  # File exist
        now = datetime.now()  # creating a Time to Live Property
        value = value + '|' + str(now)  # Appending it to the value to check whether it exist between the timeline
        with open('a.json', 'wb') as f:
            user_input = json.load(f)
        if key in user_input.keys():
            print("key already exist")
        else:
            user_input[key] = value
            user_input.update[key]
            with open('data.json', 'wb') as f:
                json.dump(user_input, f)

    except:  # Empty file
        now = datetime.now()
        value = value + '|' + str(now)
        user_input[key] = value
        user_input.update[key]
        with open('data.json', 'wb') as f:
            json.dump(user_input, f)


# Reading the value by getting Key from the user
def read():
    if os.path.isfile(filename):
        with open('data.json', 'wb') as f:
            user_input = json.load(f)
        key = input("enter the key")
        now = datetime.now()
        time = user_input[key]("|")[1]
        datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
        # Checking whether the Key exist between the time limit
        diff = dt.datetime.strptime(str(time), datetimeFormat) \
               - dt.datetime.strptime(str(now), datetimeFormat)
        if key in user_input.keys():
            if diff.days > 1:  # if key has been created within a day, then the key exist.
                print(user_input[key])
            else:
                print("key has been expired")
        else:
            print("Key isn't available")
    else:
        return "File doesn't exist in this Directory"



def remove():
    if os.path.isfile(filename):
        with open('data.json', 'wb') as f:
            user_input = json.load(f)
        key = input("enter the key")
        now = datetime.now()
        time = user_input[key]("|")[1]
        datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
        diff = dt.datetime.strptime(str(time), datetimeFormat) \
               - dt.datetime.strptime(str(now), datetimeFormat)
        if key in user_input.keys():
            if diff.days > 1:
                del user_input[key]
            else:
                print("key has been expired")
        else:
            print("Key isn't available")
    else:
        return "File doesn't exist in this Directory"
        
