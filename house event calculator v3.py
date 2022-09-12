import tkinter
from tkinter import *
from tkinter import messagebox

# Creating the window and setting the title and size.
tk = tkinter
main = Tk()
main.title("House Event Calculator")
main.geometry("500x300")

# List to hold all events
total_house_events = []

# List to be used in Option Menu
event_names_list = ["Lampada Games", "House Trivia"]

# Creating the frames for the GUI.
input_frame = LabelFrame(main)
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W)
details_frame = LabelFrame(main, width="100")
details_frame.grid(row=1, column=0, sticky=S)
leaderboard_frame = LabelFrame(main)
leaderboard_frame.grid(row=0, column=1, padx=10, pady=10, sticky=N)


# Creating the labels for the GUI.
tk.Label(input_frame, text="Is it a sport").grid(column=0, row=0, sticky=W)
tk.Label(input_frame, text="Name of Event").grid(column=0, row=1, sticky=W)
tk.Label(input_frame, text="Kowhai").grid(column=0, row=2, sticky=W)
tk.Label(input_frame, text="Pohutukawa").grid(column=0, row=3, sticky=W)
tk.Label(input_frame, text="Kauri").grid(column=0, row=4, sticky=W)
tk.Label(input_frame, text="Rimu").grid(column=0, row=5, sticky=W)


# Creating an entry box for the user to input the name of the event.
event_name_input = tk.Entry(input_frame)

# Creating a radio button to allow the user to input if the event is a sport or nor
is_sport = tk.StringVar()
is_sport.set("Yes")
Radiobutton(input_frame, text="Yes", variable=is_sport, value="Yes").grid(column=1, row=0)
Radiobutton(input_frame, text="No", variable=is_sport, value="No").grid(column=2, row=0)


# Creating entry boxes for the user to input the points for each house.
yellow_points = Entry(input_frame)
red_points = Entry(input_frame)
blue_points = Entry(input_frame)
green_points = Entry(input_frame)

# Placing the widgets in the grid.
event_name_input.grid(column=1, row=1, columnspan=2, padx=2)
yellow_points.grid(column=1, row=2, columnspan=2)
red_points.grid(column=1, row=3, columnspan=2)
blue_points.grid(column=1, row=4, columnspan=2)
green_points.grid(column=1, row=5, columnspan=2)


# Creating labels for the leaderboard and positioning them.
Label(leaderboard_frame, text="LEADERBOARD").grid(column=0, row=0, columnspan=2)
Label(leaderboard_frame, text="Kowhai").grid(column=0, row=1, sticky=W, pady=5)
Label(leaderboard_frame, text="Pohutukawa").grid(column=0, row=2, sticky=W, pady=5)
Label(leaderboard_frame, text="Kauri").grid(column=0, row=3, sticky=W, pady=5)
Label(leaderboard_frame, text="Rimu").grid(column=0, row=4, sticky=W, pady=5)


# It creates an object called Event, which has a name, event type, points for each house, and a winner
class Event:
    def __init__(self, name, event_type, yellow_p, red_p, blue_p, green_p, who_won):
        self.name = name
        self.event_type = event_type
        self.yellow_p = yellow_p
        self.red_p = red_p
        self.blue_p = blue_p
        self.green_p = green_p
        self.who_won = who_won
# Prints out the data added by the user 
    def details(self):
        return(["Event Name " + self.name, "Is it a sport " + self.event_type, "Kowhai " + str(self.yellow_p) + " Points", "Pohutukawa " + str(self.red_p) + " Points", "Kauri " + str(self.blue_p) + " Points", "Rimu " + str(self.green_p) + " Points", "Winner " + self.who_won])


# Adding pre made events
total_house_events.append(Event("Lampada Games", "Yes", 75, 60, 72, 68, "Pohutukawa"))
total_house_events.append(Event("House Trivia", "No", 66, 68, 74, 73, "Kowhai"))


# Creating an option menu that will be used to display the events that have been added.
chosen_event = tkinter.StringVar()
chosen_event.set("Choose a event")

event_name = tkinter.OptionMenu(details_frame, chosen_event, *event_names_list, "")
event_name.grid(row=0, column=1)

# It takes the total points of each team and displays them in the leaderboard frame.
def leaderboard(total_yellow_points, total_red_points, total_blue_points, total_green_points):
    for data in total_house_events:
        total_yellow_points += data.yellow_p
        total_red_points += data.red_p
        total_blue_points += data.blue_p
        total_green_points += data.green_p
    Label(leaderboard_frame, text=total_yellow_points).grid(column=1, row=1, sticky=W)
    Label(leaderboard_frame, text=total_red_points).grid(column=1, row=2, sticky=W)
    Label(leaderboard_frame, text=total_blue_points).grid(column=1, row=3, sticky=W)
    Label(leaderboard_frame, text=total_green_points).grid(column=1, row=4, sticky=W)

# It takes the values from the entry boxes and assigns them to variables.
def save():
    global chosen_event
    global event_name
    name = event_name_input.get()
    eventtype = is_sport.get()
    yellow_p = int(yellow_points.get())
    red_p = int(red_points.get())
    blue_p = int(blue_points.get())
    green_p = int(green_points.get())

# Checking if the name of the event is not empty and if the name of the event is not in the list of
# events. If it is not in the list of events, it will add the points of each house to a list and sort
# them in descending order. It will then check if the points of each house is greater than 100. If it
# is, it will display a warning message.
    
    if name.strip() != " " and name not in event_names_list:
        scores = [("Kowhai ", yellow_p),("Pohutukawa ", red_p),("Kauri ", blue_p),("Rimu ", green_p)]
        scores.sort(reverse=True, key=lambda x: x[1])
        if yellow_p > 100 or red_p > 100 or blue_p > 100 or green_p > 100:
            messagebox>messagebox.showwarning("Points Error","Maximum number you can input is 100")
  
  
        # Checking if the points of each house is equal to each other. If it is, it will set the winner
        # to "Tie". If it is not, it will set the winner to the house with the highest points.
        else:
            validate =  None
            if scores[0][1] == scores[1][1]:
                validate = True
            else:
                validate = False
            if scores[0][1] != 0:
                if validate == True:
                    winner = "Tie "
                else:
                    winner = scores[0][0]
            else:
                winner = 0
            # Adding the name of the event to the list of events.
            event_names_list.append(str(name))
            # Adding the name of the event, event type, points for each house, and the winner to the
            # list of events.
            total_house_events.append(Event(name, eventtype, yellow_p, red_p, blue_p, green_p, winner))
           
            leaderboard(0,0,0,0)
            
            # Destroying the option menu and then creating a new one with the updated list of events.
            event_name.destroy()
            chosen_event = tkinter.StringVar()
            chosen_event.set("Choose a event")
            event_name = tkinter.OptionMenu(details_frame, chosen_event, *event_names_list)
            event_name.grid(row=0, column=1)
    # Checking if the name of the event is in the list of events. If it is, it will display a message
    # saying that an event with that name has already been added.
    elif name in event_names_list:
        messagebox.showinfo("Event Name Error","An event with this name has already been added")

# It takes the chosen event from the drop down menu and then searches through the list of events to
# find the one that matches the chosen event.
def print_details():
     input = chosen_event.get()
     for info in total_house_events:
        if input == info.name:
            global event_name
            event_name.destroy()
            event_name = tkinter.OptionMenu(details_frame, chosen_event, *event_names_list)
            event_name.grid(row=0, column=1)
            tkinter.messagebox.showinfo("Chosen event details","\n".join(info.details()))

# Creating buttons that will be used to save the details, show the details, and show the leaderboard.
tkinter.Button(input_frame, text="Save Details", command=save).grid(row=7, column=0, columnspan=3, pady=5)
tkinter.Button(details_frame, text="Show Scores", command=print_details).grid(column=1, row=1, columnspan=1)


main.mainloop()