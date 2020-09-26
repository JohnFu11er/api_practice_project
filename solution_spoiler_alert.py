# Imports required Python modules
import requests
import json

# Defines the two api calls that we will do
get_inventory = requests.get('https://raw.githubusercontent.com/JohnFu11er/api_practice_project/master/Inventory.json')
get_devices = requests.get('https://raw.githubusercontent.com/JohnFu11er/api_practice_project/master/devices.json')

# Assigns the JSON formatted API data to the local dictionary variables
inventory = dict(get_inventory.json())
devices = dict(get_devices.json())

# Parses throught the two dictionaries and joins their content
for dev_name in inventory.keys():
    if dev_name in devices:
        inventory[dev_name].update({"hosts" : devices[dev_name]["hosts"]})
        inventory[dev_name].update({"vars" : devices[dev_name]["vars"]})

# Prints the result to the screen
print(json.dumps(inventory, indent=4, sort_keys=True))

# Writes the data to a file under the local directory that this program was run in
with open('./custom_inventory.json', mode='wt', encoding='utf-8') as _custom_inventory:
    _custom_inventory.write(json.dumps(inventory, indent=4, sort_keys=True))
