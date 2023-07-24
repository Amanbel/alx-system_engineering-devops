#!/usr/bin/python3
""" export fetch to csv """

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    userRes = requests.get("https://jsonplaceholder.\
typicode.com/users/{}".format(argv[1]))
    todoRes = requests.get("https://jsonplaceholder.\
typicode.com/todos?userId={}".format(argv[1]))

    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        thewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        name = userRes.json()["username"]
        for obj in todoRes.json():
            thewriter.writerow([argv[1], name, obj["completed"], obj["title"]])
