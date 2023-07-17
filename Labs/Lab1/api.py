import requests as req


def getOneUser(id):
    url = "https://jsonplaceholder.typicode.com/users/"
    response = req.get(url)
    print(response.json()[id]["name"])
    return response.json()[id]
