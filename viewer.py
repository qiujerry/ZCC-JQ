import requests 

response = requests.get('https://zccjq.zendesk.com/api/v2/requests.json', auth=('qiu.500@osu.edu/token', 'Pi6aJaMo7ZBzMy18333EJIrcFudpqM97gfH6BscO'))
print(response)