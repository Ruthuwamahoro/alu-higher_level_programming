#!/bin/bash
#Takes ,sends a request to Url and displays the size of body
curl -s "$1" | wc -c
