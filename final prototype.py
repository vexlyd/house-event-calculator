# Prototype 3

import tkinter
from tkinter import *
from tkinter import messagebox

tk = tkinter
main = Tk()
main.title("House Event Calculator")
main.geometry("500x300")

All_events = []
event_name_list = []

input_frame = LabelFrame(main, text= "Details Input")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W)
details_frame = LabelFrame(main, width='100')
details_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=N)
leaderboard_frame = LabelFrame(main)
leaderboard_frame.grid(row=0, column=1, padx=10, pady=10, sticky=E)

tk.Label(input_frame, text="Event Name").grid(column=0, row=0, sticky=W)
tk.Label(input_frame, text="Is the event a sport").grid(column=0, row=1, sticky=W)
tk.Label(input_frame, text="Yellow").grid(column=0, row=2, sticky=W)
tk.Label(input_frame, text="Green").grid(column=0, row=3, sticky=W)
tk.Label(input_frame, text="Red").grid(column=0, row=4, sticky=W)
tk.Label(input_frame, text="Blue").grid(column=0, row=5, sticky=W)

tk.Label(details_frame, text="Name of Event").grid(column=0, row=0, sticky=W)
event_name_input = tk.Entry(input_frame)
is_sport = tk.StringVar()
is_sport.set("YES")
Radiobutton(input_frame, text="YES", variable=is_sport, value="YES").grid(column=1, row=1)
Radiobutton(input_frame, text="NO", variable=is_sport, value="NO").grid(column=2, row=1)

yellow_points = Spinbox(input_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly")
green_points = Spinbox(input_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly")
red_points = Spinbox(input_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly")
blue_points = Spinbox(input_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly")

event_name_input.grid(column=1, row=0, columnspan=2, padx=2)
yellow_points.grid(column=1, row=2, columnspan=2)
green_points.grid(column=1, row=3, columnspan=2)
red_points.grid(column=1, row=4, columnspan=2)
blue_points.grid(column=1, row=5, columnspan=2)

Label(leaderboard_frame, text="LEADERBOARD").grid(column=0, row=0, columnspan=2, pady=10)
Label(leaderboard_frame, text="YELLOW HOUSE").grid(column=0, row=1, sticky=W, pady=5)
Label(leaderboard_frame, text="GREEN HOUSE").grid(column=0, row=2, sticky=W, pady=5)
Label(leaderboard_frame, text="RED HOUSE").grid(column=0, row=3, sticky=W, pady=5)
Label(leaderboard_frame, text="BLUE HOUSE").grid(column=0, row=4, sticky=W, pady=5)

class Event:
    def __init__(self, name, event_type, yellow_points, green_points, red_points, blue_points, winner):
        self.name = name
        self.event_type = event_type
        self.yellow_points = yellow_points
        self.green_points = green_points
        self.red_points = red_points
        self.blue_points = blue_points
        self.winner = winner
        
    def get_details(self):
        return(["Event Name " + self.name, "Is sport " + self.event_type, "Yellow House Points" + str(self.yellow_points), "Green House Points" + str(self.green_points), "Red House Points" + str(self.red_points), "Blue House Points" + str(self.blue_points), "The Winner Is" + self.winner])

chosen_event = tkinter.StringVar()
chosen_event.set("Choose an event")
event_name_dropdown = tkinter.OptionMenu(details_frame, chosen_event, *event_name_list, All_events)
event_name_dropdown.grid(row=0, column=1)

def leaderboard(total_yellow_house_points, total_green_house_points, total_red_house_points, total_blue_house_points):
    for obj in All_events:
        total_yellow_house_points = obj.yellow_points
        total_green_house_points = obj.green_points
        total_red_house_points = obj.red_points
        total_blue_house_points = obj.blue_points

    Label(leaderboard_frame, text=total_yellow_house_points).grid(column=1, row=1, sticky=W)
    Label(leaderboard_frame, text=total_green_house_points).grid(column=1, row=2, sticky=W)
    Label(leaderboard_frame, text=total_red_house_points).grid(column=1, row=3, sticky=W)
    Label(leaderboard_frame, text=total_blue_house_points).grid(column=1, row=4, sticky=W)

leaderboard(0, 0, 0, 0)

def save_input():
    global chosen_event
    global event_name_dropdown
    name = event_name_input.get()
    event_type = is_sport
    yellow_house = int(yellow_points.get())
    green_house = int(green_points.get())
    red_house = int(red_points.get())
    blue_house = int(blue_points.get())

    if name.strip() != "" and name not in event_name_list:
        points = [("Yellow", yellow_house), ("Green", green_house), ("Red", red_house), ("Blue", blue_house)]
        points.sort(reverse=YES, key= lambda x: x[1])

        if yellow_house == 0 and green_house == 0 and red_house == 0 and blue_house == 0:
            messagebox.showerror("Please enter points for each house")
        else:
            event_name_list.append(str(name))
            first_scan = None
            second_scan = None
            third_scan = None

            if points[0][1] == points[1][1]:
                first_scan = True
                if points[1][1] == points[2][1]:
                    second_scan = True
                    if points[2][1] == points[3][1]:
                        third_scan = True
                    else:
                        third_scan = False
                else:
                    second_scan = False
            else:
                first_scan = False
                second_scan = False
                third_scan = False
            
            if points[0][1] != 0:
                if first_scan == True:
                    if second_scan == True:
                        if third_scan == True:
                            who_won = "All teams have tied"
                        else:
                            who_won = points[0][0] + ", " + points[1][0] + ", " + points[2][0]
                    else:
                        who_won  = points[0][0] + ", " + points[1][0]
                else:
                    who_won = points[0][0]
            else:
                who_won = 0

            All_events.append(Event(name, event_type, yellow_points, green_points, red_points, blue_points, who_won))

            leaderboard(0, 0, 0, 0)

            event_name_dropdown.destroy()
            chosen_event = tkinter.StringVar()
            chosen_event.set("Choose an event")
            event_name_dropdown = tkinter.OptionMenu(details_frame, chosen_event, *event_name_list)
            event_name_dropdown.grid(row=0, column=1)

    elif name in event_name_list:
        messagebox.showwarning("A event with the name has already been added")
    elif name.strip() == "":
        messagebox.showwarning("You have to enter a name for the event")

def print_details():
    entry = chosen_event.get()
    for info in All_events:
        if entry == info.name:
            global event_name_dropdown 
            event_name_dropdown.destroy()
            event_name_dropdown = tkinter.OptionMenu(details_frame, chosen_event, *event_name_list)
            event_name_dropdown.grid(row=1, column=1)
            tkinter.messagebox.showinfo("Event Details", "\n".join(info.get_details()))

tk.Button(input_frame, text="Submit Details", command=save_input).grid(row=7, column=0, columnspan=3, pady=5)
tk.Button(details_frame, text="Show Events", command=print_details).grid(column=0, row=1, columnspan=2)

main.mainloop()