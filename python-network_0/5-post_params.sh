#!/bin/bash
#sends Request POST to the passed URL and displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
