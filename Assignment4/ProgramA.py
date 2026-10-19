# Program Name:         ProgramA.py
# Course:               IT3883/Section W01
# Student Name:         Brendan McCaffrey
# Assignment Number:    Lab4
# Due Date:             11/6/2026
# Purpose:              Prompts the user for a string, sends it to Program B
#                       over a socket, and then displays the response.
# Resources:            Module 4 Network Programming slides and Client.py

import socket

# Create a socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Connect to Program B
s.connect(("127.0.0.1", 45000))

# Prompt the user for a string
message = input("Type a string: ")

# Convert the message to bytes and send it
byte_array = message.encode('utf-8')
s.sendall(byte_array)

# Receive and display the response
response = s.recv(256).decode('utf-8')
print("Response from Program B:", response)

# Close the socket
s.close()