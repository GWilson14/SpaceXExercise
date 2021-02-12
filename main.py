#SpaceX exercise
#By Greg Wilson (12/02/2021)

import json
import requests


def main():

    launches = requests.get('https://api.spacexdata.com/v4/launches/latest')
    launchData = json.loads(launches.text)

    shipList = launchData["ships"]

    print('Here are details of the latest SpaceX Launch: \n')

    print('Name: ' + launchData["name"])
    print('Date: ' + launchData["date_local"][:10])
    print('Details: ' + launchData["details"] + '\n')

    print('Here are details of the ships assigned to this launch: \n')

    for i in shipList:
        ships = requests.get('https://api.spacexdata.com/v4/ships/' + i)
        shipData = json.loads(ships.text)
        print('Name: ' + shipData["name"])
        print('Type: ' + shipData["type"])
        print('Home Port: ' + shipData["home_port"] + '\n')

main()