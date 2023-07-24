#!/usr/bin/python3
""" python script to fetch data from api """

if __name__ == "__main__":
    import requests
    from sys import argv

    i = 0
    res = requests.get("https://jsonplaceholder.\
typicode.com/todos?userId={}".format(argv[1]))
    userRes = requests.get("https://jsonplaceholder.\
typicode.com/users/{}".format(argv[1]))
    for obj in res.json():
        if (obj['completed'] is True):
            i += 1
    print("Employee {} is done with \
tasks({}/{}):".format(userRes.json()['name'], i, len(res.json())))

    for obj in res.json():
        if (obj['completed'] is True):
            print("\t {}".format(obj['title']))
