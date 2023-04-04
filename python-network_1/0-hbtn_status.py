#!/usr/bin/python3
"""fetching data from URL"""
import urllib.request

if __name__ == "__main__":
    y = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(y) as re:
        data = re.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
