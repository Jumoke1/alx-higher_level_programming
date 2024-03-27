#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
<<<<<<< HEAD
curl -sI "$1" | grep "Content Length:" | cut -d ' ' -f 2
=======
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
>>>>>>> 820e9c06327ab7ff59fefdd81df5e7f64426298b
