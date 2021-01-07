import requests

parameters = {
    "amount": 25,
    "type": "boolean",
    "category": 18
}


response = requests.get(url="https://opentdb.com/api.php", params=parameters)
data_qu = response.json()
print(data_qu)
question_data = data_qu['results']



