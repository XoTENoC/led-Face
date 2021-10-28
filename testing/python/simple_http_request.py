
# simple script to send a http request to a webserver


import httplib2
import sys
import os
import json
import time

sys.path.append(os.path.join(os.path.dirname(__file__), "httplib2"))

http = httplib2.Http()


def main():

    # response, content = http.request(url, 'GET')
    while True:
        check = input("1 for on and 0 for off: ")
        checkInt = int(check)

        # if the user inputs 1 it will turn on
        if checkInt == 1:
            url = 'http://10.0.3.175/26/on'
            http.request(url, 'GET')

        # if the user inputs 0 it will turn off
        elif checkInt == 0:
            url = 'http://10.0.3.175/26/off'
            http.request(url, 'GET')

        elif checkInt == 3:
            flash()


if __name__ == "__main__":
    main()
