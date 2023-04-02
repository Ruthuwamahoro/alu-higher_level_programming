#!/bin/bash
#sends Get request and displays the body of response
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
