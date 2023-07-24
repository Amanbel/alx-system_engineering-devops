#!/usr/bin/python3
""" serielize the fetch
data to json file """

if __name__ == "__main__":
    import json
    import requests

    userRes = requests.get("https://jsonplaceholder.\
typicode.com/users")
    todoRes = requests.get("https://jsonplaceholder.\
typicode.com/todos")

    dicts = {}
    for user in userRes.json():
        name = user["username"]
        userId = user["id"]
        value = []
        for obj in todoRes.json():
            task = obj["title"]
            status = obj["completed"]
            jsObj = {"username": name, "task": task, "completed": status}
            value.append(jsObj)
        dicts[userId] = value
    with open("todo_all_employees.json", 'w') as f:
        json.dump(dicts, f)
