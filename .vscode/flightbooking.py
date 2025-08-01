# from datetime import datetime,timedelta

# # today's date
# current_date=datetime.now()
# print("Today's Date",current_date)
# dept_date=datetime(day,month,year)
# dept_date=datetime(23,12,2025)
# valid_depature_date=datetime.now()+timedelta(days=2)
# print("Valid Departure Date: ",valid_depature_date)

# #depature date validation

# depature_date=input("Enter your depature date in dd/mm/yyyy:- ")
# arrival_date=input("Enter your arrival date in dd/mm/yyyy:-")
# print("Depature Date:",depature_date)
# print("Arrival Date:",arrival_date)
# if arrival_date<depature_date:
#     print("Invalid Arrival Date")
#     print("Please Enter a Valid Arrival Date")
#     exit()
# else:
#     print("Valid Arrival Date")
# if depature_date==valid_depature_date:
#     print("Your flight has been booked successfully")
# else:
#     print("Invalid Depature Date")
#     print("Please enter a valid depature date")

# # flight rescheduling
# flight_reschedule=input("Do you want to reschedule your flight? (yes/no):- ")
# if flight_reschedule=="yes":
#     new_depature_date=input("Enter your new depature date in dd/mm/yyyy:- ")
#     if new_depature_date!=valid_depature_date:
#         print("Flight Rescheduled Successfully")
#     else:
#         print("Invalid Depature Date Your Booking has been closed \nThank You!")
# elif flight_reschedule=="no":
#     print("Thank You For Booking Your Flight With Us!")
#     print("Invalid Input")



from datetime import datetime, timedelta, time

# Get current date and time
now = datetime.now()
print("✈️"*3)

print("Enter departure date and time (YYYY-MM-DD HH:MM)✈️: ")
departure_input = input()
departure = datetime.strptime(departure_input, "%Y-%m-%d %H:%M")
# get arrival and depature dates

print("Enter arrival date and time (YYYY-MM-DD HH:MM)✈️: ")
arrival_input = input()
arrival = datetime.strptime(arrival_input, "%Y-%m-%d %H:%M")

if (departure.date() - now.date()).days < 2:
    print("Invalid: Departure must be at least 2 days from today.")
elif arrival <= departure:
    print("Invalid: Arrival must be after departure.")
elif not (time(6, 0) <= departure.time() <= time(22, 0)):
    print("Invalid: Departure time must be between 6:00 AM and 11:00 PM.")
else:
    print("✅ Booking successful! ✈️ Happy Journey :)")

# flight rescheduling
    print("Do you want to reschedule your flight? (yes/no):")
    answer = input().lower()

    if answer == "yes":
        print("Enter new departure date and time (YYYY-MM-DD HH:MM): ")
        new_dep_input = input()
        new_departure = datetime.strptime(new_dep_input, "%Y-%m-%d %H:%M")

        # Rescheduling condition:
        if (new_departure.date() - now.date()).days > 7:
            print("❌ Reschedule failed: New departure must be within 7 days from today.")
        elif not (time(6, 0) <= new_departure.time() <= time(23, 0)):
            print("❌ Reschedule failed: Departure time must be between 6:00 AM and 11:00 PM.")
        elif new_departure <= now:
            print("❌ Reschedule failed: Date must be after today.")
        else:
            print("✅ Reschedule successful! New departure:", new_departure)
    else:
        print("No rescheduling selected.")
