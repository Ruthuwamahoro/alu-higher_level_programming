#!/usr/bin/python3
"""fetching data from URL"""
import urllib.request
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as re:
    data = re.read()
