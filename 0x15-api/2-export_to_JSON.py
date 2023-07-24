#!/usr/bin/python3
""" serielize the fetch
data to json file """

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    userRes = requests.get("https://jsonplaceholder.\
typicode.com/users/{}".format(argv[1]))
    todoRes = requests.get("https://jsonplaceholder.\
typicode.com/todos?userId={}".format(argv[1]))

    value = []
    name = userRes.json()["username"]
    for obj in todoRes.json():
        task = obj["title"]
        status = obj["completed"]
        jsObj = {"task": task, "completed": status, "username": name}
        value.append(jsObj)
    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump({argv[1]: value}, f)
