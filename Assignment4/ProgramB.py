# Program Name:         ProgramB.py
# Course:               IT3883/Section W01
# Student Name:         Brendan McCaffrey
# Assignment Number:    Lab4
# Due Date:             11/6/2026
# Purpose:              Listens for a message from Program A, converts the
#                       received string to uppercase, and sends it back.
# Resources:            Module 4 Network Programming slides and Server.py

import socket

# Create a socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Bind the socket to an IP address and port
s.bind(("127.0.0.1", 45000))

# Listen for incoming connections
s.listen()
print("Program B is waiting for a connection...")

# Accept a connection from Program A
conn, addr = s.accept()

# Receive and decode the message
data = conn.recv(256)
message = data.decode('utf-8')

print("Received message:", message)

# Convert the message to uppercase
message = message.upper()

# Send the uppercase message back to Program A
conn.sendall(message.encode('utf-8'))

# Close the connection and socket
conn.close()
s.close()
