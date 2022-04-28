from datetime import *
class Event:
    def __init__(self,startTime,endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.venue = []

    def addVenue(self,venue):
        self.venue.append(venue)

class Venue:
    def __init__(self,name):
        self.name = name
        self.address = []

    def addAddress(self,address):
        self.address.append(address)

class Address:
    def __init__(self,street,city,state,country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country

event = Event(datetime(2022,4,1,18,30),datetime(2022,4,1,23,45))
venue = Venue('Music Event')
address = Address('MG Road','Mumbai','Maharashtra','India')
venue.addAddress(address)
event.addVenue(venue)

for i in event.venue:
    print(i.name,"\nDate:",event.startTime.date(),'\nStarts:',event.startTime.time(),'\nEnds:',event.endTime.time())
    for a in i.address:
        print("Address:{},{},{},{}".format(a.street,a.city,a.state,a.country))


