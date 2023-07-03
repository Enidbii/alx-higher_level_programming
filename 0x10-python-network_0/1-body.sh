#!/bin/bash
# takes URL, sends a GET request to URL, and display only body of a 200 status code response
curl -s "$1" -X GET -L
