# Smart Parking System

total_slots = int(input("Enter total parking slots: "))
available_slots = total_slots
vehicles = []

while True:
    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Parking Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if available_slots > 0:
            vehicle_no = input("Enter Vehicle Number: ")
            vehicles.append(vehicle_no)
            available_slots -= 1
            print("Vehicle parked successfully!")
        else:
            print("Parking Full!")

    elif choice == "2":
        vehicle_no = input("Enter Vehicle Number to Remove: ")

        if vehicle_no in vehicles:
            vehicles.remove(vehicle_no)
            available_slots += 1
            print("Vehicle removed successfully!")
        else:
            print("Vehicle not found!")

    elif choice == "3":
        print("\n----- Parking Status -----")
        print("Total Slots:", total_slots)
        print("Available Slots:", available_slots)
        print("Occupied Slots:", total_slots - available_slots)

        if len(vehicles) > 0:
            print("Parked Vehicles:")
            for v in vehicles:
                print("-", v)
        else:
            print("No vehicles parked.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")
