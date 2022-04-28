# model class
class AirTicket:
    def __init__(self):
        '''self.flightName = ""     # to store flightName
        self.departure = ""     # to store departure
        self.arrival = ""     # to store arrival
        self.personName = ""     # to store personName
        self.seatType = ""     # to store seatType
        self.status = ""     # to store status'''

    def __init__(self, flightName, departure, arrival, personName, seatType, status):
        self.flightName = flightName  # to store flightName
        self.departure = departure  # to store departure
        self.arrival = arrival  # to store arrival
        self.personName = personName  # to store personName
        self.seatType = seatType  # to store seatType
        self.status = status  # to store status

    def bookFlight(self, l):
        self.viewSchedule(l)
        book = int(input("Press 1 to book available seat, 0 to cancel - "))
        if book == 1:
            name = input("Enter your name - ")
            for obj in l:
                if obj.personName == "":
                    obj.personName = name

        else:
            return

        self.viewSchedule(l)
        print("Congratulations ! Flight booked successfully.")

    def viewSchedule(self, lis):
        print()
        print("Flight Name \t\t Departure \t\t Arrival \t\t Person name \t\t Seat Type \t\t Status")
        for obj in lis:
            print(
                obj.flightName + "\t\t\t\t" + obj.departure + "\t\t\t" + obj.arrival + "\t\t\t" + obj.personName + "\t\t\t" +
                obj.seatType + "\t\t\t" + obj.status)


li = [AirTicket("Vistara", "0200", "0700", "Naruto Uzumaki", "business", "booked"),
      AirTicket("Indigo", "1400", "2200", "Kakashi Hatake", "economy", "booked"),
      AirTicket("Air Asia", "0200", "0700", "", "business", "available")]  # schedule

a = AirTicket("", "", "", "", "", "")

print("Hi, what would you like to do?")
while True:
    print("\n--Menu--")
    choice = int(input("1. Book Flight\n2. View Schedule\n3. Checkout\nEnter choice - "))

    if choice == 1:
        a.bookFlight(li)
    elif choice == 2:
        a.viewSchedule(li)
    else:
        break

'''

OUTPUT

/usr/bin/python3 /home/tecomp/Desktop/31282_Aditya/assign6/airlinebooking.py
Hi, what would you like to do?

--Menu--
1. Book Flight
2. View Schedule
3. Checkout
Enter choice - 1

Flight Name 		 Departure 		 Arrival 		 Person name 		 Seat Type 		 Status
Vistara				0200			0700			Naruto Uzumaki			business			booked
Indigo				1400			2200			Kakashi Hatake			economy			booked
Air Asia				0200			0700						business			available
Press 1 to book available seat, 0 to cancel - 0

--Menu--
1. Book Flight
2. View Schedule
3. Checkout
Enter choice - 1

Flight Name 		 Departure 		 Arrival 		 Person name 		 Seat Type 		 Status
Vistara				0200			0700			Naruto Uzumaki			business			booked
Indigo				1400			2200			Kakashi Hatake			economy			booked
Air Asia				0200			0700						business			available
Press 1 to book available seat, 0 to cancel - 1
Enter your name - Shikamaru Nara

Flight Name 		 Departure 		 Arrival 		 Person name 		 Seat Type 		 Status
Vistara				0200			0700			Naruto Uzumaki			business			booked
Indigo				1400			2200			Kakashi Hatake			economy			booked
Air Asia				0200			0700			Shikamaru Nara			business			available
Congratulations ! Flight booked successfully.

--Menu--
1. Book Flight
2. View Schedule
3. Checkout
Enter choice - 2

Flight Name 		 Departure 		 Arrival 		 Person name 		 Seat Type 		 Status
Vistara				0200			0700			Naruto Uzumaki			business			booked
Indigo				1400			2200			Kakashi Hatake			economy			booked
Air Asia				0200			0700			Shikamaru Nara			business			available

--Menu--
1. Book Flight
2. View Schedule
3. Checkout
Enter choice - 3

Process finished with exit code 0


'''
