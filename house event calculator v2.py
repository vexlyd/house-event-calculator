def event():
    """
    The function asks the user for the name of an event and the type of event, then prints a sentence
    with the information
    """
    event_name = input("What event was held? ")
    event_type = input("What type of event was held? ")

    print(f"The event held was {event_name} this event was a {event_type} type event.")

event()

print("\n")

while True:
    try:
        yellow_house = int(input("How many points did Yellow House get?  "))
        if yellow_house > 100:
            print("A house can not earn more than 100 points.")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue
    else:
        break

while True:
    try:
        blue_house = int(input("How many points did Blue House get?  "))
        if blue_house > 100:
            print("A house can not earn more than 100 points.")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue
    else:
        break

while True:
    try:
        red_house = int(input("How many points did Red House get?  "))
        if red_house > 100:
            print("A house can not earn more than 100 points.")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue
    else:
        break

while True:
    try:
        green_house = int(input("How many points did Green House get?  "))
        if green_house > 100:
            print("A house can not earn more than 100 points.")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue
    else:
        break

print("\n")

print(f"Yellow House earned {yellow_house} points")
print(f"Blue House earned {blue_house} points")
print(f"Red House earned {red_house} points")
print(f"Green House earned {green_house} points")



