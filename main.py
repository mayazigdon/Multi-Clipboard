import sys
import clipboard
import json
SAVED_DATA = "clipboard.json"


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":
        key = input("Enter a Key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)

    elif command == "load":
        key = input("Enter a Key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard, press ctrl+v")
        else:
            print("key does not exist")

    elif command == "list":
        print(data)

    elif command == "delete":
        key = input("Enter a key: ")
        if key in data:
            del data[key]
            save_items(SAVED_DATA, data)

    else:
        print("unknown command")
else:
    print("please pass exactly one command")


