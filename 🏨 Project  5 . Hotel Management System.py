# Is project mein aap ek simple hotel system banayenge.
# Features / Concepts
# 1	Guest Name	variables
# 2	Room Booking	functions
# 3	Room List	list
# 4	Check Room	if-else
# 5	Check-in	list/operators
# 6	Check-out	remove()
# 7	Room Charges	operators
# 8	Food Order	list
# 9	Total Bill	sum() / operators
# 10	Discount	if-elif-else
# 11	Show Bill	function
# 12	Exit	while + break


# ------------------------------------------
# Hotel Data
# ------------------------------------------


rooms = ["101","102", "103", "104", "105"]
booked_rooms = []
room_check_in = []
food_orders = []


# ------------------------------------------
# Guest Information
# ------------------------------------------

def get_guest_info():
    guest_name = input("enter guest name: ")
    return guest_name

# ------------------------------------------
# room booking function
# ------------------------------------------
def book_room():
    room_number = input("enter room number to book:")
    if room_number in booked_rooms:
        print("room is already booked.")
    else:
        booked_rooms.append(room_number)
        print("room booked succesfully.")

# ------------------------------------------
# room checking function
# ------------------------------------------
def check_room():
    room_number = input("enter room number to check:")
    if room_number in booked_rooms:
        print("room is booked.")
    else:
        print("room is available.")

# ------------------------------------------
# room check_in function
# ------------------------------------------
def check_in():
    room_number = input("enter room number to check-in:")
    if room_number in booked_rooms:
        room_check_in.append(room_number)
        print("Check-in successful")
    else:
        print("room is not booked.")
# ------------------------------------------
# room check_out function
# ------------------------------------------
def check_out():
    room_number = input("enter room number to check_out:")
    if room_number in booked_rooms:
        booked_rooms.remove(room_number)
        if room_number in room_check_in:
            room_check_in.remove(room_number)
        print("guest checked out succesfully")

# ------------------------------------------
# room charges function
# ------------------------------------------
def room_charges():
    room_number = input("enter room number to calculate charges:")
    if room_number in booked_rooms:
        days = int(input("enter number of days stayed:"))
        charge = days * 1000 
        print(f"total room charges for {room_number}: {charge}")


# ------------------------------------------
# food order function
# ------------------------------------------

def food_order():
    food_item = input("enter food item to order:")
    food_orders.append(food_item)



    
# ------------------------------------------
# total bill function
# ------------------------------------------

def total_bill():
    room_number = input("enter room number to calculate total bill:")
    if room_number in booked_rooms:
        days = int(input("enter number of days stayed:"))
        room_charges = days * 1000
        food_charges = len(food_orders) * 500
        total = room_charges + food_charges
        print(f"total bill for {room_number}: {total}")



        
# ------------------------------------------
# discount function
# ------------------------------------------
def discount():
    room_number = input("enter room number to calculate discount:")
    if room_number in booked_rooms:
        days = int(input("enter number of days stayed:"))
        room_charges = days * 1000
        discount = room_charges * 0.1  
        print(f"discount for {room_number}: {discount}")


# ------------------------------------------
# show bill function
# ------------------------------------------  
def show_bill():
    room_number = input("enter room number show bill:")
    if room_number in booked_rooms:
        days = int(input("enter number of days stayed:"))
        room_charges = days * 1000
        food_charges = len(food_orders) * 500
        total = room_charges + food_charges
        discount = room_charges * 0.1
        final_bill = total - discount
        print(f"final bill for {room_number}: {final_bill}")
        
# ------------------------------------------
# exit function
# ------------------------------------------ 
while True:
        print("=== Hotel Management System ===")
        print("1. Get Guest Information")
        print("2. Book Room")
        print("3. Check Room Availability")
        print("4. Check In")
        print("5. Check Out")
        print("6. Calculate Room Charges")
        print("7. Order Food")
        print("8. Calculate Total Bill")
        print("9. Calculate Discount")
        print("10. Show Bill")
        print("11. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            get_guest_info()

        elif choice == "2":
         book_room()

        elif choice == "3":
         check_room()

        elif choice == "4":
         check_in()

        elif choice == "5":
         check_out()

        elif choice == "6":
         room_charges()

        elif choice == "7":
         food_order()

        elif choice == "8":
         total_bill()

        elif choice == "9":
         discount()

        elif choice == "10":
         show_bill()

        elif choice == "11":
         print("Thank you...")
         break

        else:
         print("Invalid choice")