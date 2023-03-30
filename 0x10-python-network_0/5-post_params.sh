#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sHX  "POST" $1 -d "email=test@gmail.com&subject=I will always be here for PLD"
