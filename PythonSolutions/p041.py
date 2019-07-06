#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Unordered Flights
#   Daily Problem #: 41
#   Author: John Deisher
#   Date Started: 7/5/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. 
If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', 
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. 
However, the first one is lexicographically smaller.
"""

def find_next_connection(flights, curr_city):
    if len(flights) == 0:
        return [curr_city]

    for i,flight in enumerate(flights):
        if flight[0] == curr_city:

            flight_path = find_next_connection(flights[:i]+flights[i+1:], flight[1])
            if flight_path == False:
                break
            else:
                flight_path.insert(0,flight[0])
                return flight_path

    return False

def main():
    testFlights = list()
    startLoc = list()

    testFlights.append([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')])
    testFlights.append([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')])
    startLoc.append('YUL')
    startLoc.append('A')

    for i, start_city in enumerate(startLoc):
        flight_iten = find_next_connection(testFlights[i], start_city)
        print("FLIGHTS: {}, START: {}".format(testFlights[i],start_city))

        if flight_iten == False:
            print("NO PATH FOUND")
        else:
            print("ITEN: {}".format(flight_iten))
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT:

FLIGHTS: [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], START: YUL
ITEN: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
FLIGHTS: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], START: A
ITEN: ['A', 'B', 'C', 'A', 'C']
[Finished in 0.1s]
"""