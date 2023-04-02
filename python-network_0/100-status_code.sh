#!/bin/bash
#bash that makes a request 
curl -s -o /dev/null -w "%{http_code}" "$1"
