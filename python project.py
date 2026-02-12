MetroPass = 500 
stations = ["CMBT", "Vadapalani", "Thousand lights", "Velachery", "Guindy", "Central"] 

while True: 
    print("\n----- MetroPass -----") 
    print("1. Check Balance") 
    print("2. Recharge") 
    print("3. Book Ticket") 
    print("4. Exit") 

    Option = int(input("Enter your option: ")) 

    if Option == 1: 
        print("Your MetroBalance = Rs.", MetroPass) 

    elif Option == 2: 
        amount = float(input("Enter recharge amount: ")) 
        MetroPass = MetroPass + amount 
        print("MetroPass recharged successfully") 

    elif Option == 3: 
        print("Available Stations:", stations) 
        source = input("Enter source station: ") 
        destination = input("Enter destination station: ") 

        if source in stations and destination in stations: 
            distance = abs(stations.index(destination) - stations.index(source)) 
            fare_per_passenger = distance * 10 
            passengers = int(input("Enter number of passengers: ")) 
            total_fare = fare_per_passenger * passengers 

            if total_fare <= MetroPass: 
                MetroPass -= total_fare 
                print(f"Ticket booked from {source} to {destination} for {passengers} passenger(s).") 
                print(f"Fare = Rs.{total_fare}") 
                print("Please collect your QR") 
            else: 
                print("Insufficient balance") 
        else: 
            print("Invalid station entered") 

    elif Option == 4: 
        print("Travel Using MetroPass") 
        break 

    else: 
        print("Invalid Option") 

