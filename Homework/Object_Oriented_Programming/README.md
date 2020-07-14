# Buses
The class Passenger is given, which describes an unfortunate person whose bicycle was stolen and who has to ride a Ljubljana bus. The passenger contains information on the serial number of the station at which he will enter (if there is any space on the bus) and exit (via corpses, if necessary).
```
class Passenger:
    def __init __ (self, entry, exit):
        self.input = entry
        self.exit = exit
```
Don't modify the Passenger class.

## Mandatory task
Program the Bus class.

- The constructor accepts one argument, namely the maximum number of passengers.
- The capacity() method returns the maximum number of passengers (i.e. what we gave to the constructor).
- The occupancy() method returns the number of passengers who managed to squeeze onto the bus.
- The bus_number() method returns 18.
- The entry(passengers) method accepts a list of passengers that contains a Passenger type object. The bus is loaded with as many passengers from the beginning of the list as there are still on it. As a result, it returns a list of passengers who remained at the station.
- The exit(station_number) method removes passengers who leave the bus at the station with the given number.
- The method station(station_number, passengers) receives the station number and the passengers waiting at it. It removes passengers going out of the bus and adds passengers who manage to get inside. (In doing so, it is understood to call the previous two methods.) As a result, it returns a list of passengers who failed to squeeze onto the bus.
## Additional task
Program a function simulation(passengers, buses, stations) that gets a list of passengers waiting at different stations (each passenger is waiting where he intends to enter), a list of buses and a list of station numbers. The buses run in the order given in the list. Passengers enter in the order given in the lists; imagine that, as in some other countries, they are waiting in line.

The function should perform a simulation of the rides and return the list of passengers who remained at the stations.

### Disclaimer
The task is not the result of personal experience or dissatisfaction. They didn’t steal my bikes, so I don’t have to be transported with LPP’s motorized billboards.
