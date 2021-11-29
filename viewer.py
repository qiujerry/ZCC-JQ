import requests 
import os
import json

#python CLI for zendesk coding challenge
#python CLI displays tickets for user

os.system('cls||clear')

print("Welcome to the Zendesk ticket viewer\n")
#response = requests.get('https://zccjq.zendesk.com/api/v2/tickets.json?per_page=25&page_number=2', auth=('qiu.500@osu.edu/token', 'Pi6aJaMo7ZBzMy18333EJIrcFudpqM97gfH6BscO'))
response = requests.get('https://zccjq.zendesk.com/api/v2/tickets.json', auth=('qiu.500@osu.edu/token', 'Pi6aJaMo7ZBzMy18333EJIrcFudpqM97gfH6BscO'))

if(response.status_code == 200):
    print("User authenticated successfully!\n")
elif (response.status_code == 401):
    print("User authentication failed. Quitting")
    exit

#create dictionary from returned json
json_data = json.loads(response.text)
print(len(json_data))
data = response.json().get("tickets")
print("data test \n")
print(len(data))

for key in json_data["tickets"]:
    print(key)
    #print(json_data[key])
    print("test\n")

# for ticket in data:
#     print(ticket)
#     print("test\n")
