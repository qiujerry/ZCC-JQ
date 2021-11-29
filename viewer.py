import requests 
import os
import json
import math

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
#print(len(json_data))
data = response.json().get("tickets")
#print("data test \n")
#print(len(data))

#used to track page number
page = 1
max_pages = 0

if(len(data)%25 == 0):
    max_pages = len(data)/25
else:
    max_pages = math.floor(len(data)/25) + 1

#message to user about number of tickets
print("There are %d tickets pulled and %d pages\n"%(len(data), max_pages))

#start loop to process user input
ans = "start"

while(ans != "quit"):
    #prompt user for input
    print("\n   Select view options:\n")
    print("         Type: {page #} to view ticktes of specified page\n")
    print("         Type: {ticket #} to view specific ticket\n")
    print("         Type 'quit' to quit\n")
    ans = raw_input("Selection: \n")
    holder = ans.strip().split(" ")

    if(holder[0].lower() == "page"):
        if(int(holder[1])<=max_pages and int(holder[1])>0):
            #display page
            page = int(holder[1])
            for x in range((page-1)*25, ((page-1)*25)+24):
                print(data[x])
            print("Page %d of %d\n"%(page, max_pages))
        else:
            print("Please enter valid page number\n")
            continue
    elif(holder[0].lower() =="ticket"):
        if(int(holder[1])<=len(data) and int(holder[1])>0):
            #display ticket
            print(data[int(holder[1])])
            print("Ticket %s of %d\n"%(holder[1], len(data)))
        else:
            print("Please enter valid ticket number\n")
            continue





# for key in json_data["tickets"]:
#     print(key)
#     #print(json_data[key])
#     print("test\n")

# for ticket in data:
#     print(ticket)
#     print("test\n")
