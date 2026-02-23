# cschumacher_Module_9_2_02222026
import json
import requests

response = requests.get('http://api.open-notify.org/astros.json') # Make single API request to OpenNotify 

def get_OpenNotify_status():
    print(f'OpenNotify API status: {response.status_code}')

def get_current_astronauts(): 
    if response.status_code == 200: # Test connection
        data = response.json()
        jprint(data) # Print formatted data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_blinded_condition():
    dnd_response = requests.get('https://www.dnd5eapi.co/api/conditions/blinded')
    if dnd_response.status_code == 200: # Test connection
        data = dnd_response.json()
        print("Connection established") 
        print(data) # Print raw data
        jprint(data) # Print formatted data
    else:
        print(f"Failed to retrieve data. Status code: {dnd_response.status_code}")
    

# Helper function to print JSON data in a readable format
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



def main():
    get_OpenNotify_status()
    get_current_astronauts()
    get_blinded_condition()

if __name__ == "__main__":
    main()

