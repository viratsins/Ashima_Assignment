class Flight:
    def _init_(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def _init_(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_by_flight_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None
    
    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result
    
    def search_by_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.destination == destination:
                result.append(flight)
        return result

# Creating flight objects and adding them to the flight table
flight_table = FlightTable()
flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

# User input
user_input = input("Enter flight ID, source city, or destination city: ")

# Searching and printing flight details based on user input
flight = flight_table.search_by_flight_id(user_input)
if flight:
    print(f"Flight ID: {flight.flight_id}")
    print(f"From: {flight.source}")
    print(f"To: {flight.destination}")
    print(f"Price: {flight.price}")
else:
    flights_from = flight_table.search_by_source(user_input)
    if flights_from:
        print("Flights from", user_input)
        for flight in flights_from:
            print(f"Flight ID: {flight.flight_id}, To: {flight.destination}, Price: {flight.price}")
    else:
        flights_to = flight_table.search_by_destination(user_input)
        if flights_to:
            print("Flights to", user_input)
            for flight in flights_to:
                print(f"Flight ID: {flight.flight_id}, From: {flight.source}, Price: {flight.price}")
        else:
            print("No matching flights found.")