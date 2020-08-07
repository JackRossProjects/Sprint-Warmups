'''
Prompt: You've booked a really cheap one-way flight. Unfortunately, that means you
have tons of layovers before you reach your destination. The morning of, you woke
up late and had to scramble to the airport to catch your first flight. However, in
your rush, you accidentally scrambled all your flight tickets. You don't know the
route of your entire trip now!

Write a function reconstruct_trip to reconstruct your trip
from your mass of flight tickets. Each ticket is represented as a
class with the following form:
'''

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

'''
Where the source string represents the starting airport and the destination
string represents the next airport along our trip. The ticket for your first
flight has a destination with a source of NONE, and the ticket for your final
flight has a source with a destination of NONE.
'''

def reconstruct_trip(tickets, length):
    # Initialize hash table and final route
    cache = {}
    route = []
    for ticket in tickets:
        # If the starting airport isnt in the cache
        if ticket.source not in cache:
            # that spot in the cache will become that tickets destination
            cache[ticket.source] = ticket.destination
    # Set current value to none
    cur = "NONE"
    # While this loop is true
    while True:
        # Check each ticket in the hash table
        for ticket in cache:
            # If the ticket is equal to the current value
            if ticket == cur:
                # Append that ticket to the sorted route
                route.append(cache[ticket])
                # and set current to the ticket in the hash table
                cur = cache[ticket]
                break
        # If all the tickets have been sorted into the final array
        if cache[ticket] == "NONE":
            # Exit the loop
            break
    # Return the sorted route
    return route
