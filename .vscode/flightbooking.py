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
