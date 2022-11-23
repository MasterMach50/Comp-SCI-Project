# 8. ILLUSTRATION OF BINARY FILE PROGRAMING-II
# A binary file named "flight.dat" which will contain certain records of
# flight (flightid,flightname and number of passengers).
# Write a menu driven program to do the
# following task:
#     1. Append a record
#     2. Delete a record
#     3. Read and display all.

import pickle

f = open("flight.dat", "a") # Ensure that the file exists
f.close()

flights = []
with open("flight.dat", "rb") as f:
    while True:
        try: # Using a try block to catch errors
            flight = pickle.load(f)
            flights.append(flight)
        except EOFError:
            break

def appendFlight():
    flightID = int(input("Enter flight ID: "))
    flightName = input("Enter flight name: ")
    nop = int(input("Enter number of passengers: "))


    with open("flight.dat", "ab") as f:
        pickle.dump([flightID, flightName, nop], f)

def deleteFlight():
    flightID = int(input("Enter flight ID: "))

    flights = []
    with open("flight.dat", "rb") as f:
        while True:
            try: # Using a try block to catch errors
                flight = pickle.load(f)
                flights.append(flight)
            except EOFError:
                break
    
    newflights = []
    for flight in flights:
        if flight[0] != flightID:
            newflights.append(flight)
    
    with open("flight.dat", "wb") as f:
        for flight in newflights:
            pickle.dump(flight, f)
    
    print("Removed flight with ID", flightID)
    

def showFlights():
    flights = []
    with open("flight.dat", "rb") as f:
        while True:
            try: # Using a try block to catch errors
                flight = pickle.load(f)
                flights.append(flight)
            except EOFError:
                break
    

    for flight in flights:
        print("--------------------")
        print("ID        :", flight[0])
        print("Name      :", flight[1])
        print("Passengers:", flight[2])
        print("--------------------")



while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Append a flight
    [2] Delete a flight
    [3] Show all flights
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        appendFlight()
    
    elif ch == "2":
        deleteFlight()

    elif ch == "3":
        showFlights()

    elif ch == "4":
        print("[ Exiting ]") # Break from the loop to exit
        break

    else:
        print("[ Invalid Choice ]") # In case user inputs a choice that was not defined
