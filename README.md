# Python Script for Hotel Room Price Analysis

This repository contains a Python script that performs analysis on hotel room booking data. The task involves processing a JSON file containing room pricing information to extract various insights about the rooms and their prices.

## Tasks Implemented in the Script

The script performs the following tasks:

1. **Download and Load JSON File**  
   The script loads the provided JSON file into the local environment (e.g., PyCharm or another IDE).

2. **Find the Cheapest Room Price**  
   The script finds and returns the lowest price among all available rooms, without using the `min()` function.

3. **Find Room Type and Number of Guests for Cheapest Room**  
   The script identifies the room type(s) and the number of guests for the room with the cheapest price.

4. **Calculate Total Price for All Rooms**  
   The script calculates the total price for all rooms, including the net price and taxes, and displays it alongside the room type.

5. **Output to File**  
   The script saves the results of the analysis, including the cheapest room, its price, room types, and the list of all rooms with their total prices, into a file named `solution.txt`.

6. **Code Documentation**  
   The code is well-documented with comments explaining the logic and flow of the script.

## Example Output (solution.txt)

The script generates an output in the `solution.txt` file, formatted as follows:

Cheapest room: King Studio Suite - Non Smoking
Price: 90.0
Room Name: King Studio Suite
Room Types: ['Non Smoking']
Number of Guests: 4
All rooms:
[
    {
        "room_name": "King Studio Suite",
        "room_types": [
            "Hearing Accessible",
            "Non-Smoking"
        ],
        "total_room_price": 131.76
    },
    {
        "room_name": "King Studio Suite",
        "room_types": [
            "Non Smoking"
        ],
        "total_room_price": 108.71
    },
    {
        "room_name": "King Room",
        "room_types": [
            "Mobility",
            "Hearing Accessible",
            "Non-Smoking"
        ],
        "total_room_price": 133.76
    },
    {
        "room_name": "Queen Suite with Two Queen Beds",
        "room_types": [
            "Non-Smoking"
        ],
        "total_room_price": 130.76
    }
]

