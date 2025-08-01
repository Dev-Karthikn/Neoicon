# # ticket=input("Do u wish to book a ticket:-")
# # seat=int(input("Enter the seat number you want to book(Available seats Are from 0-10):-"))
# # available_seats=[]
# # seats=10
# # if(ticket == "yes"):
# #     for i in range(0,10):
# #         available_seats.append(i)
# #     print(available_seats)
# #     print("The seat number",seat,"ticket is booked")
# # if(ticket=="no"):
# #     print("Thank you for visiting our website")

# # Simple Seat Booking System

# # Total number of available seats
# total_seats = 10
# booked_seats = []

# print("Welcome to the Seat Booking System.")
# print("There are 10 seats available (Seat numbers: 1 to 10).\n")

# while len(booked_seats) < total_seats:
#     try:
#         seat = int(input("Enter the seat number you want to book (1-10): "))
#         if seat < 1 or seat > 10:
#             print("Invalid seat number. Please enter a number between 1 and 10.")
#         elif seat in booked_seats:
#             print(f"Seat {seat} is already booked. Please choose another seat.")
#         else:
#             booked_seats.append(seat)
#             print(f"Seat {seat} successfully booked.")
#             print(f"Remaining seats: {total_seats - len(booked_seats)}\n")
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# print("\nAll seats are now booked. No more seats available.")


print("Welcome to the Seat Booking System.")
print("There are 10 seats available (Seat numbers: 1 to 10)")
seat_number=int(input("Which Seat do u Prefer?:- "))
booked_seats=[]
confirmation=input("Do u wish to book a ticket:-")
while(seat_number>10)&(seat_number<1):
    
    print("Invalid seat number. Please enter a number between 1 and 10.")


