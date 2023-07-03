#!/bin/bash
# takes URL and displaysHTTP methods the server will accept
curl -sI "$1" | grep "Allow: " | cut -d' ' -f 2-
